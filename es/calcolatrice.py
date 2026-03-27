print("Benvenuto nella calcolatrice che ruba il lavoro a conti")

Num1 = input("inserisci il tuo primo numero: ")

Segno = input("inserisci il se segno che vuoi usare: (+ - * /): ")

Num2 = input("inserisci il tuo secondo numero: ")

if Segno == "+":
    result = int(Num1) + int(Num2)
    print (round(result, 2))
elif Segno == "-":
    result = int(Num1) - int(Num2)
    print (round(result, 2))
elif Segno == "*":
    result = int(Num1) * int(Num2)
    print (round(result, 2))
elif Segno == "/":
        result = int(Num1) / int(Num2)
        print (round(result, 2))
else:
    print("Errore:  per zero non è consentita.")
