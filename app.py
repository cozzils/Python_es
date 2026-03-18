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


print(f"Per addeso hai risparmiato {Accumullo}")
print(f"Per il tuo target ti manca {Attualita}")
print(f"Continuando cosi ci vorra ancora {tempo} per raggiungere l'obbietivo")
print(os)