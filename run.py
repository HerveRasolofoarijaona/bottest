import json
import random
from src.instadm import InstaDM

f = open('infos/accounts.json',)
accounts = json.load(f)

with open('infos/usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

# -- un text selon ton besoin
# -- python randomtext.py ou tu écris directement dans le fichier messages.txt
with open('infos/messages.txt', 'r') as f:
    messages = [line.strip() for line in f]

# -- Si t'as envie qu'il prenne des texte au hasard , tu décommente ici
# with open('infos/message.txt', 'r') as f:
#     messages = [line.strip() for line in f]


while True:
    if not usernames:
        print('Finished usernames.')
        break

    for account in accounts:
        if not usernames:
            break
        # Auto login
        insta = InstaDM(username=account["username"],
                        password=account["password"], headless=False)

        for i in range(10):

            if not usernames:
                break

            username = usernames.pop()
            # Send message
            insta.sendMessage(
                user=username, message=random.choice(messages))

        insta.teardown()
