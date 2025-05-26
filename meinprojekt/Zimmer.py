def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl (1,2,3...) ein.")

def zimmer_input():
    print("Bitte geben Sie die Zimmereigenschaften ein:\n")
    zimmer = {}
    zimmer["Zimmernummer"] = input_int("Zimmernummer: ")
    zimmer["Etage"] = input_int("Etage: ")
    zimmer["Fläche (m²)"] = input_int("Fläche in m²: ")
    zimmer["Badewanne"] = input("Badewanne vorhanden? (ja/nein): ")
    zimmer["Balkon"] = input("Hat das Zimmer einen Balkon? (ja/nein): ")
    zimmer["Zimmerart"] = input("Zimmerart (z.B. Schlafzimmer, Küche): ")
    zimmer["Zustand"] = input("Ist das Zimmer frisch gestrichen? (ja/nein): ") 
    zimmer["Wandfarbe"] = input("Farbe der Wand: ")
    zimmer["Küche"] = input("Ist eine Küche bereits eingebaut? (ja/nein): ")
    zimmer["Internet"] = input("Welcher Internetanbieter ist verfügbar? ")
    return zimmer

def zimmer_output(zimmer):
    print("\nZimmerdaten:")
    print("------------")
    for eigenschaft, wert in zimmer.items():
        print(f"{eigenschaft}: {wert}")

## Hauptprogramm
def main():
    zimmer = zimmer_input()
    zimmer_output(zimmer)

if __name__ == "__main__":
    main()
