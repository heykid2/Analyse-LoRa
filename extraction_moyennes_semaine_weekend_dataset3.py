import json
from datetime import datetime

def extraction_données(nom_fichier_entrée):
    with open(nom_fichier_entrée, "r") as fichier_entrée:
        data = json.load(fichier_entrée)
        parametre = ["rssi","snr"]
        for i in range(0,2):
            res10_jour = 0
            it10_jour = 0
            res10_nuit = 0
            it10_nuit = 0
            res11_jour = 0
            it11_jour = 0
            res11_nuit = 0
            it11_nuit = 0
            res12_jour = 0
            it12_jour = 0
            res12_nuit = 0
            it12_nuit = 0
            cle1 = parametre[i]
            timestamp_initial = 1642806000 #20 janvier 2022 8h
            date_format = '%Y-%m-%dT%H:%M:%S+00:00'
            for x in range(len(data["donnee"])):
                date = datetime.strptime(data["donnee"][x].get("timestamp"), date_format)
                ts = datetime.timestamp(date)
                if(ts > timestamp_initial+604800):
                    timestamp_initial += 604800
                if(ts - timestamp_initial < 172800 ): #test definissaant selon que la trame ait été recue en journée ou de nuit
                    if(data["donnee"][x].get("sf")==10):
                        res10_jour += data["donnee"][x].get(cle1)
                        it10_jour += 1
                    elif(data["donnee"][x].get("sf")==11):
                        res11_jour += data["donnee"][x].get(cle1)
                        it11_jour += 1
                    else:    
                        res12_jour += data["donnee"][x].get(cle1)
                        it12_jour += 1
                else:    
                    if(data["donnee"][x].get("sf")==10):
                        res10_nuit += data["donnee"][x].get(cle1)
                        it10_nuit += 1
                    elif(data["donnee"][x].get("sf")==11):
                        res11_nuit += data["donnee"][x].get(cle1)
                        it11_nuit += 1
                    else:    
                        res12_nuit += data["donnee"][x].get(cle1)
                        it12_nuit += 1
                    
            print(parametre[i])        
            print(res10_jour/it10_jour)
            print(": sf 10 en semaine")
            print(res10_nuit/it10_nuit)
            print(": sf 10 le Weekend")
            print(res11_jour/it11_jour)
            print(": sf 11 en semaine")
            print(res11_nuit/it11_nuit)
            print(": sf 11 la Weekend")
            print(res12_jour/it12_jour)
            print(": sf 12 en semaine")
            print(res12_nuit/it12_nuit)
            print(": sf 12 la Weekend")
    fichier_entrée.close()

extraction_données("dataset3.json")