#ES 1 rettangolo 
name = input("inserisci il tuo nome: ")

print(f"ciao {name} oggi andiamo a costruire un rettangolo e a calcolare la sua aerea")

altezza = input("inserisci l'altezza del nostro rettangolo: ")

lunghezza = input("inserisci la lunghezza del nostro rettangolo: ")

lunghezza = True 
while lunghezza > altezza :
    print(f"la lunghezza non puo essere minore dell'altezza che è {altezza}, perfafore inserisci un altro valore")


A = int(altezza)

L = int(lunghezza)

Area = A * L

print(f"ecco l'area del nostro rettangolo : {Area}, bel lavoro {name} ")
