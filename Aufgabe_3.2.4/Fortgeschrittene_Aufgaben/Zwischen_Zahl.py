## Zahl zwischen zwei anderen?
## Lies drei Zahlen ein. Überprüfe, ob die zweite Zahl zwischen der ersten und dritten liegt.

def zwischenzahl():
    try:
        zahl01 = int(input("Bitte geben Sie die erste Zahl ein: "))
        zahl02 = int(input("Bitte geben Sie die zweite Zahl ein: "))
        zahl03 = int(input("Bitte geben Sie die dritte Zahl ein: "))

        if (zahl01 <= zahl02 <= zahl03) or (zahl03 <= zahl02 <= zahl01):
            print(f"Die Zahl {zahl02} liegt zwischen {zahl01} und {zahl03}.")
        else:
            print(f"Die Zahl {zahl02} liegt NICHT zwischen {zahl01} und {zahl03}.")
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie nur Zahlen ein.")

if __name__ == "__main__":
    zwischenzahl()