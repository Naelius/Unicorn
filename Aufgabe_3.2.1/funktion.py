def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))

def temp_list(start=-20, ende=41, schritt=5):
    breite = 50
    print("\n" + "📋 Temperaturtabelle".center(breite)) 
    print("Celsius → Fahrenheit & Kelvin".center(breite))
    print("=" * 50)
    print(f"{'Celsius (°C)':<15}{'Fahrenheit (°F)':<18}{'Kelvin (K)':<12}")
    print("-" * 50)
    for c in range(start, ende, schritt):
        f = c_to_f(c)
        k = c_to_k(c)
        print(f"{c:<15.2f}{f:<18.2f}{k:<12.2f}")
    print("=" * 50)

def menu():
    breite = 50
    print("\n" + "=" * 50)
    print("🌡️  Temperaturumrechner".center(breite))
    print("=" * 50)
    print("1. Celsius    ➡️    Fahrenheit")
    print("2. Fahrenheit ➡️    Celsius")
    print("3. Celsius    ➡️    Kelvin")
    print("4. Kelvin     ➡️    Celsius")
    print("5. Fahrenheit ➡️    Kelvin")
    print("6. Kelvin     ➡️    Fahrenheit")
    print("7. 📋 Temperaturtabelle anzeigen")
    print("8. ❌ Beenden")
    print("=" * 50)

def text_center(text, breite=50):
    print("\n" + "=" * breite)
    print("|" + text.center(breite-2) + "|")
    print("=" * breite)

def temp_rechner():
    while True:
        menu()
        wahl = input("Bitte wähle eine Option (1–8): ").strip()

        try:
            if wahl == "1":
                celsius = float(input("🌡️  Temperatur in Celsius: "))
                fahrenheit = c_to_f(celsius)
                text_center(f"{celsius:.2f}°C sind {fahrenheit:.2f}°F")

            elif wahl == "2":
                fahrenheit = float(input("🌡️  Temperatur in Fahrenheit: "))
                celsius = f_to_c(fahrenheit)
                text_center(f"{fahrenheit:.2f}°F sind {celsius:.2f}°C")

            elif wahl == "3":
                celsius = float(input("🌡️  Temperatur in Celsius: "))
                kelvin = c_to_k(celsius)
                text_center(f"{celsius:.2f}°C sind {kelvin:.2f}K")

            elif wahl == "4":
                kelvin = float(input("🌡️  Temperatur in Kelvin: "))
                celsius = k_to_c(kelvin)
                text_center(f"{kelvin:.2f}K sind {celsius:.2f}°C")

            elif wahl == "5":
                fahrenheit = float(input("🌡️  Temperatur in Fahrenheit: "))
                kelvin = f_to_k(fahrenheit)
                text_center(f"{fahrenheit:.2f}°F sind {kelvin:.2f}K")

            elif wahl == "6":
                kelvin = float(input("🌡️  Temperatur in Kelvin: "))
                fahrenheit = k_to_f(kelvin)
                text_center(f"{kelvin:.2f}K sind {fahrenheit:.2f}°F")

            elif wahl == "7":
                temp_list()

            elif wahl == "8":
                print("Programm wird beendet. Auf Wiedersehen! 👋 ")
                break

            else:
                print("❗ Ungültige Auswahl. Bitte wähle zwischen 1 und 8. ❗")

        except ValueError:
            print("⚠️ Falsche Eingabe! Bitte eine Zahl eingeben! ⚠️")


temp_rechner()
