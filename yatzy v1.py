import random


class Terning():
    def __init__(self, verdi, behold):
        self.verdi = verdi
        self.behold = behold

    def behold_terning(self):
        self.behold=True






t1 = Terning(random.randint(1,6), False)
t2 = Terning(random.randint(1,6), False)
t3 = Terning(random.randint(1,6), False)
t4 = Terning(random.randint(1,6), False)
t5 = Terning(random.randint(1,6), False)
t6 = Terning(random.randint(1,6), False)


terningsett_verdi = [t1.verdi,t2.verdi,t3.verdi,t4.verdi,t5.verdi]
terningsett_behold = [t1.behold,t2.behold,t3.behold,t4.behold,t5.behold]


# Funksjoner:

def terningkast():
    kast = random.randint(1,6)
    return kast



# ____________________________________Hovedspill______________________________________

print("Yatzy spill!")

input("Trykk RETURN for å kaste ditt første kast")

print (terningsett_verdi)
print (terningsett_behold)

t1.behold=True

print (terningsett_behold)
print (t1.verdi)
print (t1.behold)