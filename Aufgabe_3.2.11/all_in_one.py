zahlen = []

while True:
    eingabe = input("Gib eine Zahl ein oder 'stop' zum Beenden: ")
    
    if eingabe.lower() == "stop":
        break
    try:
        zahl = int(eingabe)
        zahlen.append(zahl)
    except ValueError:
        print("Fehler: Bitte gib eine gültige ganze Zahl ein!")

if not zahlen:
    print("Keine Zahlen eingegeben.")
else:
    kleinste = zahlen[0]
    groesste = zahlen[0]
    summe = 0

    for zahl in zahlen:
        if zahl < kleinste:
            kleinste = zahl
        if zahl > groesste:
            groesste = zahl
        summe += zahl

    durchschnitt = round(summe / len(zahlen), 2)

    sortiert = sorted(zahlen)

    print("\nListe")
    print("Eingetragene Zahlen", zahlen)
    print("Größte Zahl", groesste)
    print("Kleinste Zahl", kleinste)
    print("Durchschnitt", durchschnitt)
    print("Sortierte Liste", sortiert)
