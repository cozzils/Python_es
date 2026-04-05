import re # importo la libreria re per utilizzare re.fullmatch(r'^[a-zA-Z_]+$', name)

username = input("inserisci il tuo username: ")
name = (username)
name = username.replace(" ", "_")

# mia versione 
if len(name) > 12:
    print("Il tuo username è troppo lungo!")
elif re.fullmatch(r'^[a-zA-Z_]+$', name):
    print(f"il tuo username è {name} ")
else:
    print("Il tuo username non può contenere numeri o caratteri speciali!")

    
