class BankAccount:
    def __init__(self, kontoinhaber, ueberziehungsrahmen=-100.0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = 0.0
        self.ueberziehungsrahmen = ueberziehungsrahmen

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag:.2f} € eingezahlt.")
        else:
            print("Einzahlungsbetrag muss positiv sein.")

    def abheben(self, betrag):
        if betrag <= 0:
            print("Abhebungsbetrag muss positiv sein.")
            return

        if not self._hat_ueberzogen(betrag):
            self.kontostand -= betrag
            print(f"{betrag:.2f} € abgehoben.")
        else:
            print(f"Abhebung abgelehnt. Überziehungsrahmen von {self.ueberziehungsrahmen:.2f} € würde überschritten.")

    def _hat_ueberzogen(self, betrag):
        """Private Methode: Prüft, ob der Kontostand nach Abhebung unter den Überziehungsrahmen fällt."""
        return self.kontostand - betrag < self.ueberziehungsrahmen

    def zeige_kontostand(self):
        print(f"Aktueller Kontostand: {self.kontostand:.2f} €")

    def __str__(self):
        return f"Konto von {self.kontoinhaber} – Kontostand: {self.kontostand:.2f} €"

