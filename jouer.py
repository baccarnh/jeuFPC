def ENTRE():
    nom=input("entrer votre nom")
    while len(nom)<2: #oblige the player to give a real name with at least 2 letters
        print("erreur renter votre nom de minimum 2 lettres")
        nom = input("entrer votre nom")
    else:
        print("nom du joueur=".center(50), nom.upper().center(50))

def CHOIX():
    ch = input("entrer votre choix parmi feuille/pierre/ciseaux").upper() ##accept all type of letters
    FPC = ['FEUILLE', 'PIERRE', 'CISEAUX']
    while ch not in FPC:  ##verify that the choice is OK
        print("erreur choix non valide")
        ch = input("entrer votre choix parmi feuille/pierre/ciseaux").upper() ##ask the choice again
    if ch in FPC:
        print("le choix du joueur est".center(40), ch.center(40))
    return ch

def CHOIXPC():
    import random
    FPC = ['FEUILLE', 'PIERRE', 'CISEAUX']
    rch=random.choice(FPC)#the computer choice
    print("le choix de l'ordinateur est".center(40), rch.center(40))#present the computer choice to the player
    return rch


def ATTRIBUE():
    scor_pl= 0
    scor_comp= 0
    while scor_pl!=3 and scor_comp!=3:##repeat the game until one of the computer or the player has 3 point
        player_c=CHOIX()
        computer_c=CHOIXPC()
        player_win=[('PIERRE','CISEAUX'), ('FEUILLE','PIERRE'), ('CISEAUX', 'FEUILLE')] ##a list that the player win
        computer_win=[('PIERRE','FEUILLE'), ('FEUILLE','CISEAUX'), ('CISEAUX', 'PIERRE')] ##a list yhet the computer win
        if player_c==computer_c:#if have the same choice 0point added for both
            scor_pl+=0
            scor_comp+=0
            print("vous avez fait le meme choix que la machine vos scores")
        elif (player_c, computer_c) in player_win:
            scor_pl+=1
            scor_comp+=0
        elif (player_c, computer_c) in computer_win :
            scor_pl+=0
            scor_comp+=1
        print("**************************************************************************")
        print("le score du joueur est".center(40),scor_pl)
        print("le score de la machine est".center(40), scor_comp)
        print("**************************************************************************")
    if scor_pl==3:
        print("la partie est finie, œœœœœœœœœœœœœœœœœœœœœœ vous avez gagné œœœœœœœœœœœœœœœœœœœœœœœ".center(20))
    elif scor_comp==3:
        print("la partie est finie, ::(:(:(::(:(:(:(:(:vous avez perdu:(:(:(:(:(:(:(:(:".center(20))
    return (scor_pl, scor_comp)


def PLAYAGAIN():
    pl = input("voulez vous jouer de nouveau? taper oui ou non").upper()#accept oui/non
    tag=["OUI", "NON"]
    while pl not in tag:#if input different =error
        print("erreur de saisie taper oui ou non")
        pl = input("entrer votre réponce de nouveau").upper()
    if pl=="NON":
        print("Merci Aurevoir".center(50))
    elif pl=="OUI":
        print("les scores sont remis à zéros".center(50))
    return pl

#the main code body

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