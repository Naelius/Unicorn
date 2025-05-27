## Aufgabenstellung:
## Schreibe ein Python-Programm, das mithilfe einer for-Schleife alle geraden Zahlen von 1 bis 100 summiert und das Ergebnis ausgibt.

summe = 0

for zahl in range(1, 101):
    if zahl % 2 == 0:
        summe += zahl

print("Die Summe aller geraden Zahlen von 1 bis 100 beträgt:", summe)
