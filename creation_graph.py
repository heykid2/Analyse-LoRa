import json
import matplotlib.pyplot as plt 
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        parametre = ["rssi","snr","volt", "test", "freq", "length", "preamble", "cr", "sf"]
        for i in range(0,9):
            cle1 = parametre[i]
            for j in range(0,9):
                if i != j:
                    entier = 1
                    cle2 = parametre[j]
                else:
                    entier = 0
                    cle2 = "timestamp"
                nom_fichier_image = cle1 + "_" + cle2 + ".png"
                ordonee = []
                abcisse = []
                for x in range(len(data["donnee"])):
                    ordonee.append(data["donnee"][x].get(cle1))
                    if entier == 0:
                        date_format = '%Y-%m-%dT%H:%M:%S+00:00'
                        date = datetime.strptime(data["donnee"][x].get(cle2), date_format)
                        ts = datetime.timestamp(date)
                        abcisse.append(ts)
                    else:
                        abcisse.append(data["donnee"][x].get(cle2))
                plt.figure(figsize=(120,12))
                plt.title(cle1 + ' en fonction du ' + cle2)
                plt.ylabel(cle1, fontsize = 12)
                plt.xlabel(cle2, fontsize = 12)
                plt.plot(abcisse, ordonee, color = 'blue', marker= '.', linestyle = 'solid', linewidth = 1, markersize = 2)
                plt.savefig(nom_fichier_image)
                plt.close()
    fichier_entrée.close()

extraction_données("test.json")