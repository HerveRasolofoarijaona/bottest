# Instagram DM bot

Instagram DM bot with account switcher feature. This bot can send messages automatically in your list of usernames.
It will send DMs and switch account automatically. It will switch account every 10 messages, so this means it will
change account after it sends message to 10 usernames and then it will go to the next account.

## Setup Bot

1.  Git clone this repo with this command --> `git clone https://github.com/HerveRasolofoarijaona/bottest.git`
2.  Install requirements with this command --> `pip install -r requirements.txt`
3.  Setup your username --> `infos/accounts.json`
4.  Open infos folder and fill your infos of accounts in accounts.json file, in messages.txt put your message list and
    in usernames.txt put you username list that you want to send dm.
5.  Run the bot with this command --> `python run.py`
6.  To wrap messages sent by the bot in sentence on one line in message.txt --> `@n one line, @n@n to line` 
7.the message to be written must be a line in the txt file otherwise the bot would not recognize it


Thank You!
