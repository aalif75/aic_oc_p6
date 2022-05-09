liste_donnees = []  # initialisation de la liste

def read_users_csv(csvFilePath):


	with open(csvFilePath, 'r') as f:
		descripteurs = f.readline()
		descripteurs = descripteurs[:-1].split(';')  # transformation descripteurs  en  liste sans "\n" pour traiter les champs
		lignes = f.read().splitlines()   # lecture des autes lignes

		for ligne in lignes:
			# recuperation des champs separes par un virgule
			champs = ligne.split(";")

			d = {}  # creation dico vide
			for i in range(len(descripteurs)):  # Mise en dico des enreg d'une ligne
				d[descripteurs[i]] = champs[i]
			liste_donnees.append(d)

	# print("les données sous format dico :"); print(liste_donnees, '\n')  # verification des données
	logins = []

	for i in liste_donnees:  # parcourt dico liste_donneés  pour extraire les logins
		login = i['login']
		logins.append(login)

	return logins

















	


