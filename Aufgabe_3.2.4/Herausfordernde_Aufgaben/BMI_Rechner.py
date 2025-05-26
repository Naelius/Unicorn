## BMI-Rechner mit Bewertung
## Lies Gewicht und Größe ein, berechne den BMI und gib aus, ob die Person untergewichtig, normalgewichtig oder übergewichtig ist.

def bmirechner():
    try:
        weight = float(input("Bitte geben Sie Ihr Gewicht in Kilogramm ein: "))
        height = float(input("Bitte geben Sie Ihre Größe in Metern ein (z.B. 1.75): "))

        if weight <= 0 or height <= 0:
            print("Gewicht und Größe müssen positive Werte sein.")
            return

        bmi = weight / (height ** 2)

        print(f"Ihr BMI beträgt: {bmi:.2f}")

        if bmi < 18.5:
            print("Sie sind untergewichtig.")
        elif 18.5 <= bmi < 25:
            print("Sie sind normalgewichtig.")
        else: # bmi >= 25
            print("Sie sind übergewichtig.")

    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie nur Zahlen ein.")

if __name__ == "__main__":
    bmirechner()