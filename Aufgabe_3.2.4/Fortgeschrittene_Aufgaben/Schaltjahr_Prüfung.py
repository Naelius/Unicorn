## Schaltjahr-Prüfung
## Frage nach einem Jahr und gib aus, ob es ein Schaltjahr ist (Regel: durch 4 teilbar, aber nicht durch 100, außer es ist durch 400 teilbar).

def schaltjahr():
    try:
        jahr = int(input("Bitte geben Sie eine Jahreszahl ein: "))

        if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
            print(f"Das Jahr {jahr} ist ein Schaltjahr.")
        else:
            print(f"Das Jahr {jahr} ist kein Schaltjahr.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl für das Jahr ein.")

if __name__ == "__main__":
    schaltjahr()