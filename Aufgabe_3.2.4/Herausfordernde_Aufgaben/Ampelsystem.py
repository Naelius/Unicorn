## Ampelsystem
## Lies eine Farbe ein (rot, gelb, grün) und gib aus, was man machen soll (z. B. "stehen bleiben", "bereit machen", "gehen").

def ampelsystem():
    farbe = input("Eine Ampelfarbe eingeben (rot, gelb, grün): ").lower()

    if farbe == "rot":
        print("Stehen bleiben")
    elif farbe == "gelb":
        print("Bereit machen")
    elif farbe == "grün":
        print("Gehen")
    else:
        print("Ungültige Farbe. Grün, Gelb oder Rot eingeben")

if __name__ == "__main__":
    ampelsystem()