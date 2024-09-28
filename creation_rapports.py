import json
import matplotlib.pyplot as plt 
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        parametre = ["rssi","snr"]
        for i in range(0,2):
            cle1 = parametre[i]
            nom_fichier_image = cle1 + "_timestamp.png"
            canal1 = []
            canal2 = []
            canal3 = []
            abcisse1 = []
            abcisse2 = []
            abcisse3 = []
            date_format = '%Y-%m-%dT%H:%M:%S+00:00'
            for x in range(len(data["donnee"])):
                if(data["donnee"][x].get("freq")==2403000000):
                    canal1.append(data["donnee"][x].get(cle1))
                    date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                    ts = datetime.timestamp(date)
                    abcisse1.append(ts)
                elif(data["donnee"][x].get("freq")==2425000000):
                    canal2.append(data["donnee"][x].get(cle1))
                    date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                    ts = datetime.timestamp(date)
                    abcisse2.append(ts)
                else:    
                    canal3.append(data["donnee"][x].get(cle1))
                    date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                    ts = datetime.timestamp(date)
                    abcisse3.append(ts)
            
            plt.figure(figsize=(120,12))
            plt.title(cle1 + ' en fonction du timestamp')
            plt.ylabel(cle1, fontsize = 12)
            plt.xlabel("timestamp", fontsize = 12)
            plt.scatter(abcisse1, canal1, color = 'black', marker= '.', linewidth = 5)
            plt.scatter(abcisse2, canal2, color = 'red', marker= '.')
            plt.savefig(nom_fichier_image)
            plt.close()
    fichier_entrée.close()

extraction_données("dataset1.json")