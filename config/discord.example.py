class DiscordApiCredentials(object):
    def __init__(self, token: str):
        self.token = token


# --- "User" Stuff Section ---
# ----------------------------

DISCORD_CLIENT_ID = 69696969696969696969
DISCORD_TOKEN = 'REPLACEME'

DISCORD_CREDENTIALS = DiscordApiCredentials(token=DISCORD_TOKEN)

DISCORD_USERNAME = 'YourDiscordBOT#6969'

# Prefix for the bot to recognise when you're talking to it, other the @bot mention and auto_talk channels
CHATTER_PREFIX = ['']

# Talk normally to the bot like you're conversing, without any prefix or ping
# This requires a channel name, you can add multiple auto talk channels with a comma.
DISCORD_AUTO_TALK = ['']

# Learn from all servers and channels
# If you have a large server, it will learn from bot channels too, if you enable this be sure to disable the bot from reading the channel.
DISCORD_LEARN_FROM_ALL = False

# Learn from any of these channels
# If this channel is set, it will ignore DISCORD_LEARN_FROM_ALL setting and will explicitly learn in the channel.
DISCORD_LEARN_CHANNEL = ['']

# Learn from direct messages
DISCORD_LEARN_FROM_DIRECT_MESSAGE = False

# Always learn from a specific user no matter what other flags are set
# This should be set to a string containing a username like "SomeGuy#1234"
DISCORD_LEARN_FROM_USER = None

# Don't learn from any of these channels
DISCORD_LEARN_CHANNEL_EXCEPTIONS = []

# Don't learn anything from selected user/s
# This is a username string like, 'SomeDiscordDude#1234'
DISCORD_NEGLECT_LEARN = []

# Embed footer messages, you can ignore here but you can add variations on the embed messages when talking to the bot
TALKING_TO = ['Responding to ',
              'Talking to ',
              'Really bored and learning from ',
              'Will dominate the world with ',
              'Plotting schemes with ']
# --- Technical Stuff Section ---
# -------------------------------

# Housekeeping
DISCORD_REMOVE_URL = True
EMOTES_SKIP = True

# Stips discord emotes from messages
STRIP_EMOTES = True

# Store training data here
DISCORD_TRAINING_DB_PATH = 'db/discord.db'
