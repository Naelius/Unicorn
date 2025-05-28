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

    print("\n" + "="*50)
    print("{:^50}".format("Liste"))
    print("="*50)
    print("{:<25} {:>25}".format("Eingetragene Zahlen", str(zahlen)))
    print("{:<25} {:>25}".format("Größte Zahl", groesste))
    print("{:<25} {:>25}".format("Kleinste Zahl", kleinste))
    print("{:<25} {:>25}".format("Durchschnitt", durchschnitt))
    print("{:<25} {:>25}".format("Sortierte Liste", str(sortiert)))
    print("="*50)
