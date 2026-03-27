name = input("Scrivi il tuo nome: ")

result = len(name) #len conta le lettere tenendo in considerazione anche gli spazi
result = name.find("a") #find trova la posizione della prima lettera che viene ricercata 
result = name.rfind("a") #rfind trova la posizione dell'ultima lettera che viene ricercata
result = name.capitalize() #capitalize mette in maiuscolo la prima lettera della stringa
result = name.upper() #upper mette tutte le lettere in maiuscolo
result = name.lower() #lower mette tutte le lettere in minuscolo
result = name.isdigit() #isdigit controlla se la stringa è composta solo da numeri
result = name.isalpha() #isalpha controlla se la stringa è composta solo da lettere
result = name.replace("a", "o") #replace sostituisce una lettera con un'altra
result = name.count("a") #count conta quante volte una lettera appare nella stringa
result = name.replace(" ", "_") #replace sostituisce gli spazi con underscore

print(result)