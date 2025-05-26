import tkinter as tk
from tkinter import messagebox

def validate_int(value, field_name):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"{field_name} muss eine ganze Zahl sein.")

def speichern():
    try:
        zimmer = {
            "Zimmernummer": validate_int(entry_zimmernummer.get(), "Zimmernummer"),
            "Etage": validate_int(entry_etage.get(), "Etage"),
            "Fläche (m²)": validate_int(entry_flaeche.get(), "Fläche"),
            "Badewanne": var_badewanne.get(),
            "Balkon": var_balkon.get(),
            "Zimmerart": entry_zimmerart.get(),
            "Zustand": var_zustand.get(),
            "Wandfarbe": entry_wandfarbe.get(),
            "Küche": var_kueche.get(),
            "Internet": entry_internet.get()
        }

        ausgabe_text = "Zimmerdaten:\n" + "-"*30 + "\n"
        for key, value in zimmer.items():
            ausgabe_text += f"{key}: {value}\n"

        text_output.config(state='normal')
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, ausgabe_text)
        text_output.config(state='disabled')
        
    except ValueError as e:
        messagebox.showerror("Fehler", str(e))


# GUI-Fenster
fenster = tk.Tk()
fenster.title("Zimmerdaten Eingabe")
fenster.geometry("400x600")

# Eingabefelder
tk.Label(fenster, text="Zimmernummer:").pack()
entry_zimmernummer = tk.Entry(fenster)
entry_zimmernummer.pack()

tk.Label(fenster, text="Etage:").pack()
entry_etage = tk.Entry(fenster)
entry_etage.pack()

tk.Label(fenster, text="Fläche in m²:").pack()
entry_flaeche = tk.Entry(fenster)
entry_flaeche.pack()

tk.Label(fenster, text="Badewanne vorhanden?").pack()
var_badewanne = tk.StringVar(value="nein")
tk.OptionMenu(fenster, var_badewanne, "ja", "nein").pack()

tk.Label(fenster, text="Balkon vorhanden?").pack()
var_balkon = tk.StringVar(value="nein")
tk.OptionMenu(fenster, var_balkon, "ja", "nein").pack()

tk.Label(fenster, text="Zimmerart:").pack()
entry_zimmerart = tk.Entry(fenster)
entry_zimmerart.pack()

tk.Label(fenster, text="Frisch gestrichen?").pack()
var_zustand = tk.StringVar(value="nein")
tk.OptionMenu(fenster, var_zustand, "ja", "nein").pack()

tk.Label(fenster, text="Farbe der Wand:").pack()
entry_wandfarbe = tk.Entry(fenster)
entry_wandfarbe.pack()

tk.Label(fenster, text="Küche vorhanden?").pack()
var_kueche = tk.StringVar(value="nein")
tk.OptionMenu(fenster, var_kueche, "ja", "nein").pack()

tk.Label(fenster, text="Internet-Anbieter:").pack()
entry_internet = tk.Entry(fenster)
entry_internet.pack()

# Button
tk.Button(fenster, text="Speichern", command=speichern).pack(pady=10)

# Textfeld zur Ausgabe
text_output = tk.Text(fenster, height=12, width=40, state='disabled', bg="#f0f0f0")
text_output.pack(pady=10)

fenster.mainloop()
