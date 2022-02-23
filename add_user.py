
# script creation mulitiple users à partir de fichier user.txt
# avec  mot de passe generique  "Pass@2022"  pour tous les utlisateurs
#

# import modules  necessaires pour l'execution des scripts

import sys
import os
import getpass
import subprocess

def  add_user(username,password):
    try:
        subprocess.run(['useradd','-p',password,username])
    except:
        print(f"Failed to add user.")
        sys.exit(1)

if os.path.exists("user.txt"):
    with open ("user.txt") as file:
        for line in file:

             #os.system("echo -e 'Pass@22'\n'Pass@22'|passwd{}").format line())
            add_user(line,'Pass2022')

else:
    print("Erreur: le ichier user.txt est manquanqant!")

