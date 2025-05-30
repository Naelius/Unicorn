import tkinter as tk
from tkinter import messagebox

class TemperaturumrechnerGUI:
    def __init__(self, master):
        self.master = master
        master.title("🌡️ Temperaturumrechner")
        master.configure(bg="#f0f8ff")

        self.label = tk.Label(master, text="🌡️ Temperaturumrechner", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#003366")
        self.label.pack(pady=10)

        self.optionen = [
            "Celsius ➡️ Fahrenheit",
            "Fahrenheit ➡️ Celsius",
            "Celsius ➡️ Kelvin",
            "Kelvin ➡️ Celsius",
            "Fahrenheit ➡️ Kelvin",
            "Kelvin ➡️ Fahrenheit"
        ]

        self.var = tk.StringVar(master)
        self.var.set(self.optionen[0])
        self.option_menu = tk.OptionMenu(master, self.var, *self.optionen)
        self.option_menu.config(font=("Helvetica", 12))
        self.option_menu.pack(pady=5)

        self.eingabe_label = tk.Label(master, text="Temperatur eingeben:", font=("Helvetica", 12), bg="#f0f8ff")
        self.eingabe_label.pack(pady=2)
        self.eingabe_entry = tk.Entry(master, font=("Helvetica", 12))
        self.eingabe_entry.pack(pady=5)

        self.berechnen_button = tk.Button(master, text="Umrechnen", command=self.umrechnen, font=("Helvetica", 12, "bold"), bg="#003366", fg="white")
        self.berechnen_button.pack(pady=10)

        self.ergebnis_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f8ff", fg="#006400")
        self.ergebnis_label.pack(pady=5)

    def umrechnen(self):
        try:
            wert = float(self.eingabe_entry.get())
            auswahl = self.var.get()
            
            if auswahl == "Celsius ➡️ Fahrenheit":
                ergebnis = wert * 9 / 5 + 32
                self.ergebnis_label.config(text=f"{wert:.2f}°C = {ergebnis:.2f}°F")
            elif auswahl == "Fahrenheit ➡️ Celsius":
                ergebnis = (wert - 32) * 5 / 9
                self.ergebnis_label.config(text=f"{wert:.2f}°F = {ergebnis:.2f}°C")
            elif auswahl == "Celsius ➡️ Kelvin":
                ergebnis = wert + 273.15
                self.ergebnis_label.config(text=f"{wert:.2f}°C = {ergebnis:.2f}K")
            elif auswahl == "Kelvin ➡️ Celsius":
                ergebnis = wert - 273.15
                self.ergebnis_label.config(text=f"{wert:.2f}K = {ergebnis:.2f}°C")
            elif auswahl == "Fahrenheit ➡️ Kelvin":
                ergebnis = (wert - 32) * 5 / 9 + 273.15
                self.ergebnis_label.config(text=f"{wert:.2f}°F = {ergebnis:.2f}K")
            elif auswahl == "Kelvin ➡️ Fahrenheit":
                ergebnis = (wert - 273.15) * 9 / 5 + 32
                self.ergebnis_label.config(text=f"{wert:.2f}K = {ergebnis:.2f}°F")
        
        except ValueError:
            messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperaturumrechnerGUI(root)
    root.mainloop()