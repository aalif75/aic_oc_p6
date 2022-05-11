def read_hosts_csv(csvFilePath):
	liste_donnees = []
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

	hosts = []
	for i in liste_donnees:  # parcourt dico liste_donneés  pour extraire les IP des machines
		ip = i['ip']
		hosts.append(ip)
	return hosts




















	


