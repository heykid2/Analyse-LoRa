import json
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        parametre = ["rssi","snr"]
        for i in range(0,2):
            res1_jour = 0
            res2_jour = 0
            res3_jour = 0
            it1_jour = 0
            it2_jour = 0
            it3_jour = 0
            res1_nuit = 0
            res2_nuit = 0
            res3_nuit = 0
            it1_nuit = 0
            it2_nuit = 0
            it3_nuit = 0
            cle1 = parametre[i]
            timestamp_initial = 1642662000 #20 janvier 2022 8h
            date_format = '%Y-%m-%dT%H:%M:%S+00:00'
            for x in range(len(data["donnee"])):
                date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                ts = datetime.timestamp(date)
                if(ts > timestamp_initial+86400):
                    timestamp_initial += 86400
                if(ts - timestamp_initial < 72000 ): #test definissaant selon que la trame ait été recue en journée ou de nuit
                    if(data["donnee"][x].get("freq")==2403000000):
                        res1_jour += data["donnee"][x].get(cle1)
                        it1_jour += 1
                    elif(data["donnee"][x].get("freq")==2425000000):
                        res2_jour += data["donnee"][x].get(cle1)
                        it2_jour += 1
                    else:    
                        res3_jour += data["donnee"][x].get(cle1)
                        it3_jour += 1
                else:    
                    if(data["donnee"][x].get("freq")==2403000000):
                        res1_nuit += data["donnee"][x].get(cle1)
                        it1_nuit += 1
                    elif(data["donnee"][x].get("freq")==2425000000):
                        res2_nuit += data["donnee"][x].get(cle1)
                        it2_nuit += 1
                    else:    
                        res3_nuit += data["donnee"][x].get(cle1)
                        it3_nuit += 1
                    
            print(parametre[i])        
            #print(res1_jour/it1_jour)
            #print(": channel 1 en journée")
            #print(res2_jour/it2_jour)
            #print(": channel 2 en journée")
            print(res3_jour/it3_jour)
            print(": channel 3 en journée")
            
            #print(res1_nuit/it1_nuit)
            #print(": channel 1 la nuit")
            #print(res2_nuit/it2_nuit)
            #print(": channel 2 la nuit")
            print(res3_nuit/it3_nuit)
            print(": channel 3 la nuit")
    fichier_entrée.close()

extraction_données("dataset3.json")