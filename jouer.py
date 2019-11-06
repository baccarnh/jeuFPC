def ENTRE():
    nom=input("entrer votre nom")
    while len(nom)<2:
        print("erreur renter votre nom de minimum 2 lettres")
        nom = input("entrer votre nom")
    else:
        print("nom du joueur=", nom.upper())


ENTRE()