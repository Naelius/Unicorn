import random

def guess_number():
    randomnumber = random.randint(1, 100)
    attempts = 0

    print("Kannst du meine Zahl zwischen 1 und 100 erraten?")

    while True:
        try:
            guess = int(input("Dein Tipp: "))
        except ValueError:
            print("Bitte nur eine Zahl eingeben")
            continue

        attempts += 1

        if guess < 1 or guess > 100:
            print("Die Zahl muss zwischen 1 und 100 liegen")
        elif guess < randomnumber:
            print("Nein, zu niedrig")
        elif guess > randomnumber:
            print("Nein, zu hoch")
        else:
            print(f"Herzlichen Glückwunsch, du hast die Nummer nach {attempts} Versuchen gefunden!")

guess_number()