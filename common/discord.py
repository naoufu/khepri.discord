import discord
import re
from config.discord import *

class DiscordHelper(object):
    @staticmethod
    def filter_content(message: discord.Message):
        # Replace mentions with names
        filtered_content = message.content
        if filtered_content is not None and STRIP_EMOTES is True:
            filtered_content = re.sub(r'<(a?):([A-Za-z0-9_]+):([0-9]+)>', '', filtered_content)
            filtered_content = filtered_content.strip()

        # Filters punctuations away for better or worse, it won't respond to random punctuations
        if filtered_content.startswith:
            filtered_content = re.sub(r'[^\w\s]', '', filtered_content)
            filtered_content = filtered_content.strip()

        for mention in message.mentions:
            try:
                if mention.nick is not None:
                    replace_name = mention.nick
                else:
                    replace_name = mention.name
            except AttributeError:
                replace_name = mention.name
            replace_id = mention.id
            replace_tag = "<@%s>" % replace_id
            filtered_content = filtered_content.replace(replace_tag, replace_name)
        return filtered_content
