import random                    # Für die zufällige Zahl zwischen 1 und 100
import tkinter as tk             # Für die GUI-Bibliothek tkinter
from tkinter import messagebox   # Für Popup-Nachrichten im GUI
from PIL import Image, ImageTk   # Pillow-Bibliothek für Bildverarbeitung
from PIL.Image import Resampling # Für hochwertige Bildskalierung (anstelle von ANTIALIAS)

class RateSpielGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Zahlenraten-Spiel")     # Fenstertitel setzen
        self.master.config(bg="#1497d4")           # Hintergrundfarbe des Fensters setzen (wird aber vom Bild überdeckt)

        # Hintergrundbild laden, unverändert (Originalgröße)
        self.original_bg_image = Image.open("bild.png")

        # Label-Widget als Container für das Hintergrundbild erstellen
        self.bg_label = tk.Label(self.master)
        # Das Label so platzieren, dass es das ganze Fenster ausfüllt
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame für die restlichen Widgets (Text, Eingabe, Button)
        # Damit wir alles zusammen gruppieren und einfach zentrieren können
        self.frame = tk.Frame(self.master, bg="#1497d4")
        # Frame mittig im Fenster platzieren (relx=0.5, rely=0.5 bedeutet 50% Position x und y)
        # anchor="center" sorgt dafür, dass der Frame genau an diesem Punkt zentriert ist
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Zufallszahl generieren zwischen 1 und 100
        self.randomnumber = random.randint(1, 100)
        # Versuchszähler auf 0 setzen
        self.attempts = 0

        # Text-Label mit Frage, mittig, mit Schriftart und Farbe
        self.label = tk.Label(
            self.frame,
            text="Kannst du meine Zahl zwischen 1 und 100 erraten?",
            font=("Arial", 14),
            bg="#1497d4",
            fg="#000000",
            justify="center"
        )
        # Label im Frame mit Grid platzieren, mit Abstand (pady) und horizontaler Ausdehnung (sticky="ew")
        self.label.grid(row=0, column=0, pady=15, sticky="ew")

        # Eingabefeld für die Benutzereingabe
        self.entry = tk.Entry(self.frame, font=("Arial", 12), width=10, justify="center")
        # Eingabefeld direkt unter dem Label platzieren mit Abstand
        self.entry.grid(row=1, column=0, pady=5)

        # Button mit Text und Farbe, ruft bei Klick die Methode überprüfe_tipp auf
        self.button = tk.Button(
            self.frame,
            text="Tipp abgeben",
            font=("Arial", 12, "bold"),
            bg="#E7770F",
            fg="white",
            activebackground="#45a049",
            command=self.überprüfe_tipp
        )
        # Button unter dem Eingabefeld platzieren, mit Abstand, und horizontal ausdehnen
        self.button.grid(row=2, column=0, pady=10, sticky="ew")

        # Label für Feedback (z. B. "Zu hoch", "Zu niedrig")
        self.feedback_label = tk.Label(
            self.frame,
            text="",
            font=("Arial", 14),
            bg="#1497d4",
            fg="#000000"
        )
        # Feedback-Label unter dem Button platzieren
        self.feedback_label.grid(row=3, column=0, pady=5, sticky="ew")

        # Spalte 0 im Frame so konfigurieren, dass sie sich mit dem Fenster verbreitert (flexible Breite)
        self.frame.grid_columnconfigure(0, weight=1)

        # Event-Handler registrieren, der auf Fenstergrößenänderung reagiert
        # Damit das Hintergrundbild bei Größenänderung automatisch skaliert wird
        self.master.bind("<Configure>", self.resize_background)

        # Beim Start direkt Hintergrundbild in der aktuellen Fenstergröße anzeigen
        self.resize_background()

    def resize_background(self, event=None):
        # Aktuelle Fensterbreite holen
        width = self.master.winfo_width()
        # Aktuelle Fensterhöhe holen
        height = self.master.winfo_height()

        # Falls Fenstergröße noch nicht initialisiert ist (0 oder 1), dann abbrechen
        if width < 1 or height < 1:
            return

        # Hintergrundbild auf die aktuelle Fenstergröße skalieren
        resized = self.original_bg_image.resize((width, height), Resampling.LANCZOS)
        # Bild in ein tkinter-kompatibles Bild umwandeln
        self.bg_photo = ImageTk.PhotoImage(resized)

        # Hintergrund-Label mit dem neuen Bild updaten
        self.bg_label.config(image=self.bg_photo)
        # Referenz auf das Bild speichern, damit es nicht vom Garbage Collector gelöscht wird
        self.bg_label.image = self.bg_photo

    def überprüfe_tipp(self):
        # Eingabe aus dem Eingabefeld lesen
        eingabe = self.entry.get()

        # Versuch, Eingabe in Integer umzuwandeln
        try:
            guess = int(eingabe)
        except ValueError:
            # Falls Eingabe keine Zahl ist, Feedback anzeigen und Funktion beenden
            self.feedback_label.config(text="Bitte nur eine Zahl eingeben")
            return

        # Versuchszähler erhöhen
        self.attempts += 1

        # Prüfen, ob die Zahl im erlaubten Bereich liegt
        if guess < 1 or guess > 100:
            self.feedback_label.config(text="Die Zahl muss zwischen 1 und 100 liegen")
        # Feedback, wenn Zahl zu klein ist
        elif guess < self.randomnumber:
            self.feedback_label.config(text="Nein, zu niedrig")
        # Feedback, wenn Zahl zu groß ist
        elif guess > self.randomnumber:
            self.feedback_label.config(text="Nein, zu hoch")
        else:
            # Bei richtigem Tipp Popup mit Erfolg und Anzahl Versuche zeigen
            messagebox.showinfo("🎉 Erfolg!", f"Richtig! Nach {self.attempts} Versuchen.")
            # Spiel neustarten
            self.neustart()

    def neustart(self):
        # Neue Zufallszahl generieren
        self.randomnumber = random.randint(1, 100)
        # Versuchszähler zurücksetzen
        self.attempts = 0
        # Eingabefeld löschen
        self.entry.delete(0, tk.END)
        # Feedback-Label zurücksetzen
        self.feedback_label.config(text="Neues Spiel gestartet!")

# Programmstart:
root = tk.Tk()               # Hauptfenster erstellen
root.geometry("600x300")     # Fenstergröße festlegen (Breite x Höhe)
spiel = RateSpielGUI(root)   # Objekt der Klasse RateSpielGUI mit root als Fenster erzeugen
root.mainloop()              # Haupt-Eventloop starten (Fenster anzeigen und auf Events warten)
