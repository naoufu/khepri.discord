class DiscordApiCredentials(object):
    def __init__(self, token: str):
        self.token = token


# ----------DISCORD TOKEN SECTION----------
# -----------------------------------------

DISCORD_CLIENT_ID = 69696969696969696969
DISCORD_TOKEN = 'REPLACEME'

DISCORD_CREDENTIALS = DiscordApiCredentials(token=DISCORD_TOKEN)

DISCORD_USERNAME = 'YourDiscordBOT#6969'

# ---------Server Specific Section --------
# -----------------------------------------

# Prefix for the bot to recognise when you're talking to it, other the @bot mention and auto_talk channels
CHATTER_PREFIX = ['']

# Talk normally to the bot like you're conversing, without any prefix or ping
# This requires a channel name, you can add multiple auto talk channels with a comma.
DISCORD_AUTO_TALK = ['']
# -----------------------------------------
# -----SERVER SPECIFIC SECTION ENDS HERE---

# -----------ALWAYS LEARN------------------
# -----------------------------------------
# Learn from any of these channels
# If this channel is set, it will ignore DISCORD_LEARN_FROM_ALL setting and will explicitly learn in the channel.
DISCORD_LEARN_CHANNEL = ['']

# Always learn from a specific user no matter what other flags are set
# This should be set to a string containing a username like "SomeGuy#1234"
DISCORD_LEARN_FROM_USER = ['']

# Learn from direct messages
DISCORD_LEARN_FROM_DIRECT_MESSAGE = False

# Learn from all servers and channels
# If you have a large server, it will learn from bot channels too, if you enable this be sure to disable the bot from reading the channel.
DISCORD_LEARN_FROM_ALL = False
# -----------------------------------------
# -----------ALWAYS LEARN ENDS HERE---------


# -------IGNORE SECTION--------------------
# -----------------------------------------

# Don't learn anything from selected user/s
# This is a username string like, 'SomeDiscordDude#1234'
DISCORD_LEARN_NEGLECT_USERNAMES = []
# Similar as above but just userID
DISCORD_LEARN_NEGLECT_UIDS = []

# Absolutely disable the bot from learning anything with-in the server/s
# This is done by ignoring the server ID but DOES permit them from interacting
# I would only have this on, IF "DISCORD_AUTO_TALK" and "DISCORD_LEARN_CHANNEL" names match
# and "DISCORD_LEARN_FROM_USER" is inside the named server.
DISCORD_LEARN_SERVER_ID_EXCEPTIONS = []

# Don't learn from any of these channels
DISCORD_LEARN_CHANNEL_EXCEPTIONS = []
#------------------------------------------
#--------IGNORE SECTION ENDS HERE----------


#------EXTRA STUFF-------------------------
#------------------------------------------
# Embed footer messages, you can ignore here but you can add variations on the embed messages when talking to the bot
TALKING_TO = ['Responding to ',
              'Talking to ',
              'Really bored and learning from ',
              'Will dominate the world with ',
              'Plotting schemes with ']

# Housekeeping
DISCORD_REMOVE_URL = True
EMOTES_SKIP = True

# Stips discord emotes from messages
STRIP_EMOTES = True
# -----------------------------------------
# -----EXTRA STUFF ENDS HERE---------------


# --------- Technical Stuff Section -------
# -----------------------------------------
# Store training data here
DISCORD_TRAINING_DB_PATH = 'db/discord.db'
# -----------------------------------------
