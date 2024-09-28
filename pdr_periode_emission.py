import json
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        with open("pdr.txt", 'x') as sortie:
            data = json.load(fichier_entrée)
            date_format = '%Y-%m-%dT%H:%M:%S+00:00'
            t0 = datetime.timestamp(datetime.strptime(data["donnee"][0].get("timestamp"), date_format))
            y = 0
            t1 = t0
            nbr_trames = 0
            fcount = 0
            res=0
            for x in range(len(data["donnee"])):
                fcount = data["donnee"][y].get("fcount")
                date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                t2 = datetime.timestamp(date)
                if (t2 - t1 > 3600):
                    sortie.write("début d'émission " + data["donnee"][y].get("timestamp") + " jusqu'à " + data["donnee"][x-1].get("timestamp") + '\n')
                    fcount = (data["donnee"][x-1].get("fcount") - data["donnee"][y].get("fcount"))*9
                    t0 = t1
                    y = x
                    res = nbr_trames/fcount
                    sortie.write("pdr de cette journée " + str(res) + '\n')
                    nbr_trames = 0
                nbr_trames +=1
                t1 = t2    
        sortie.close()        
    fichier_entrée.close()
                
extraction_données("dataset3.json")