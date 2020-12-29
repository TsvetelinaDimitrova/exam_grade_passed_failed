#Prüfungsergebnis
a = int(input("Note für Pflichtfach A eingeben:"))
b = int(input("Note für Pflichtfach B eingeben:"))
w = int(input("Note für Wahlfach eingeben:\t"))
d = (a+b+w)/3
if int(a)<=6 and int(b)<=6 and int(w)<=6:
    if d<4.5 :
        if a<4:
            print("Prüfung bestanden")
        else:
            print("Prüfung nicht bestanden")
    else:
        print("Prüfung nicht bestanden")
else:
    print("Sie sollen nur Noten zwischen 1 und 6 eingeben")
input("Beenden mit Eingabetaste")