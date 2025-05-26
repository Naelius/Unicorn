## Größte von drei Zahlen
## Lies drei Zahlen ein und gib die größte aus.

def find_largest_number():
    try:
        zahl01 = float(input("Erste Zahl: "))
        zahl02 = float(input("Zweite Zahl: "))
        zahl03 = float(input("Dritte Zahl: "))

        if zahl01 >= zahl02 and zahl01 >= zahl03:
            print(f"Die größte Zahl ist: {zahl01}")
        elif zahl02 >= zahl01 and zahl02 >= zahl03:
            print(f"Die größte Zahl ist: {zahl02}")
        else:
            print(f"Die größte Zahl ist: {zahl03}")

    except ValueError:
        print("Ungültige Eingabe. Nur Zahlen eingeben")

if __name__ == "__main__":
    find_largest_number()