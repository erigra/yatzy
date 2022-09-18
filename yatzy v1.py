import random

# Klassedefinisjoner
class Terning():
    def __init__(self, verdi, behold):
        self.verdi = verdi
        self.behold = behold

    def behold_terning(self):
        self.behold=True

# Funksjoner:

# Skriver ut en liste med terningverdiene og om terningen er valgt å beholde
def vis_terningoversikt(terningliste):
    for n in range(5):
        if terningliste[n].behold==False:           
            print ("Terning",str(n+1),":",terningliste[n].verdi)                                
        else:
            print ("Terning",str(n+1),":",terningliste[n].verdi," - beholdt!") 


# Lar spilleren velge hvilke terninger som skal beholdes
def velge_terninger():
    while True:
        vis_terningoversikt(terningsett)

        valgt_terning=input ("Skriv tallet til en terning du vil beholde, eller 0 for å avslutte valg av terninger: ")

        if valgt_terning not in ["0","1","2","3","4","5"]:
            print("Feil input! Prøv igjen...")
            continue
        elif valgt_terning == "0":
            break
        else:
            if terningsett[int(valgt_terning)-1].behold==False:
                terningsett[int(valgt_terning)-1].behold=True
                 # print("Du har valgt å beholde terning",valgt_terning,"med verdi:",terningsett[int(valgt_terning)-1].verdi)
            else:
                # print("Du har valgt å kaste på nytt terning",valgt_terning,"med verdi:",terningsett[int(valgt_terning)-1].verdi)
                terningsett[int(valgt_terning)-1].behold=False

# Kaster på nytt ikke beholdte terninger
def kast_terninger_igjen(terningsett):
    for n in range(5):
        if terningsett[n].behold==False:
            terningsett[n].verdi=random.randint(1,6)

# ____________________________________Hovedspill______________________________________

print("Yatzy spill!")

# 1 kast ----------------------------------------
input("Trykk RETURN for å kaste ditt første kast")
antall_kast=1

t0 = Terning(random.randint(1,6), False)
t1 = Terning(random.randint(1,6), False)
t2 = Terning(random.randint(1,6), False)
t3 = Terning(random.randint(1,6), False)
t4 = Terning(random.randint(1,6), False)

terningsett= [t0,t1,t2,t3,t4]

print()
print("------------------------- Resultat 1. kast: -----------------------------------")
velge_terninger()


# 2 kast ---------------------------------------
antall_kast=2
kast_terninger_igjen(terningsett)

print()
print("--------------------  Resultat 2. kast: -------------------------")

velge_terninger()

# 3 kast ---------------------------------------

antall_kast=3
kast_terninger_igjen(terningsett)

print()
print("--------------------  Resultat 3. kast: -------------------------")
vis_terningoversikt(terningsett)


# Ferdig med å kaste terninger -------------------------------------------------------

# Lager en ny liste med bare terningverdier
endelige_verdier = []
for n in range(5):
    endelige_verdier.append(terningsett[n].verdi)

# Lager en liste med antallet av hver verdi  
antall_oversikt = []
for n in range(1, 7):
    antall_oversikt.append(endelige_verdier.count(n))

print(antall_oversikt)

