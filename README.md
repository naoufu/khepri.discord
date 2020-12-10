# Khepri Discord Bot
- Based off from [csvance's armchair-expert](https://github.com/csvance/armchair-expert), a machine learning chatbot that mainly operates as a Discord Server Bot.
- A private bot, which you will need to run your own instance.


## Changes
- has been updated portions of the code to work with discord
- improved interactions in interacting with the bots
- now strips punctuations when processing messages and wont respond to !!!! messages or spam punctuations
- Upgraded Tensorflow and able to use above Tensorflow 2.0+

## Features
- Uses NLP to select the most optimal subjects for which to generate a response
- Uses a Recurrent Neural Network (RNN) to structure and capitalize the output, mimicking sentence structure and capitalization of learned text
- Learns new words in real-time with an n-gram markov chain, which is positionally aware of the distances between different words, creating a more coherent sentence

## Running your own Installation
- Any device windows or any linux distro with at least 3 GB of ram
- Python 3.7 at least
- If no version is specified, you can run the latest version of the package.

You typically need to install the following requirements:
- tensorflow-cpu or tensorflow
- keras(Tensorflow backend)
- spaCy
- spacymoji
- numpy==1.16.3
- tweepy
- discord.py
- sqlalchemy

This was ran under a **Windows** enviroment, so `python` could be `python3` in linux.
**First:** Run the Requirements.txt file in the root folder:

*I really recommend you install this in a virtual env, as you will install specific versions of some packages which might conflict on what you have. If not, you can just install it normally.*

If you run into any issues, just run the command below.
```
pip install -r requirements.txt
```
--------------------------------------------------

### Setup & Training:
Navigate to the `\armchairexpert\config` folder:
- Create a copy of armchair_expert.example.py and rename it to armchair_expert.py
- Create a copy of config/ml.example.py and rename it to config/ml.py
- Then go back to the root folder `\armchairexpert\`
- It is preferred to import data first for training before starting the bot.
  - You can use the provided import script in `\scripts\import_text_file.py`
  - Simply copy the script to the root folder, together with your txt file and run it as:
    `python import_txt.py "<your-data-file-name-here>"`
  - It would look like this: `python import_text_file.py "CAN YOU HEAR ME.txt"`
  - Another option is to let the bot run for a while and learn from the user messages being sent in the servers.
- Every time the bot starts it will train on all new data it acquired since it started up last
-The bots sentence structure model is only trained once on initial start-up.
To train it with the most recent acquired data, start the bot with the `--retrain-structure flag`. If you are noticing the bot is not generating sentences which the structure of learned material, this will help.

### Connectors
#### Discord:
- Before you can run the bot, you will need to have a [Discord app](https://discord.com/) account and register a [discord bot](https://discord.com/developers/applications/me#top) to interface with.
- You can take a look and see a step by step instructions on how to create and add the bot into your server, [Here](https://discordpy.readthedocs.io/en/latest/discord.html).

#### Filling in the discord bot info and configuration:
*The following configuration is enough to make the bot running. To configure and refine how the bot learns, you need to check the [Wiki](https://github.com/naoufu/khepri.discord/wiki) for additional info and explainations.*
- Navigate to the `\armchairexpert\config` folder:
- Create a copy of discord.example.py and rename it to discord.py
- Open the discord.py file with your text editor and fill the required fields.
- Now copy the **Client ID**, **Username#xxxx**, and **TOKEN** to the discord.py file.
- Change the configuration as you wish, for instance enabling learn from all, etc.
- Go back to the `\armchairexpert\` Directory
- open console within the directory and run, `python armchair.py`
- When the bot starts you should see a message print to the console containing a link which will allow you to join the bot to a server.

#### Twitter (I've only prioritised discord and is not updated, not sure if twitter changed their api or not. Proceed at your own expense.)
You can just skip this if you want discord.
- You will need to create an application on the twitter developer site on your bot's twitter account https://apps.twitter.com
- After creating it, assign it permissions to do direct messages (this isn't default)
- Create an access token for your account
- Copy config/twitter.example.py to config/twitter.py
- Fill in the tokens and secrets along with your handle
- Go back to the Root Directory
- python armchair.py

## LICENSE
```
MIT License

Copyright (c) 2017 Carroll Vance

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
