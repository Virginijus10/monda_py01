""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""

pelno_nuostolio_ataskaita = []

def prideti_pajamas(suma):
    if suma > 0:
        pelno_nuostolio_ataskaita.append(('Pajamos', suma))
        print(f"Pajamos pridėtos: +{suma}")
    else:
        print("Netinkama suma pajamoms")

def atimti_islaidas(atimti):
    if atimti > 0:
        pelno_nuostolio_ataskaita.append(('Išlaidos', -atimti))
        print(f"Išlaidos atimtos: -{atimti}")
    else:
        print("Netinkama suma išlaidoms")

while True:
    veiksmas = input("Norite pridėti pajamas (p) ar išlaidas (i)? Arba norite atimti išlaidas (a)? Arba spausdinti žurnalą (s)? Arba baigti (q)? ").lower()

    if veiksmas == 'p':
        suma = float(input("Įveskite sumą pajamoms: "))
        prideti_pajamas(suma)
    elif veiksmas == 'i':
        islaidos = float(input("Įveskite sumą išlaidoms: "))
        atimti_islaidas(islaidos)
    elif veiksmas == 's':
        pinigu_likutis = suma - islaidos
        print(pinigu_likutis)
    
        break
    else:
        print("Netinkamas pasirinkimas, bandykite dar kartą")




