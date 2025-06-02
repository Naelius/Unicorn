def zinsen_berechnen(self, zinssatz):
    if self.kontostand > 0:
        zinsen = self.kontostand * (zinssatz / 100)
        self.kontostand += zinsen
        print(f"Zinsen in Höhe von {zinsen:.2f} € gutgeschrieben.")
    else:
        print("Keine Zinsen berechnet, da der Kontostand nicht positiv ist.")