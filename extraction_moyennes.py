import json

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        parametre = ["rssi","snr"]
        for i in range(0,2):
            res1 = 0
            res2 = 0
            res3 = 0
            it1 = 0
            it2 = 0
            it3 = 0
            cle1 = parametre[i]
            for x in range(len(data["donnee"])):
                if(data["donnee"][x].get("freq")==2403000000):
                    res1 += data["donnee"][x].get(cle1)
                    it1 += 1
                elif(data["donnee"][x].get("freq")==2425000000):
                    res2 += data["donnee"][x].get(cle1)
                    it2 += 1
                else:    
                    res3 += data["donnee"][x].get(cle1)
                    it3 += 1
            print(res1/it1)
            print(res2/it2)
            print(res3/it3)
    fichier_entrée.close()
                
extraction_données("dataset2.json")