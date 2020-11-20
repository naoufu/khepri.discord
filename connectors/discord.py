import asyncio
import re

import discord
import logging
from discord.ext import commands
from config.discord import *
from connectors.connector_common import *
from storage.discord import DiscordTrainingDataManager
from common.discord import DiscordHelper
from spacy.tokens import Doc

from datetime import datetime
t1 = datetime.now()
import tensorflow as tf
import sys

class DiscordReplyGenerator(ConnectorReplyGenerator):
    def generate(self, message: str, doc: Doc = None) -> Optional[str]:

        reply = ConnectorReplyGenerator.generate(self, message, doc, ignore_topics=[DISCORD_USERNAME.split('#')[0]])

        if reply is None:
            return None

        if DISCORD_REMOVE_URL:
            # Remove URLs
            reply = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', reply)
            reply = reply.strip()
        if EMOTES_SKIP:
            # Strips discord emotes
            reply = re.sub(r'<(a?):([A-Za-z0-9_]+):([0-9]+)>', '', reply)
            reply = reply.strip()
        if len(reply) > 0:
            return reply
        else:
            return None


class DiscordClient(discord.Client):

    def __init__(self, worker: 'DiscordWorker'):
        discord.Client.__init__(self, activity=discord.Game(name="My reality", type=3), status=discord.Status.dnd)
        self._worker = worker
        self._ready.set()
        self._logger = logging.getLogger(self.__class__.__name__)

    async def on_ready(self):
        self._ready.set()
        self._logger.info(
            "Server join URL: https://discord.com/oauth2/authorize?&client_id=%d&scope=bot&permissions=379968"
            % DISCORD_CLIENT_ID)
        print('--------')
        print('--------')
        print('Using Python ' + (sys.version))
        print('--------')
        print('Using Tensorflow '+ tf.__version__)
        print('--------')
        print("Ready in " + datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        print('--------')
        print("Discord.py verison: " + discord.__version__)
        print('--------')
        print('Connected to ' + str(self.user.name) + '#' + str(self.user.discriminator))
        print('--------')
        print('--------')

    async def on_message(self, message: discord.Message):
        # Ignore attachements and Feedback Loop
        if message.attachments or message.author.bot:
            return

        filtered_content = DiscordHelper.filter_content(message)

        # Ignore empty and letter messages
        if not len(filtered_content) > 2:
            return
        if filtered_content == '':
            return

        learn = False
        # Learn from private messages
        if message.guild is None and DISCORD_LEARN_FROM_DIRECT_MESSAGE:
            DiscordTrainingDataManager().store(message)
            learn = True
        # Learn from all server messages
        elif message.guild is not None and DISCORD_LEARN_FROM_ALL:
            if str(message.channel) not in DISCORD_LEARN_CHANNEL_EXCEPTIONS:
                DiscordTrainingDataManager().store(message)
                learn = True
        # Learn will accept new input from specified channel and neglect specified user
        elif str(message.channel) in DISCORD_LEARN_CHANNEL and message.content is not None:
            if str(message.author) in DISCORD_NEGLECT_LEARN:
                return
            else:
                DiscordTrainingDataManager().store(message)
                learn = True
        # Learn from Specific User
        elif str(message.author) == DISCORD_LEARN_FROM_USER:
            DiscordTrainingDataManager().store(message)
            learn = True
        # Real-time learning
        if learn:
            self._worker.send(ConnectorRecvMessage(filtered_content, learn=True, reply=False))
            self._worker.recv()


        # This pulls from discord config, just the embed footer for gags
        TALKING_VARIANT = random.choice(TALKING_TO)
        # Reply to mentions
        # Typically has embeds so be sure to enable the embed permission across all channels
        for mention in message.mentions:
            if str(mention) == DISCORD_USERNAME:
                self._logger.debug("Message: %s" % filtered_content)
                self._worker.send(ConnectorRecvMessage(filtered_content))
                reply = self._worker.recv()
                self._logger.debug("Reply: %s" % reply)
                if reply is not None:
                    embed = discord.Embed(description=reply, color=message.author.color)
                    embed.set_footer(text = TALKING_VARIANT + message.author.name, icon_url = message.author.avatar_url)
                    embed.timestamp = datetime.utcnow()
                    await asyncio.sleep(0.25)
                    await message.channel.send(embed=embed)
                return

        # Extra chunck where the bot will reply via keyword or prefix found in CHATTER_PREFIX
        # Keep in mind this can happen anywhere the bot has access to send messages
        if message.content.lower().startswith(tuple(CHATTER_PREFIX)):
            self._logger.debug("Message: %s" % filtered_content)
            self._worker.send(ConnectorRecvMessage(filtered_content))
            reply = self._worker.recv()
            self._logger.debug("Reply: %s" % reply)
            if reply is not None:
                embed = discord.Embed(description=reply, color=message.author.color)
                embed.set_footer(text = TALKING_VARIANT + message.author.name, icon_url = message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await asyncio.sleep(0.25)
                await message.channel.send(embed=embed)
            return

        # Channel which the bot will respond without any prefixes or @mentions
        elif str(message.channel) in DISCORD_AUTO_TALK and message.content is not None:
            self._logger.debug("Message: %s" % filtered_content)
            self._worker.send(ConnectorRecvMessage(filtered_content))
            reply = self._worker.recv()
            self._logger.debug("Reply: %s" % reply)
            if reply is not None:
                embed = discord.Embed(description=reply, color=message.author.color)
                embed.set_footer(text = str(TALKING_VARIANT) + message.author.name, icon_url = message.author.avatar_url)
                embed.timestamp = datetime.utcnow()
                await asyncio.sleep(0.25)
                await message.channel.send(embed=embed)
            return

        # For the bot to reply in private messages, no embeds for private channels
        elif message.guild is None:
                self._logger.debug("Private Message: %s" % filtered_content)
                self._worker.send(ConnectorRecvMessage(filtered_content))
                reply = self._worker.recv()
                self._logger.debug("Reply: %s" % reply)
                if reply is not None:
                    await asyncio.sleep(0.25)
                    await message.channel.send(reply)
                return

class DiscordWorker(ConnectorWorker):
    def __init__(self, read_queue: Queue, write_queue: Queue, shutdown_event: Event,
                 credentials: DiscordApiCredentials):
        ConnectorWorker.__init__(self, name='DiscordWorker', read_queue=read_queue, write_queue=write_queue,
                                 shutdown_event=shutdown_event)
        self._credentials = credentials
        self._client = None
        self._logger = None

    async def _watchdog(self):
        while True:
            await asyncio.sleep(0.2)

            if self._shutdown_event.is_set():
                self._logger.info("Got shutdown signal.")
                await self._client.close()
                return

    def run(self):
        from storage.discord import DiscordTrainingDataManager
        self._logger = logging.getLogger(self.__class__.__name__)
        self._db = DiscordTrainingDataManager()
        self._client = DiscordClient(self)
        self._client.loop.create_task(self._watchdog())
        self._client.run(self._credentials.token)


class DiscordScheduler(ConnectorScheduler):
    def __init__(self, shutdown_event: Event, credentials: DiscordApiCredentials):
        ConnectorScheduler.__init__(self, shutdown_event)
        self._worker = DiscordWorker(read_queue=self._write_queue, write_queue=self._read_queue,
                                     shutdown_event=shutdown_event, credentials=credentials)


class DiscordFrontend(Connector):
    def __init__(self, reply_generator: DiscordReplyGenerator, connectors_event: Event,
                 credentials: DiscordApiCredentials):
        Connector.__init__(self, reply_generator=reply_generator, connectors_event=connectors_event)
        self._scheduler = DiscordScheduler(self._shutdown_event, credentials)
