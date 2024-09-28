import json
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        parametre = ["rssi","snr"]
        for i in range(0,2):
            res1_semaine = 0
            res2_semaine = 0
            res3_semaine = 0
            it1_semaine = 0
            it2_semaine = 0
            it3_semaine = 0
            res1_weekend = 0
            res2_weekend = 0
            res3_weekend = 0
            it1_weekend = 0
            it2_weekend = 0
            it3_weekend = 0
            cle1 = parametre[i]
            timestamp_initial = 1642806000 #20 janvier 2022 8h
            date_format = '%Y-%m-%dT%H:%M:%S+00:00'
            for x in range(len(data["donnee"])):
                date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                ts = datetime.timestamp(date)
                if(ts > timestamp_initial+604800):
                    timestamp_initial += 604800
                if(ts - timestamp_initial < 172800 ): #test definissaant selon que la trame ait été recue en journée ou de nuit
                    if(data["donnee"][x].get("freq")==2403000000):
                        res1_semaine += data["donnee"][x].get(cle1)
                        it1_semaine += 1
                    elif(data["donnee"][x].get("freq")==2425000000):
                        res2_semaine += data["donnee"][x].get(cle1)
                        it2_semaine += 1
                    else:    
                        res3_semaine += data["donnee"][x].get(cle1)
                        it3_semaine += 1
                else:    
                    if(data["donnee"][x].get("freq")==2403000000):
                        res1_weekend += data["donnee"][x].get(cle1)
                        it1_weekend += 1
                    elif(data["donnee"][x].get("freq")==2425000000):
                        res2_weekend += data["donnee"][x].get(cle1)
                        it2_weekend += 1
                    else:    
                        res3_weekend += data["donnee"][x].get(cle1)
                        it3_weekend += 1
                    
            print(parametre[i])        
            #print(res1_semaine/it1_semaine)
            #print(": channel 1 en semaine")
            #print(res2_semaine/it2_semaine)
            #print(": channel 2 en semaine")
            print(res3_semaine/it3_semaine)
            print(": channel 3 en semaine")
            
            #print(res1_weekend/it1_weekend)
            #print(": channel 1 le weekend")
            #print(res2_weekend/it2_weekend)
            #print(": channel 2 le weekend")
            print(res3_weekend/it3_weekend)
            print(": channel 3 le weekend")
    fichier_entrée.close()
                
extraction_données("dataset3.json")