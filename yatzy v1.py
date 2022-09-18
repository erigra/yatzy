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


enere0 = Poengfelt("A - Enere:     ", 0 , False )
toere1 = Poengfelt("B - Toere:     ", 0 , False )
treere2 = Poengfelt("C - Treere:   ", 0 , False )
firere3 = Poengfelt("D - Firere:    ", 0 , False )
femere4 = Poengfelt("E - Femere:    ", 0 , False )
seksere5 = Poengfelt("F - Seksere:   ", 0 , False )
delestrek6 = Poengfelt ("_______________________________", 0, False)
delsum7 = Poengfelt("Delsum     ", 0 , False )
bonus8 = Poengfelt("Bonus:     ", 0 , False )
ett_par9 = Poengfelt("G - Ett par:   ", 0 , False )
to_par10 = Poengfelt("H - To par:    ", 0 , False )
tre_like11= Poengfelt("I - Tre like:  ", 0 , False )
fire_like12 = Poengfelt("J - Fire like: ", 0 , False )
hus13 = Poengfelt("K - Hus:       ", 0 , False )
straight14 = Poengfelt("L - Straight:  ", 0 , False )
yatzy15 = Poengfelt("M - Yatzy!:    ", 0 , False )
sjanse16 = Poengfelt("N - Sjanse     ", 0 , False )
sluttstrek17 = Poengfelt ("_______________________________", 0, False)
sum18 = Poengfelt("Sum:        ", 0 , False )

# En Tuple som har 19 elementer (0-18)
poeng_skjema=(enere0, toere1, treere2, firere3, femere4, seksere5, delestrek6, delsum7, bonus8, ett_par9, to_par10, tre_like11, fire_like12, hus13, straight14, yatzy15, sjanse16, sluttstrek17, sum18)


# Funksjoner:

# Skriver ut poengskjemaet
def vis_poengskjema(poengskjema):
    print()
    print("POENGSKJEMA: ")
    for n in range (19):
        if poengskjema[n].brukt==False:
            print(poengskjema[n].navn)
        else:    
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

    

# ____________________________________Hovedspill______________________________________

print("Yatzy spill!")


while True:

    # En kasterunde starter her
    # 1 kast 
    input("Trykk RETURN for å kaste ditt første kast!")
    antall_kast = 1

    # Setter opp/kaster nye terninger for denne runden som første kast
    t0 = Terning(random.randint(1,6), False)
    t1 = Terning(random.randint(1,6), False)
    t2 = Terning(random.randint(1,6), False)
    t3 = Terning(random.randint(1,6), False)
    t4 = Terning(random.randint(1,6), False)
    terningsett = [t0,t1,t2,t3,t4]

    print()
    print("------------------------- Resultat 1. kast: -----------------------------------")
    velge_terninger()


    # 2 kast
    antall_kast=2
    kast_terninger_igjen(terningsett)
    print()
    print("--------------------  Resultat 2. kast: -------------------------")
    velge_terninger()


    # 3 kast 
    antall_kast=3
    kast_terninger_igjen(terningsett)
    print()
    print("--------------------  Resultat 3. kast: -------------------------")
    vis_terningoversikt(terningsett)


    # Ferdig med å kaste terninger denne runden ::::::::::::::::::::

    # Lager en ny liste med bare terningverdier for denne runden
    endelige_verdier = []
    for n in range(5):
        endelige_verdier.append(terningsett[n].verdi)

    # Lager en liste med antallet av hver verdi for denne runden  
    antall_oversikt = []
    for n in range(1, 7):
        antall_oversikt.append(endelige_verdier.count(n))

    print(endelige_verdier)
    vis_poengskjema(poeng_skjema) 

    valg=input("Skriv bokstaven foran der du vil putte denne kasteserien (eksempel H for To par): ").upper() 
    print()
    print()

    # Sette poeng på enkeltterninger 1-6
    if valg in ["A","B","C","D","E","F"]: 
        liste = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5 }
        print (f"Du har {antall_oversikt[liste[valg]]} stk {str(liste[valg]+1)}'ere, det blir {(antall_oversikt[liste[valg]]*(liste[valg]+1))} poeng")
        poeng_skjema[liste[valg]].verdi=(antall_oversikt[liste[valg]]*(liste[valg]+1))
        poeng_skjema[liste[valg]].brukt=True

    # Ett par
    if valg == "G":
        pass

    # To par
    if valg == "G":
        pass

    # 3 like
    if valg == "I":
        if max(antall_oversikt) >= 3:
            print (f"Du har {max(antall_oversikt)} stk {antall_oversikt.index(max(antall_oversikt))+1}'ere, det blir {(3*(antall_oversikt.index(max(antall_oversikt))+1))} poeng")
            poeng_skjema[11].verdi=(3*(antall_oversikt.index(max(antall_oversikt))+1))
            poeng_skjema[11].brukt=True

    # 4 like
    if valg == "J":
        if max(antall_oversikt) >= 4:
            print (f"Du har {max(antall_oversikt)} stk {antall_oversikt.index(max(antall_oversikt))+1}'ere, det blir {(4*(antall_oversikt.index(max(antall_oversikt))+1))} poeng")
            poeng_skjema[12].verdi=(4*(antall_oversikt.index(max(antall_oversikt))+1))
            poeng_skjema[12].brukt=True



    # Summer poeng så langt
    # Delsum
    for n in range(7):
        delsum = 0
        delsum += poeng_skjema[n].verdi
    poeng_skjema[7].verdi = delsum
    
    # Totalsum
    for n in range(7,18):
        totalsum = 0
        totalsum += poeng_skjema[n].verdi
    poeng_skjema[18].verdi = totalsum


    vis_poengskjema(poeng_skjema)


   



