## Notenbewertung
## Lies eine Zahl zwischen 1 und 6 ein und gib die entsprechende Schulnote aus (z. B. 1 = sehr gut, 6 = ungenügend).

def noten():
    try:
        note_input = int(input("Bitte eine Schulnote (1-6) eingeben: "))

        if note_input == 1:
            print("Sehr gut")
        elif note_input == 2:
            print("Gut")
        elif note_input == 3:
            print("Befriedigend")
        elif note_input == 4:
            print("Ausreichend")
        elif note_input == 5:
            print("Mangelhaft")
        elif note_input == 6:
            print("Ungenügend")
        else:
            print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 6 eingeben")
    except ValueError:
        print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben")

if __name__ == "__main__":
    noten()