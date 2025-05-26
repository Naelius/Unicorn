## Rabatt-Rechner
## Wenn der Einkaufswert über 100 € liegt, gibt es 10 % Rabatt. Gib den Endpreis aus.

def rabatt():
    try:
        einskaufpreis = float(input("Bitte dein Einkaufspreis angeben: "))

        if einskaufpreis > 100:
            rabattpreis = einskaufpreis * 0.90
            print(f"Sie erhalten 10% Rabatt. Der Endpreis beträgt: {rabattpreis:.2f} €")
        else:
            print(f"Kein Rabatt. Der Endpreis beträgt: {einskaufpreis:.2f} €")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie einen numerischen Wert für den Einkaufswert ein.")

if __name__ == "__main__":
    rabatt()