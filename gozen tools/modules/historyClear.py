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

def progressbar(it, prefix="", size=60, file=sys.stdout): # Setup the progress bar to be used later
    count = len(it) # Get the lenght of the loop

    def show(i, user): # Define a function to show the current progress bar
        x = int(size * i / count) # Get the lenght of the bar

        file.write(f"{r2} [{b}!{r2}] {r}|{r2}{'#' * x}{'.' * ( size - x )}{r}| {r2}{i}{r}/{r2}{count} {r}|{r2} {str(user):<30}              {r}\r")
        file.flush() # Print out the bar

    if count > 0:

        show(0, "None") # Show the bar empty
        for i, item in enumerate(it): # Loop over the iterator
            show(i+1, item) # Show the progress bar at its current state
            yield item # Yield the item allowing us to loop over the function later

        show(len(it), "Done") # Show the progress bar is done

        file.write("\n") # Flush the newline
        file.flush()
    else:
        print(f"{r2} [{b}?{r2}] {r}|{r2}{'#' * 60}{r}| {r2}0{r}/{r2}0 {r}|{r2} No messages found")

def clear():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {r2}[{b}?{r2}] Token: ")
    }

    id = input(f" {r2}[{b}?{r2}] Channel ID: ")

    author = requests.get("https://discord.com/api/users/@me", headers = headers).json()["id"]

    allMessages = []

    messages = requests.get(
        f"https://discord.com/api/channels/{id}/messages",
        headers = headers,
        params = {"limit" : 100}
    )

    if messages.status_code != 200:
        print(f" {r2}[{b}!{r2}] Channel not found")
        return

    for x in messages.json():
        if x["author"]["id"] == author:
            allMessages.append(x["id"])

    try:
        for i in range(0, 1000, 100):
            messages = messages.json()
            messages = requests.get(
                f"https://discord.com/api/channels/{id}/messages",
                headers = headers,
                params = {"limit" : 100, "before" : messages[-1]["id"]}
            )
            if messages.status_code != 200:
                break

            for x in messages.json():
                if x["author"]["id"] == author:
                    allMessages.append(x["id"])
    except IndexError:
        pass

    for i in progressbar(allMessages, "", 60):
        responce = requests.delete(
            f"https://discord.com/api/channels/{id}/messages/{i}",
            headers = headers
        )
        time.sleep(2.5)

        while responce.status_code != 204:
            responce = requests.delete(
                f"https://discord.com/api/channels/{id}/messages/{i}",
                headers = headers
            )
            time.sleep(2.5)
