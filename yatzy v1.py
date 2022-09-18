import random

# Klassedefinisjoner
class Terning():
    def __init__(self, verdi, behold):
        self.verdi = verdi
        self.behold = behold

class Poengfelt():
    def __init__(self, navn, verdi, brukt):
        self.navn = navn
        self.verdi = verdi
        self.brukt = brukt


enere = Poengfelt("Enere:    ", 0 , False )
toere = Poengfelt("Toere:    ", 0 , False )
treere = Poengfelt("Treere:   ", 0 , False )
firere = Poengfelt("Firere:   ", 0 , False )
femere = Poengfelt("Femere:   ", 0 , False )
seksere = Poengfelt("Seksere:  ", 0 , False )
delestrek = Poengfelt ("_______________________________", 0, True)
delsum = Poengfelt("Delsum    ", 0 , False )
bonus = Poengfelt("Bonus:    ", 0 , False )
ett_par = Poengfelt("Ett par:  ", 0 , False )
to_par = Poengfelt("To par:   ", 0 , False )
tre_like= Poengfelt("Tre like: ", 0 , False )
fire_like = Poengfelt("Fire like:", 0 , False )
hus = Poengfelt("Hus:      ", 0 , False )
straight = Poengfelt("Straight: ", 0 , False )
yatzy = Poengfelt("Yatzy!:   ", 0 , False )
sjanse = Poengfelt("Sjanse    ", 0 , False )
sluttstrek = Poengfelt ("_______________________________", 0, True)
sum = Poengfelt("Sum:       ", 0 , False )

# En Tuple som har 19 elementer (0-18)
poeng_skjema=(enere, toere, treere, firere, femere, seksere, delestrek, delsum, bonus, ett_par, to_par, tre_like, fire_like, hus, straight, yatzy, sjanse, sluttstrek, sum)


# Funksjoner:

# Skriver ut poengskjemaet
def vis_poengskjema(poengskjema):
    print("POENGSKJEMA: ")
    for n in range (19):
        print(poengskjema[n].navn,poengskjema[n].verdi)


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

#::::::::::::::::::::::::::::::::::::::::::::::::::::: TESTING, TESTING :::::::::::::::::::::::::::::


vis_poengskjema(poeng_skjema)





# ____________________________________Hovedspill______________________________________

print("Yatzy spill!")

# 1 kast ----------------------------------------
input("Trykk RETURN for å kaste ditt første kast!")
antall_kast = 1

t0 = Terning(random.randint(1,6), False)
t1 = Terning(random.randint(1,6), False)
t2 = Terning(random.randint(1,6), False)
t3 = Terning(random.randint(1,6), False)
t4 = Terning(random.randint(1,6), False)

terningsett = [t0,t1,t2,t3,t4]

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



