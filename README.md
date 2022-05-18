# Projet 06 du parcours Administrateur Infrastructure & Cloud d'OpenClassrooms


 * Apprenant  AIC OpenClassrooms: Abderrazak ALIF  
 * Date de création : 0/04/2022  
 * Dernière modification : 09/05/2022  
 * Testé sous : Python 3.10.2
 * Projet sous: LICENSE  MIT 
 
## Contexte du projet

Ce projet décrit des scripts python pour automatiser la gestion des comptes utilisateurs, sous Ubuntu 20.04.1 TLS ; sur un site distant, via une connexion sécurisée SSH. Et de partager  le code avec la communauté open source git hub.


## Technologies utilisées 

* VirtualBox Version 6.1.34
* GNS3 2.2.17 
* Configuration réseau  en mode bridge
* 3 desktops Ubuntu 20.04.4 LTS
* 1 desktop admin sous windows 10 entreprise
* IDE : PyCharm 2021.3.2 (Community Edition)


## Contenu du dépôt

* README.md  
* lICENSE.md
* Fichier 001_hosts.csv
* Fichier 001_users.csv
* image topologie.png
* Script config.py
* Script Python :main.py  
* Script check_file.py
* Script read_hosts_csv.py
* Script read_users_csv.py
* Script ssh_creat_users.py
* Script ssh_read_users.py
* Script ssh_del_users.py

## Fonctionnement du programme  main 

Le script main se lance ou se configure  avec deux arguments:
un préfixe  pour manipuler  le jeu de fichiers d'entrée csv  sous la forme  numérique 999.
Et une  lettre **C** ,**R** ou **D** pour exécuter les actions suivantes:

* **C** pour créer les utilisateurs sur les machines  distantes 
* **R** pour lire ou éditer la liste des utilisateurs des machines distantes
* **D** pour supprimer les utilisateurs des machines distantes.

Exemple pour créer les utilisateurs  sous la console windows PowerShell:

PC:\WINDOWS\system32> **_python main.py 001 C_**




  