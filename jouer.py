def ENTRE():
    nom=input("entrer votre nom")
    while len(nom)<2: #oblige the player to give a real name with at least 2 letters
        print("erreur renter votre nom de minimum 2 lettres")
        nom = input("entrer votre nom")
    else:
        print("nom du joueur=", nom.upper())

def CHOIX():
    ch=input("entrer votre choix parmi feuille/pierre/ciseaux")
    ch=ch.upper() ##accept all type of letters
    FPC=['FEUILLE', 'PIERRE', 'CISEAUX']
    while ch not in FPC: ##verify that the choice is OK
        print("erreur choix non valide")
        ch=input("rentrer votre choix de nouveau")
    if ch in FPC:
        print("le choix du joueur est", ch)
    return ch


def CHOIXPC():
    import random
    FPC = ['FEUILLE', 'PIERRE', 'CISEAUX']
    rch=random.choice(FPC)#the computer choice
    print('le choix de lordinateur est', rch)#present the computer choice to the player
    return rch


def ATTRIBUE():
    scor_pl= 0
    scor_comp= 0
    player_c=CHOIX()
    computer_c=CHOIXPC()
    player_win=[('PIERRE','CISEAUX'), ('FEUILLE','PIERRE'), ('CISEAUX', 'FEUILLE')]
    computer_win=[('PIERRE','FEUILLE'), ('FEUILLE','CISEAU'), ('CISEAUX', 'PIERRE') ]
    if player_c==computer_c:
        scor_pl+=0
        scor_comp+=0
        print("vous avez fait le meme choix que la machine vos scores")
    elif (player_c, computer_c) in player_win:
        scor_pl+=1
        scor_comp+=0
    elif (player_c, computer_c) in computer_win :
        scor_pl+=0
        scor_comp+=1
    print("le score du joueur est",scor_pl, "le score de la machine est", scor_comp)
    return (scor_pl, scor_comp)



scorej=0
scorepc=0

ENTRE()
while scorej<3 and scorepc<3:
    (scorej, scorepc)=ATTRIBUE()
