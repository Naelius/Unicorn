## Positiv, negativ oder null
## Lies eine Zahl ein und gib aus, ob sie positiv, negativ oder null ist.

number = int(input("Bitte gib eine Zahl ein: "))

if number == 0:
    print("Die Zahl ist null")
elif number > 0:
    print("Die Zahl ist positiv")
else:
    print("Die Zahl ist negativ")