Age = input("insrisci la tua età: ")

if int(Age) == 22:
    print("22 simba")
elif int(Age) >= 18:
    print("puoi bere alcolici")
else:    
    print(f"non puoi bere alcolici perche la tua eta di {Age} e minore di 18")


F = input("sei felice oggi? (Y/N)")

if F == "Y":
    print("sono felice per te")
else:
    print("mi dispiace, spero che la tua giornata migliori")
