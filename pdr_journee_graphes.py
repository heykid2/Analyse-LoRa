import json
from datetime import datetime
from statistics import fmean, pstdev
import matplotlib.pyplot as plt 
import numpy as np

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        date_format = '%Y-%m-%dT%H:%M:%S+00:00'
        t0 = 1678834800 #dataset3
        #t0 = 1642683337 #dataset1
        #t0 = 1648130677 #dataset2
        fcount_tmp = data["donnee"][0].get("fcount")
        res = []
        nbr_trames_test = 0
        moyenne = 0
        ecart_type_haut = 0
        ecart_type_bas = 0
        tab_moyenne = []
        tab_ecart_type_haut = []
        tab_ecart_type_bas = []
        abcisse = 0
        for x in range(len(data["donnee"])):
            date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
            t2 = datetime.timestamp(date)
            fcount_tmp = data["donnee"][x-1].get("fcount")
            if (fcount_tmp == data["donnee"][x].get("fcount")):
                nbr_trames_test += 1
            else:
                res.append(nbr_trames_test/6)
                nbr_trames_test = 0
            if (t2 - t0 > 86400):
                abcisse += 1
                moyenne = fmean(res)
                ecart_type = pstdev(res)
                ecart_type_haut = moyenne + ecart_type
                ecart_type_bas = moyenne - ecart_type
                tab_moyenne.append(moyenne)
                tab_ecart_type_haut.append(ecart_type_haut)
                tab_ecart_type_bas.append(ecart_type_bas)
                res = []
                moyenne = 0
                ecart_type = 0
                t0 = t2
        test = np.linspace(1, abcisse, abcisse)
        plt.figure(figsize=(120,12))
        plt.ylabel("pdr", fontsize = 12)
        plt.xlabel("date", fontsize = 12)
        plt.plot(test, tab_moyenne, color = 'black', marker= '.', linewidth = 5)
        plt.plot(test, tab_ecart_type_haut, color = 'blue', marker= '.', linewidth = 5)
        plt.plot(test, tab_ecart_type_bas, color = 'blue', marker= '.', linewidth = 5)
        plt.savefig("test")
        plt.close()     
    fichier_entrée.close()
                
extraction_données("dataset3.json")