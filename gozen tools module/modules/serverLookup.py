LICNECE = """
Copyright © 2021 𓇬| gozen#0666
L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "logiciel"), de traiter le logiciel sans restriction, y compris, sans s'y limiter, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de sous-licence et/ou de vente de copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni à le faire, sous réserve des conditions suivantes :
L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.
LE LOGICIEL EST FOURNI " EN L'ÉTAT ", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU TOUTE AUTRE TRANSACTION DU LOGICIEL.
"""

from colored import fg, attr
import requests
import time
import sys

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def fetch_data():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {w}[{b}?{w}] Token: ")
    }

    guildId = input(f" {w}[{b}?{w}] Guild Id: ")

    response = requests.get(
        f"https://discord.com/api/guilds/{guildId}",
        headers = headers,
        params = {"with_counts" : True}
    ).json()

    owner = requests.get(
        f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
        headers = headers,
        params = {"with_counts" : True}
    ).json()

    print(f"""
Server name: {response['name']} ~ {response['id']}
Icon URL: https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
Approxomate member count: {response['approximate_member_count']}
Owner: {owner['user']['username']}#{owner['user']['discriminator']} ~ {response['owner_id']}
Region: {response['region']}
Valnaty invite: {response['vanity_url_code']}
""")

if __name__ == '__main__':
    fetch_data()
