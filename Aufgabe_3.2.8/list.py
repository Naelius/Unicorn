
zahlen = [4, 7, 2, 9, 1, 5, 3, 12, 54, 23, 56, 763, 345, 4564, 34536]
print(zahlen[10])

zahlen[10] = 76
print(zahlen[10])

## Einfach

print("Länge der Liste:", len(zahlen))
print("Größte Zahl:", max(zahlen))
print("Kleinste Zahl:", min(zahlen))

## Mittel

durchschnitt = sum(zahlen) / len(zahlen)
print("Durchschnitt:", durchschnitt)

umgekehrt = list(reversed(zahlen))
print("Umgekehrte Liste:", umgekehrt)

## Experte

gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]
print("Gerade Zahlen:", gerade_zahlen)
