while True:
    eingabe = input("Windgeschwindigkeit eingeben (oder 'exit' zum Beenden): ")

    if eingabe.lower() == "exit":
        print("Programm beendet.")
        break

    try:
        wind = int(eingabe)

        if wind <= 8:
            status = "Ruhig"
        elif wind >= 8 and wind <= 31:
            status = "Lüftchen"
        elif wind >= 32 and wind <=63:
            status = "Windig"
        else:
            status = "Sturm"

        print(f"Windstatus = {status}")
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl oder 'exit' eingeben.")
