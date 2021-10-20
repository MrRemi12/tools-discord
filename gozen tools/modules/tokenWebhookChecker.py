LICNECE = """
Copyright © 2021 𓇬| gozen#0666
L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "logiciel"), de traiter le logiciel sans restriction, y compris, sans s'y limiter, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de sous-licence et/ou de vente de copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni à le faire, sous réserve des conditions suivantes :
L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.
LE LOGICIEL EST FOURNI " EN L'ÉTAT ", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU TOUTE AUTRE TRANSACTION DU LOGICIEL.
"""

from colored import fg, attr
import requests
import time

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def token():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")

    print(f" {r2}[{b}+{r2}] Getting user information")
    time.sleep(.5)

    user = requests.get("https://discord.com/api/users/@me", headers = {'Authorization' : token})

    if user.status_code == 401:
        print(f" {r2}[{b}!{r2}] Invalid Token")
        return

    servers = requests.get("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
    relations = requests.get("https://discord.com/api/v8/users/@me/relationships", headers = {'Authorization' : token}).json()

    user = user.json()

    print(f"\n {r2}[{b}!{r2}] Valid Token")
    print(f" {r2}[{b}+{r2}] User: {user['username']}#{user['discriminator']} | Email: {user['email']}")
    print(f" {r2}[{b}+{r2}] Guilds: {len(servers)} | Friends: {len([i for i in relations if i['type'] == 1])}")

    inp = input(f"\n {r2}[{b}?{r2}] Do you want to download aditional data? (Y/n)")

    if "y" in inp.lower():
        # if user["premium_type"] == 0:
        #     nitro = "None"
        # elif user["premium_type"] == 1:
        #     nitro = "Nitro Classic"
        # elif user["premium_type"] == 2:
        #     nitro = "Normal Nitro"

        serversOT = ""
        for i in servers:
            serversOT += f"Name: {i['name']}\nId: {i['id']} Owner: {i['owner']}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"

        relationsOT = ""
        for i in relations:
            if i['type'] == 1:
                relationsOT += f"Friend: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"
            elif i['type'] == 2:
                relationsOT += f"Blocked: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"
            elif i['type'] == 3:
                relationsOT += f"Incomming: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"
            elif i['type'] == 4:
                relationsOT += f"Outgoing: {i['user']['username']}#{i['user']['discriminator']} Id: {i['user']['id']}\n"

        if user['avatar'] is not None:
            avatar = f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png"
        else:
            avatar = "Not set"

        with open(f"TokenData {user['username']}#{user['discriminator']}.txt", "w", encoding = "utf-8") as file:
            file.write(
f"""~~~~~~~~~~~ USER INFORMATION ~~~~~~~~~~~
User: {user['username']}#{user['discriminator']}
Id: {user['id']}
Email: {user['email']}
Phone: {user['phone']}
Token: {token}
Avatar: {avatar}
2fA: {user['mfa_enabled']}
Languge: {user['locale']}

~~~~~~~~~~~ SERVER INFORMATOIN ~~~~~~~~~~~
{serversOT}
~~~~~~~~~~~ FRIEND INFORMATION ~~~~~~~~~~~
{relationsOT}""")

def webhook():
    webhook = input(f"\n {r2}[{b}?{r2}] Webhook Url: ")

    print(f" {r2}[{b}+{r2}] Webhook information")
    time.sleep(.5)

    responce = requests.get(
        webhook
    )

    if responce.status_code != 200:
        print(f" {r2}[{b}!{r2}] Invalid Webhook")
        return

    responce = responce.json()

    print(f"\n {r2}[{b}!{r2}] Valid Token")
    print(f" {r2}[{b}+{r2}] Name: {responce['name']} Id: {responce['id']}")
