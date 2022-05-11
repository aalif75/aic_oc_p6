# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Abderrazak ALIF
# Created Date: 04/05/2022
# version ='1.0'
# -----------------------------------------------------------


import sys
import read_hosts_csv as rhc   # import module lecteur  fichier csv machines
import read_users_csv as ruc   # import module lecteur  fichier csv utilisateurs
import check_file as cf        # import module test existence fichies data
import config as cfg           # chargement  module config compte sysadmin
import ssh_creat_users as scu  # import mudule fonction creation des utiisateurs
import ssh_del_users as sdu    # import mudule fonction suppression  des utiisateurs
import ssh_read_users as sru   # import mudule fonction édition  des utiisateurs

# arguments du script  prefixe fichiers csv d"entrées  et type action  à exécuter (CRUD) (sans Update)
if len(sys.argv) != 3:
    print("usage : "+sys.argv[0]+" <jeu> <action>")
    exit(0)

hostfile = sys.argv[1] + "_hosts.csv"
userfile = sys.argv[1] + "_users.csv"
action = sys.argv[2]

print("Fichier des machines: "+hostfile)
print("Fichier des utilisateurs: "+userfile)

# Appel  module checkFile userfile
if not cf.checkFile(userfile):
    print("le fichier: " + userfile + " n'existe pas:")
    exit(1)

# Appel  module checkFile hostfile
if not cf.checkFile(hostfile):
    print("le fichier n'existe pas:" + hostfile)
    print("le fichier: " + hostfile + " n'existe pas:")
    exit(1)


if (action not in ['C','D','R']):  # negation
    print("action non reconnue")
    exit(1)

#  recuperation des listes machines et des logins utlisateurs
machines = rhc.read_hosts_csv(hostfile)  # appel foncton lecteur csv machines (hostfile)
logins = ruc.read_users_csv(userfile)    # appel module  lecteurs _csv  users"""

result = []  # initalisation de la variable result

if action == "C":
    print("Creation des utilisateurs:\n")
    result = scu.ssh_creat_users(logins, machines, cfg.adminLogin, cfg.adminPwd)
elif action == "D":
    print("Suppression des utilisateurs: \n")
    result = sdu.ssh_del_users(logins, machines, cfg.adminLogin, cfg.adminPwd)
elif action == "R":
    print("Edition listes des utilisateurs: \n")
    result = sru.ssh_read_users(machines, cfg.adminLogin, cfg.adminPwd)
else:
    result.append("action : " + action + " non reconnue")

""" Affichage resultat  action"""
for line in result:
    print(line)
    print()

exit(0)



