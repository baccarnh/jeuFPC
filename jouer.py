def ENTRE():
    nom=input("entrer votre nom")
    while len(nom)<2: #oblige the player to give a real name with at least 2 letters
        print("erreur renter votre nom de minimum 2 lettres")
        nom = input("entrer votre nom")
    else:
        print("nom du joueur=", nom.upper())

def CHOIX():
    ch = input("entrer votre choix parmi feuille/pierre/ciseaux").upper()
    # ch=ch.upper() ##accept all type of letters
    FPC = ['FEUILLE', 'PIERRE', 'CISEAUX']
    while ch not in FPC:  ##verify that the choice is OK
        print("erreur choix non valide")
        ch = input("entrer votre choix parmi feuille/pierre/ciseaux").upper()
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
    while scor_pl!=3 and scor_comp!=3:
        player_c=CHOIX()
        computer_c=CHOIXPC()
        player_win=[('PIERRE','CISEAUX'), ('FEUILLE','PIERRE'), ('CISEAUX', 'FEUILLE')]
        computer_win=[('PIERRE','FEUILLE'), ('FEUILLE','CISEAUX'), ('CISEAUX', 'PIERRE') ]
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
    if scor_pl==3:
        print('la partie est finie, vous avez gagné')
    elif scor_comp==3:
        print('la partie est finie, vous avez perdu')
    return (scor_pl, scor_comp)


def PLAYAGAIN():
    pl = input("voulez vous jouer de nouveau? taper oui ou non").upper()
    tag=["OUI", "NON"]
    while pl not in tag:
        print("erreur de saisie taper oui ou non")
        pl = input("entrer votre réponce de nouveau").upper()
    if pl=="NON":
        print("Merci Aurevoir")
    elif pl=="OUI":
        print("les scores sont remis à zéros")
    return pl



ENTRE()
scorej=0
scorepc=0
(scorej, scorepc)=ATTRIBUE()
answer=PLAYAGAIN()
while answer=="OUI":
    scorej = 0
    scorepc = 0
    (scorej, scorepc)=ATTRIBUE()
    answer=PLAYAGAIN()