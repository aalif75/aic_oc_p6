


"""  script creation  utisateurs  à distance à partir de fichier csv 
avec  mot de passe generique  "Pass@2022"  pour tous les utlisateurs sur un client linux unbuntu 20.04

"""

import subprocess
import sys



# Fonction creation nouveaux utilsateurs

def creat_user(liste_donnees):
    # Appel module connect_ssh
    # appel module lecteur_csv

    for i in liste_donnees:
        username = i["login"]  # attribition  variable username à partir  du dico liste_donnes() du module lecteur_csv
        password = "Pass@2022"

        try:
            # executing useradd command using subprocess module
           #  subprocess.run(['useradd', '-p', password, username])
            print(f"utilisateur créé:"+username)
        except:
            print(f" Echec Cceation utlisateur.")
            sys.exit(1)


creat_user()