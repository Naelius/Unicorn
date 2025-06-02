

from BankAccount import BankAccount
from zinsen import zinsen_berechnen


konto = BankAccount("Unicorn")
print(konto)
konto.zeige_kontostand()
konto.einzahlen(500)
konto.abheben(70)
print(konto)
konto.abheben(600)
zinsen_berechnen(konto, 7.2)
konto.zeige_kontostand()
print(konto)
