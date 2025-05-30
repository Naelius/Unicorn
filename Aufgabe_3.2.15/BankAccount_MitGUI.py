import tkinter as tk
from tkinter import messagebox, simpledialog

class BankAccount:
    def __init__(self, kontoinhaber, ueberziehungsrahmen=-100.0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = 0.0
        self.ueberziehungsrahmen = ueberziehungsrahmen

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            return True, f"{betrag:.2f} € eingezahlt."
        else:
            return False, "Einzahlungsbetrag muss positiv sein."

    def abheben(self, betrag):
        if betrag <= 0:
            return False, "Abhebungsbetrag muss positiv sein."
        if not self._hat_ueberzogen(betrag):
            self.kontostand -= betrag
            return True, f"{betrag:.2f} € abgehoben."
        else:
            return False, f"Abhebung abgelehnt. Überziehungsrahmen von {self.ueberziehungsrahmen:.2f} € würde überschritten."

    def _hat_ueberzogen(self, betrag):
        return self.kontostand - betrag < self.ueberziehungsrahmen

    def zeige_kontostand(self):
        return f"Aktueller Kontostand: {self.kontostand:.2f} €"

    def zinsen_berechnen(self, zinssatz):
        if self.kontostand > 0:
            zinsen = self.kontostand * (zinssatz / 100)
            self.kontostand += zinsen
            return True, f"Zinsen in Höhe von {zinsen:.2f} € gutgeschrieben."
        else:
            return False, "Keine Zinsen berechnet, da der Kontostand nicht positiv ist."

    def __str__(self):
        return f"Konto von {self.kontoinhaber} – Kontostand: {self.kontostand:.2f} €"


class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bankkonto Verwaltung")
        self.geometry("600x500")
        self.configure(bg="#f0f4f8")

        self.konto = BankAccount("Unicorn")

        self.create_widgets()
        self.update_kontostand_label()

    def create_widgets(self):
        # Titel
        title = tk.Label(self, text="Willkommen bei Unicorn Bank", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#003366")
        title.pack(pady=10)

        # Kontostand-Anzeige
        self.kontostand_label = tk.Label(self, text="", font=("Arial", 14), bg="#f0f4f8", fg="#004080")
        self.kontostand_label.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self, bg="#f0f4f8")
        btn_frame.pack(pady=15)

        btn_einzahlen = tk.Button(btn_frame, text="Einzahlen", width=12, command=self.einzahlen)
        btn_einzahlen.grid(row=0, column=0, padx=5, pady=5)

        btn_abheben = tk.Button(btn_frame, text="Abheben", width=12, command=self.abheben)
        btn_abheben.grid(row=0, column=1, padx=5, pady=5)

        btn_zinsen = tk.Button(btn_frame, text="Zinsen berechnen", width=25, command=self.zinsen_berechnen)
        btn_zinsen.grid(row=1, column=0, columnspan=2, pady=5)
        self.btn_zinsen = btn_zinsen

        # Status Label
        self.status_label = tk.Label(self, text="", font=("Arial", 12), bg="#f0f4f8")
        self.status_label.pack(pady=10)

    def update_kontostand_label(self):
        self.kontostand_label.config(text=str(self.konto))

    def einzahlen(self):
        betrag = self.ask_betrag("Einzahlen")
        if betrag is not None:
            success, message = self.konto.einzahlen(betrag)
            self.show_status(message, success)
            self.update_kontostand_label()

    def abheben(self):
        betrag = self.ask_betrag("Abheben")
        if betrag is not None:
            success, message = self.konto.abheben(betrag)
            self.show_status(message, success)
            self.update_kontostand_label()

    def zinsen_berechnen(self):
        zinssatz = 7.2
        success, message = self.konto.zinsen_berechnen(zinssatz)
        self.show_status(message, success)
        self.update_kontostand_label()
        if success:
            self.btn_zinsen.config(state="disabled")

    def ask_betrag(self, titel):
        try:
            eingabe = simpledialog.askstring(titel, f"Gib den Betrag für '{titel}' ein:")
            if eingabe is None:
                return None
            betrag = float(eingabe.replace(",", "."))
            return betrag
        except ValueError:
            messagebox.showerror("Ungültige Eingabe", "Bitte eine gültige Zahl eingeben.")
            return None

    def show_status(self, message, success):
        self.status_label.config(text=message)
        if success:
            self.status_label.config(fg="green")
        else:
            self.status_label.config(fg="red")


if __name__ == "__main__":
    app = BankApp()
    app.mainloop()
