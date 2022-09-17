import random


class Terning():
    def __init__(self, verdi, behold):
        self.verdi = verdi
        self.behold = behold

    def behold_terning(self):
        self.behold=True










# Funksjoner:

def terningkast():
    kast = random.randint(1,6)
    return kast



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
for n in range(5):
    print ("Terning",str(n+1),":",terningsett[n].verdi)


