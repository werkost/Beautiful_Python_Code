import matplotlib.pyplot as plt

summe = 0
feldListe = []

for feld in range(64):
    reiskorn = 2**feld
    feldListe.append(reiskorn)
    summe += reiskorn
    print(f"Feld {feld+1}: = {reiskorn:>28,} Reiskörner, insgesamt {summe:>28,} Reiskörner.")
print()

gewicht = summe * 0.02 / 1000 / 1000
print(f"Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten Reiskörner {gewicht:,.0f} Tonnen.")
print()
plt.plot(feldListe)
plt.show()
