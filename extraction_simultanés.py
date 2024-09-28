import json
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        date_format = '%Y-%m-%dT%H:%M:%S+00:00'
        t0 = datetime.timestamp(datetime.strptime(data["donnee"][0].get("timestamp"), date_format))
        nbr = 0
        for x in range(len(data["donnee"])):
            date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
            t1 = datetime.timestamp(date)
            if (t1 - t0 == 0):
                nbr += 1
            t0 = t1
        print(nbr)
    fichier_entrée.close()
                
extraction_données("dataset3.json")