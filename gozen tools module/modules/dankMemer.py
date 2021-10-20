LICNECE = """
Copyright © 2021 𓇬| gozen#0666
L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "logiciel"), de traiter le logiciel sans restriction, y compris, sans s'y limiter, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de sous-licence et/ou de vente de copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni à le faire, sous réserve des conditions suivantes :
L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.
LE LOGICIEL EST FOURNI " EN L'ÉTAT ", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU TOUTE AUTRE TRANSACTION DU LOGICIEL.
"""

# 
# This is the source code for my dank memer gridner, if you want to create a custom action you can head down to line 42, the bot will run the command then wait the set amount of seconds and type it agein, do whatever you want you can add stuff such as "pls steal..." or "pls buy..."
# 

from colored import fg, attr
import requests
import threading
import time
import random

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def start():
    token = input(f"\n {r2}[{b}?{r2}] Token: ")
    channel = input(f" {r2}[{b}?{r2}] Channel Id: ")

    def execute_command(command = "", cooldown = 0):
        print(f"{r2}[{b}!{r2} Loaded: '{command}' With cooldown of {cooldown} Seconds")
        while True:
            requests.post(
                f"https://discord.com/api/channels/{channel}/messages",
                data = {'content': command},
                headers = {
                    'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                    'Authorization' : token
                }
            )
            print(f"{r2}[{b}+{r2}] '{command}' Ran successfully")

            time.sleep(cooldown + random.randint(2, 10))

    commands = {
        "pls beg" : 45,
        "pls hunt" : 40,
        "pls fish" : 40,
        "pls daily" : 86400
    }

    print()

    for cmd, cooldown in commands.items():
        threading.Thread(target = execute_command, kwargs = {"command" : cmd, "cooldown" : cooldown}).start()
        time.sleep(5)
