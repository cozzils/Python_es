amico1 = "lorenzo"
amico2 = "marta"
amico3 = "gaia"

aggetivo = "e stupido"

#print(f"{amico1} {aggetivo} ")
#print(f"{amico2} {aggetivo}")
#print(f"{amico3} {aggetivo}")


Risparmio = 11
mesi = 6
target = 100

os = target / Risparmio

Accumullo = Risparmio * mesi 
Attualita = target - Accumullo

tempo =  Attualita / Risparmio


#print(f"Per addeso hai risparmiato {Accumullo}")
#print(f"Per il tuo target ti manca {Attualita}")
#print(f"Continuando cosi ci vorra ancora {tempo} per raggiungere l'obbietivo")
#print(os)


Pasquetta = True

#if Pasquetta:
    #print("spacchiammo tutto")
#else:
    #print("organnizziamo")



#base per costruire un piccolo check campo per login o altro 
#name = input("compila con il tuo nome: ")

#name = bool(name)

#Nome = name

#if Nome:
 #   print("puoi proccedere")
#else: 
#    print("compila il campo nome")


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

