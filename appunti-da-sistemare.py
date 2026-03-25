Pasquetta = True

if Pasquetta:
    print("spacchiammo tutto")
else:
    print("organnizziamo")



#base per costruire un piccolo check campo per login o altro 
name = input("compila con il tuo nome: ")

name = bool(name)

Nome = name

if Nome:
    print("puoi proccedere")
else: 
    print("compila il campo nome")