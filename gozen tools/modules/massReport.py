LICNECE = """
Copyright © 2021 𓇬| gozen#0666
L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "logiciel"), de traiter le logiciel sans restriction, y compris, sans s'y limiter, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de sous-licence et/ou de vente de copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni à le faire, sous réserve des conditions suivantes :
L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.
LE LOGICIEL EST FOURNI " EN L'ÉTAT ", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU TOUTE AUTRE TRANSACTION DU LOGICIEL.
"""

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
    guildId = input(f" {r2}[{b}?{r2}] Server Id: ")
    channelId = input(f" {r2}[{b}?{r2}] Channel Id: ")
    messageId = input(f" {r2}[{b}?{r2}] Message Id: ")
    reason = input(f" {r2}[{b}?{r2}] Reason: ")

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : token,
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
    }

    payload = {"guild_id" : guildId, "channel_id" : channelId, "message_id" : messageId, "reason" : reason}

    def report():
        while True:
            response = requests.post(
                'https://discord.com/api/v6/report',
                headers = headers,
                json = payload
            )
            if response.status_code == 201:
                print(f" {r2}[{b}+{r2}] Report sent successfully")
            elif response.status_code == 429:
                print(f" {r2}[{b}!{r2}] Ratelimited, waiting 5 seconds")
                time.sleep(5)
            elif response.status_code == 401:
                print(f" {r2}[{b}!{r2}] Invalid token")
                return
            else:
                print(f" {r2}[{b}!{r2}] Unknown error: {response.status_code}")

    for i in range(500):
        threading.Thread(target = report).start()

if __name__ == '__main__':
    start()
