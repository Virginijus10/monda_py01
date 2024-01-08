""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""
albumas = {
    'atlikejas': "Queen",
    'pavadinimas': "A Kind of Magic",
    'daina': [
        {"pavadinimas": "One Vision", "trukme_min": (5), "trukme_sec": (10)},
        {"pavadinimas": "A Kind of Magic", "trukme_min": (4), "trukme_sec": (46)},
        {"pavadinimas": "One Year of Love", "trukme_min": 3, "trukme_sec": 53},
        {"pavadinimas": "Pain Is So Close to Pleasure", "trukme_min": 3, "trukme_sec": 19},
        {"pavadinimas": "Friends Will Be Friends", "trukme_min": 6, "trukme_sec": 11},
        {"pavadinimas": "Who Wants to Live Forever", "trukme_min": 3, "trukme_sec": 30},
        {"pavadinimas": "Gimme the Prize (Kurgan's Theme)", "trukme_min": 4, "trukme_sec": 16},
        {"pavadinimas": "Don't Lose Your Head", "trukme_min": 5, "trukme_sec": 43},
        {"pavadinimas": "Princes of the Universe", "trukme_min": 4, "trukme_sec": 50},
        {"pavadinimas": "A Kind of 'A Kind of Magic'", "trukme_min": 3, "trukme_sec": 50},
        {"pavadinimas": "Friends Will Be Friends Will Be Friends...", "trukme_min": 5, "trukme_sec": 12},
        {"pavadinimas": "Forever", "trukme_min": 4, "trukme_sec": 46}
    ]
}


def prideti_daina(pavadinimas, trukme):
    trukme_min, trukme_sec = map(int, trukme.split(':'))
    albumas['dainos'].append({
        'pavadinimas': pavadinimas(),
        'trukme_min': trukme_min(),
        'trukme_sec': trukme_sec()
    })

def istrinti_daina(pavadinimas):
    albumas['dainos'] = [daina for daina in albumas['dainos'] if daina['pavadinimas'] != pavadinimas]

def redaguoti_albumo_info(atlikejas=None, pavadinimas=None):
    if atlikejas:
        albumas['atlikejas'] = atlikejas
    if pavadinimas:
        albumas['pavadinimas'] = pavadinimas

def perziureti_albuma():
    print(f"Albumas: {albumas['pavadinimas']} ({albumas['atlikejas']})")
    print(f"Dainų kiekis: {len(albumas['daina'])}")
    trukme_minutemis = sum(daina['trukme_min'] for daina in albumas['daina'])
    trukme_sekundemis = sum(daina['trukme_sec'] for daina in albumas['daina'])
    trukme_minutemis += trukme_sekundemis // 60
    trukme_sekundemis %= 60
    

def dainu_sarasas():
    print("Dainos:")
    for daina in albumas['daina']:
        trukme_minutemis = daina['trukme_min']
        trukme_sekundemis = daina['trukme_sec']
        print(f"{daina['pavadinimas']:<50} {trukme_minutemis}:{trukme_sekundemis}")


# Funkcija, leidžianti vartotojui pasirinkti, ką jis nori daryti su albumu
def meniu():
    while True:
        print("\nAlbumo veiksmai:")
        print("1. Pridėti naują dainą")
        print("2. Ištrinti dainą")
        print("3. Redaguoti albumo informaciją")
        print("4. Peržiūrėti albumą")
        print("5. Peržiūrėti albumo dainas")
        print("6. Baigti")

        pasirinkimas = input("Pasirinkite veiksmą: ")

        if pasirinkimas == '1':
            pavadinimas = input("Įveskite dainos pavadinimą: ")
            trukme = input("Įveskite dainos trukmę minutės:sekundės formatu (pvz., 5:32): ")
            prideti_daina(pavadinimas, trukme)
        elif pasirinkimas == '2':
            pavadinimas = input("Įveskite dainos pavadinimą, kurią norite ištrinti: ")
            istrinti_daina(pavadinimas)
        elif pasirinkimas == ("4"):   
            perziureti_albuma()
        elif pasirinkimas == ("5"):
            dainu_sarasas()
        # Kitos funkcijos
        elif pasirinkimas == '6':
            break
        else:
            print("Netinkamas pasirinkimas, bandykite dar kartą")

# Paleiskime meniu
meniu()
