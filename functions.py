import random
def presentation():
    name=input("entrer votre nom")
    while len(name)<2: #oblige the player to give a real name with at least 2 letters
        print("erreur renter votre nom de minimum 2 lettres")
        name = input("entrer votre nom")
    else:
        print("nom du joueur=".center(50), name.upper().center(50))

def choice_player():
    his_choice = input("entrer votre choix parmi feuille/pierre/ciseaux").upper() ##accept all type of letters
    choices_list = ['FEUILLE', 'PIERRE', 'CISEAUX']
    while his_choice not in choices_list:  ##verify that the choice is OK
        print("erreur choix non valide")
        his_choice = input("entrer votre choix parmi feuille/pierre/ciseaux").upper() ##ask the choice again
    if his_choice in choices_list:
        print("le choix du joueur est".center(40), his_choice.center(40))
    return his_choice

def choice_pc():
    choices_list= ['FEUILLE', 'PIERRE', 'CISEAUX']
    rand_choice=random.choice(choices_list)#the computer choice
    print("le choix de l'ordinateur est".center(40), rand_choice.center(40))#present the computer choice to the player
    return rand_choice

def game():
    scor_player= 0
    scor_computer= 0
    while scor_player!=3 and scor_computer!=3:##repeat the game until one of the computer or the player has 3 point
        player_c=choice_player()
        computer_c=choice_pc()
        player_win=[('PIERRE','CISEAUX'), ('FEUILLE','PIERRE'), ('CISEAUX', 'FEUILLE')] ##a list that the player win
        computer_win=[('PIERRE','FEUILLE'), ('FEUILLE','CISEAUX'), ('CISEAUX', 'PIERRE')] ##a list yhet the computer win
        if player_c==computer_c:#if have the same choice 0point added for both
            print("vous avez fait le meme choix que la machine vos scores")
        elif (player_c, computer_c) in player_win:
            scor_player+=1
        elif (player_c, computer_c) in computer_win :
            scor_computer+=1
        print("**************************************************************************")
        print("le score du joueur est".center(40),scor_player)
        print("le score de la machine est".center(40), scor_computer)
        print("**************************************************************************")
    if scor_player==3:
        print("œœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœ")
        print("la partie est finie, œœœœœœœœœœœœœœœœœœœœœœ vous avez gagné œœœœœœœœœœœœœœœœœœœœœœœ".center(20))
        print("œœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœœ")
        play_again()
    elif scor_computer==3:
        print("dommage dommage dommage dommage dommage dommage dommagedommage dommage dommage dommage dommage")
        print("la partie est finie, ::(:(:(::(:(:(:(:(:vous avez perdu:(:(:(:(:(:(:(:(:".center(20))
        play_again()


def play_again():
    answer = input("voulez vous jouer de nouveau? taper oui ou non").upper()#accept oui/non
    tag=["OUI", "NON"]
    while answer not in tag:#if input different =error
        print("erreur de saisie taper oui ou non")
        answer = input("entrer votre réponce de nouveau").upper()
    if answer=="OUI":
        print("les scores sont remis à zéros".center(50))
        game()
    if answer=="NON":
        print("Merci Aurevoir".center(50))
