
""" Test Exisence fichier"""
import csv

def checkFile(file):
    try:
        with open(file, 'r') as f:
            return True

    except FileNotFoundError as e:
        return False

    except IOError as e:
        return False



