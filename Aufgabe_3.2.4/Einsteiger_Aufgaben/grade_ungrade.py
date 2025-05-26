## Gerade oder ungerade?
## Schreibe ein Programm, das eine Zahl vom Benutzer einliest und ausgibt, ob sie gerade oder ungerade ist.

zahl = int(input("Gib eine Zahl ein: "))

if zahl % 2 == 0:
    print("Zahl ist gerade")
else:
    print("Zahl ist ungerade")
