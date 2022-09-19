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

# Poengskjema oppsett
enere0 =           Poengfelt("A - Enere:         ", 0 , False )
toere1 =           Poengfelt("B - Toere:         ", 0 , False )
treere2 =          Poengfelt("C - Treere:        ", 0 , False )
firere3 =          Poengfelt("D - Firere:        ", 0 , False )
femere4 =          Poengfelt("E - Femere:        ", 0 , False )
seksere5 =         Poengfelt("F - Seksere:       ", 0 , False )
delestrek6 =       Poengfelt("    ___________________", 0, False)
delsum7 =          Poengfelt("    SUM            ", 0 , False )
bonus8 =           Poengfelt("    Bonus:         ", 0 , False )
ett_par9 =         Poengfelt("G - Ett par:       ", 0 , False )
to_par10 =         Poengfelt("H - To par:        ", 0 , False )
tre_like11=        Poengfelt("I - Tre like:      ", 0 , False )
fire_like12 =      Poengfelt("J - Fire like:     ", 0 , False )                       
liten_straight13 = Poengfelt("K - Liten straight:", 0 , False )
stor_straight14 =  Poengfelt("L - Stor straight: ", 0 , False )
hus15 =            Poengfelt("M - Hus:           ", 0 , False )
sjanse16 =         Poengfelt("N - Sjanse:        ", 0 , False )
yatzy17 =          Poengfelt("Y - YATZY!:        ", 0 , False )
sluttstrek18 =     Poengfelt("    ___________________", 0, False)
sum19 =            Poengfelt("    TOTALT:        ", 0 , False )

# Poengskjema organisering: En Tuple som har 20 elementer (0-19)
poeng_skjema=(enere0, toere1, treere2, firere3, femere4, seksere5, delestrek6, delsum7, bonus8, ett_par9, to_par10, tre_like11, fire_like12, liten_straight13, stor_straight14, hus15, sjanse16, yatzy17, sluttstrek18, sum19)

# En dictionary som knytter rett index-verdi til hver bokstavstreng i poeng_skjema, brukes ved valg til å få rett index for en bokstav valgt
bokstav_nummer_liste = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":9, "H":10, "I":11, "J":12, "K":13, "L":14, "M":15, "N":16, "Y":17 }


# Funksjoner:_________________________________________

# Skriver ut poengskjemaet
def vis_poengskjema(poengskjema):
    print()
    print("POENGSKJEMA: ")
    for n in range (20):
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

# Feilmelding ved opptatt felt
def feil_felt_mld():
    print("Du kan ikke bruke dette feltet, vennligst velg et annet!")
    print()    

# Funksjon som kalles idet antall kast = 15
def avslutt():
    print("Takk for at du spilte, du er ferdig!")
    quit
# ____________________________________Hovedspill______________________________________

print("Yatzy spill!")

antall_kast=0

while True:

    # En kasterunde starter her
    # 1 kast 
    input("Trykk RETURN for å kaste terningene!")

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
    kast_terninger_igjen(terningsett)
    print()
    print("--------------------  Resultat 2. kast: -------------------------")
    velge_terninger()

    # 3 kast 
    kast_terninger_igjen(terningsett)
    print()
    print("--------------------  Resultat 3. kast: -------------------------")
    vis_terningoversikt(terningsett)
    print()
    print()


    # Ferdig med å kaste terninger denne runden ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # Lager en ny liste med bare terningverdier for denne runden
    endelige_verdier = []
    for n in range(5):
        endelige_verdier.append(terningsett[n].verdi)

    # Lager en liste med antallet av hver verdi for denne runden (Arne!) 
    antall_oversikt = []
    for n in range(1, 7):
        antall_oversikt.append(endelige_verdier.count(n))

    antall_kast+=1


    # Valg-løkke for å sette poeng på poengskjema
    while True:
        print()
        print("Du endte opp med følgende terninger:")
        print(endelige_verdier)
        print()
        vis_poengskjema(poeng_skjema) 

        valg=input("Skriv bokstaven der du vil sette denne kasteserien (eller skriv X for å stryke et felt)): ").upper() 
        print()
        
        # Sjekk rett input
        if valg not in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Y", "X"]:
            print("Vennligst velg en gyldig bokstav")
            continue

        # Stryke et felt
        if valg=="X":
            while True:
                strykefelt = input ("Skriv bokstaven til feltet du vil stryke: ").upper()           
                if poeng_skjema[bokstav_nummer_liste[strykefelt]].brukt == False:    
                    poeng_skjema[bokstav_nummer_liste[strykefelt]].brukt=True
                    poeng_skjema[bokstav_nummer_liste[strykefelt]].verdi=0
                    break
                else:
                    feil_felt_mld()
                    continue

        # Sjekk om feltet er brukt allerede
        if valg != "X":
            if poeng_skjema[bokstav_nummer_liste[valg]].brukt == True:
                feil_felt_mld()
                continue   

        # Sette poeng på enkeltterninger 1-6
        if valg in ["A","B","C","D","E","F"]: 
           #  liste = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5 }
            print (f"Du har {antall_oversikt[bokstav_nummer_liste[valg]]} stk {str(bokstav_nummer_liste[valg]+1)}'ere, det blir {(antall_oversikt[bokstav_nummer_liste[valg]]*(bokstav_nummer_liste[valg]+1))} poeng")
            poeng_skjema[bokstav_nummer_liste[valg]].verdi=(antall_oversikt[bokstav_nummer_liste[valg]]*(bokstav_nummer_liste[valg]+1))
            poeng_skjema[bokstav_nummer_liste[valg]].brukt=True

        # Ett par
        if valg == "G": 
            if max(antall_oversikt)>=2:
                parverdi=[]
                for n in range(6):
                    if antall_oversikt[n]>=2:
                        parverdi.append(2*(n+1))
                
                # Det finnes to par i resultatet
                if len(parverdi)==2:                
                    print(f"Du har 2 par.") 
                    print (f"Nr 1: ett par {int(parverdi[0]/2)}'ere, med verdi {int(parverdi[0])} ")
                    print (f"Nr 2: ett par {int(parverdi[1]/2)}'ere, med verdi {int(parverdi[1])} ")
                    
                    while True:
                        parvalg = input("Velg 1 eller 2: ")
                        if parvalg in ["1","2"]:
                            if parvalg == "1":
                                poeng_skjema[9].verdi = parverdi[0]
                                poeng_skjema[9].brukt = True
                                break
                            else:
                                poeng_skjema[9].verdi = parverdi[1]
                                poeng_skjema[9].brukt = True
                                break
                        else:
                            continue

                # Det finnes kun ett par i resultatet
                elif len(parverdi)==1:          
                    print (f"Du har ett par {int(parverdi[0]/2)}'ere, med verdi {int(parverdi[0])} ")
                    poeng_skjema[9].verdi = parverdi[0]
                    poeng_skjema[9].brukt = True

            else:
                feil_felt_mld()
                continue 





        # To par
        if valg == "H":
            if max(antall_oversikt)>=2:
                parverdi=[]
                for n in range(6):
                    if antall_oversikt[n]>=2:
                        parverdi.append(2*(n+1))
                if len(parverdi)==2:
                    print(f"Du har to {parverdi[0]/2}'ere, og to {parverdi[1]/2}'ere, med verdi {parverdi[0]+parverdi[1]} ")
                    poeng_skjema[10].verdi = parverdi[0]+parverdi[1]
                    poeng_skjema[10].brukt = True
                else:
                    feil_felt_mld()
                    continue
            else:
                feil_felt_mld()
                continue
                
        # 3 like
        if valg == "I":
            if max(antall_oversikt) >= 3:
                print (f"Du har {max(antall_oversikt)} stk {antall_oversikt.index(max(antall_oversikt))+1}'ere, det blir {(3*(antall_oversikt.index(max(antall_oversikt))+1))} poeng")
                poeng_skjema[11].verdi=(3*(antall_oversikt.index(max(antall_oversikt))+1))
                poeng_skjema[11].brukt=True
            else:
                feil_felt_mld()
                continue

        # 4 like
        if valg == "J":
            if max(antall_oversikt) >= 4:
                print (f"Du har {max(antall_oversikt)} stk {antall_oversikt.index(max(antall_oversikt))+1}'ere, det blir {(4*(antall_oversikt.index(max(antall_oversikt))+1))} poeng")
                poeng_skjema[12].verdi=(4*(antall_oversikt.index(max(antall_oversikt))+1))
                poeng_skjema[12].brukt=True
            else:
                feil_felt_mld()
                continue

        # Liten Straight
        if valg == "K":
            if max(antall_oversikt)==1 and antall_oversikt[5]==0:
                print(f"Du har fått liten straight, det er 15 poeng.")
                poeng_skjema[13].verdi = 15
                poeng_skjema[13].brukt = True
            else:
                feil_felt_mld()
                continue

        # Stor straight
        if valg == "L":
            if max(antall_oversikt)==1 and antall_oversikt[0]==0:
                print(f"Du har fått stor straight, det er 20 poeng.")
                poeng_skjema[14].verdi = 20
                poeng_skjema[14].brukt = True
            else:
                feil_felt_mld()
                continue

        # Hus
        if valg == "M":
            if 3 in antall_oversikt and 2 in antall_oversikt:
                print(f"Du fikk hus med {sum(endelige_verdier)} poeng.")
                poeng_skjema[15].verdi = sum(endelige_verdier)
                poeng_skjema[15].brukt = True
            else:
                feil_felt_mld()
                continue
        
        # Sjanse
        if valg == "N":
            print(f"Du putter dette på sjanse og får {sum(endelige_verdier)} poeng")
            poeng_skjema[16].verdi = sum(endelige_verdier)
            poeng_skjema[16].brukt = True

        # YATZY!
        if valg == "Y":
            if 5 in antall_oversikt:
                print(f"Gratulerer, du har fått Yatzy! Du har 5 stk {antall_oversikt.index(max(antall_oversikt))+1}ere og får 50 poeng!")
                poeng_skjema[17].verdi = 50
                poeng_skjema[17].brukt = True
            else:
                feil_felt_mld()
                continue
        


        # Beregn poeng så langt _________________________
        # Delsum
        delsum = 0
        for n in range(7):    
            delsum += poeng_skjema[n].verdi
        poeng_skjema[7].verdi = delsum
        poeng_skjema[7].brukt=True
        if delsum > 62:                     # Bonus ved 63 poeng over streken
            poeng_skjema[8].verdi = 50
            poeng_skjema[8].brukt = True
        
        # Totalsum
        totalsum = 0
        for n in range(7,19):
            totalsum += poeng_skjema[n].verdi
        poeng_skjema[19].verdi = totalsum
        poeng_skjema[19].brukt=True


        vis_poengskjema(poeng_skjema)

        if antall_kast==15:
            avslutt()
        
        break


   



