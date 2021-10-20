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

def spammer():
    webhook = input(f"\n {r2}[{b}?{r2}] Webhook Url: ")
    message = input(f" {r2}[{b}?{r2}] Message: ")
    timer = input(f" {r2}[{b}?{r2}] Amount of time for the attack (s): ")
    print("")

    timeout = time.time() + 1 * float(timer) + 2

    while time.time() < timeout:
        response = requests.post( # Send the webhook message
            webhook,
            json = {"content" : message},
            params = {'wait' : True}
        )

        if response.status_code == 204 or response.status_code == 200:
            print(f" {r2}[{b}+{r2}] Message sent")
        elif response.status_code == 429:
            print(f" {r2}[{b}-{r2}] Rate limited ({response.json()['retry_after']}ms)")
            time.sleep(response.json()["retry_after"] / 1000)
        else:
            print(f" {r2}[{b}-{r2}] Error code: {response.status_code}")

        time.sleep(.5)
