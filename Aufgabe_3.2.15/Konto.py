

from BankAccount import BankAccount


konto = BankAccount("Unicorn")
print(konto)
konto.zeige_kontostand()
konto.einzahlen(500)
konto.abheben(70)
print(konto)
konto.abheben(600)
konto.zinsen_berechnen(7.2)
konto.zeige_kontostand()
print(konto)
