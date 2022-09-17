import random

# ANSII escape codes for farger på valgte terninger i lista
#  Grønn      \033[1;32;40m Bright Green  \n 
#  Reset(?)    \033[0m \n

class Terning():
    def __init__(self, verdi, behold):
        self.verdi = verdi
        self.behold = behold

    def behold_terning(self):
        self.behold=True

# Funksjoner:
def vis_terningoversikt(terningliste):
    for n in range(5):
        if terningliste[n].behold==False:
            
            print ("Terning",str(n+1),":",terningliste[n].verdi)                                
        else:
            # Skriver i grønn skrift dersom valgt å beholde (og så settes hvit farge igjen)
            print ("Terning",str(n+1),":",terningliste[n].verdi," - beholdt!")    


# ____________________________________Hovedspill______________________________________

print("Yatzy spill!")
input("Trykk RETURN for å kaste ditt første kast")

antall_kast=1

t0 = Terning(random.randint(1,6), False)
t1 = Terning(random.randint(1,6), False)
t2 = Terning(random.randint(1,6), False)
t3 = Terning(random.randint(1,6), False)
t4 = Terning(random.randint(1,6), False)

terningsett= [t0,t1,t2,t3,t4]

print("Resultat 1. kast:")
# for n in range(5):
#    print ("Terning",str(n+1),":",terningsett[n].verdi)

behold_terninger = []

while True:

    vis_terningoversikt(terningsett)

    valgt_terning=input ("Skriv tallet til en terning du vil beholde, eller 0 for å avslutte valg av terninger: ")

    if valgt_terning not in ["0","1","2","3","4","5"]:
        print("Feil input! Prøv igjen...")
        continue
    elif valgt_terning == "0":
        break
    else:
        terningsett[int(valgt_terning)-1].behold=True
        print("Du har valgt å beholde terning",valgt_terning,"med verdi:",terningsett[int(valgt_terning)-1].verdi)

