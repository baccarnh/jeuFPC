def ENTRE():
    nom=input("entrer votre nom")
    while len(nom)<2:
        print("erreur renter votre nom de minimum 2 lettres")
        nom = input("entrer votre nom")
    else:
        print("nom du joueur=", nom.upper())

def CHOIX():
    ch=input("entrer votre choix parmi feuille/pièrre/ciseaux")
    ch=ch.upper() #accept all type of letters
    FPC=['FEUILLE', 'PIERRE', 'CISEAUX']
    while ch not in FPC: # verify that the choice is OK
        print("erreur choix non valide")
        ch=input("rentrer votre choix de nouveau")
    else:
        print("le choix du joueur est {}".format(ch))




ENTRE()
CHOIX()