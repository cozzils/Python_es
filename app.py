import math

x = 5

print(math.pi) #stampa il valore di pi greco
print(math.e) #stampa il valore di euler
result = math.sqrt(x) #calcola la radice quadrata di x
result = math.ceil(x) #arrotonda per eccesso
result = math.floor(x) #arrotonda per diffeto 

radius = float(input("inserisci il raggio del cerchio: "))  

area = math.pi * pow(radius, 2) #calcola l'area del cerchio usando la formula A = πr^2

print(f"L'area del cerchio con raggio {radius} è: {area}")