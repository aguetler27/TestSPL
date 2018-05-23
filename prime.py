# primzahlen ueberpruefen
zahl = input("Bitte eine Zahl eingeben: ")
z = int(zahl)
prime = True
for i in range (2, z):
    # ist die zahl durch i teilbar?
    # dann ist sie keine Primzahl!
    if (z % i == 0):
        prime = False
    # ist die zahl nie durch i teilbar?
    # dann ist sie eine Primzahl!

if (prime == True):
    print(zahl+" ist eine Primzahl.")
else:
    print(zahl+" ist keine Primzahl.")

    
