età = input("inserisci la tua età: ")
accompagnato = input("sei accompagnato? (si/no): ")

if int(età) >= 18:
    print("puoi entrare")
elif int(età) >= 16 and accompagnato == "si":
    print("puoi entrare")
else:
    print("non puoi entrare")