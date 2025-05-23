Name = "Max Mustermann"
Alter = "30"
Geschlecht = "männlich"
Größe = "1,80m"
Gewicht = "75kg"
Augenfarbe = "braun"
Haarfarbe = "schwarz"
Beruf = "Softwareentwickler"
Hobby = "Lesen"
Charaktereigenschaften = "freundlich"


satz = (
    f"{Name} ist ein {Alter}-jähriger, {Charaktereigenschaften}er {Beruf}. \n"
    f"Er ist {Geschlecht}, {Größe} groß, wiegt {Gewicht}, hat {Augenfarbe}e Augen und {Haarfarbe}e Haare. "
    f"In seiner Freizeit liest er gerne. \n \n"
)

print(satz)


# DnD-Charakter-Datensatz
name = "Elionis Silbermähne"
alter = 42
geschlecht = "männlich"
größe = "2,10 m"
gewicht = "130 kg"
augenfarbe = "eisblau"
haarfarbe = "silbern"
rasse = "Leonin"
charakter_klasse = "Paladin des Einhorn-Gottes"
herkunft = "Steppe von Tharalon"
charaktereigenschaften = ["ehrenhaft", "beschützend", "gläubig"]


satz02 = (
    f"{name} ist ein {alter}-jähriger, {', '.join(charaktereigenschaften)}er "
    f"{rasse}-{charakter_klasse} aus der {herkunft}. \nMit {größe} Größe, "
    f"{gewicht} Gewicht, {augenfarbe}en Augen und {haarfarbe}er Mähne dient er "
    f"seinem Einhorn-Gott mit unerschütterlichem Glauben und beschützender Stärke."
)

print(satz02)