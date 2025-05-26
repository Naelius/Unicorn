## Passwort prüfen
## Erstelle ein einfaches Login-System, das überprüft, ob das eingegebene Passwort "geheim" ist.

def login():
    correct_password = "geheim"
    entered_password = input("Bitte geben Sie das Passwort ein: ")

    if entered_password == correct_password:
        print("Login erfolgreich! Willkommen")
    else:
        print("Passwort falsch. Zugang verweigert")

if __name__ == "__main__":
    login()