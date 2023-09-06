import random

# init variables
input_init = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ).upper()

score_player1= 0
score_player2 = 0

round_count= 0
gameActive = False

# init players
if input_init != 'O' and input_init != 'N' :
    print("Je n'ai pas compris votre réponse")
    
else : 
    player = input("Quel est votre nom ? ")
    gameActive= True
    if input_init == 'O':
        print("Bienvenu ",player, " nous allons jouer ensemble \n")
        player2 = 'Machine'
    else :
        print("Bienvenu ",player, " nous allons jouer ensemble")
        player2 = input("Quel est le nom du deuxième joueur ?")
        print("Bienvenu ",player2, " nous allons jouer ensemble \n")
        


while gameActive== True:
    
    round_count+= 1 
    
    player_choice = input(f"{player} faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
    
    if player_choice != 'pierre' and player_choice != 'papier' and player_choice != 'ciseaux' :
                player_choiceok = False
                print("Je n'ai pas compris votre réponse")
                
                while player_choiceok == False :
                    print("Joueur ", player)
                    player_choice = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
                    player_choiceok = True
                    if player_choice != 'pierre' and player_choice != 'papier' and player_choice != 'ciseaux': 
                        player_choiceok = False

    if input_init == 'O': 
       machine_choice= ['papier','pierre','ciseaux'][random.randint(0, 2)]

    if input_init == 'N':
        print("Joueur", player2)
        player2_choice= input("faîtes votre choix parmi (pierre, papier, ciseaux): ").lower()
        if machine_choice!= 'pierre':
            if machine_choice!= 'papier':
                if machine_choice!= 'ciseaux':
                    j2bon = False
                    print("Je n'ai pas compris votre réponse")
                    while not j2bon :
                        print("Joueur ", player2)
                        machine_choice= input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
                        j2bon = True
                        if machine_choice!= 'pierre': 
                            if machine_choice!= 'papier':
                                if machine_choice!= 'ciseaux':
                                    j2bon = False

    #On affiche les choix de chacun
    print("Si on récapitule :",player, player_choice, "et", player2, machine_choice,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if player_choice == 'papier' and machine_choice== 'papier' :
        winner = "aucun de vous, vous être exequo"
        score_player1= score_player1+ 0
        score_player2 = score_player2 + 0
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'pierre' and machine_choice== 'papier' :
        winner = player2
        score_player1= score_player1+ 0
        score_player2 = score_player2 + 1
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'pierre' and machine_choice== 'pierre' :
        winner = "aucun de vous, vous être ex æquo"
        score_player1= score_player1+ 0
        score_player2 = score_player2 + 0
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'pierre' and machine_choice== 'ciseaux' :
        winner = player
        score_player1= score_player1+ 1
        score_player2 = score_player2 + 0
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'papier' and machine_choice== 'ciseaux' :
        winner = player2
        score_player1= score_player1+ 0
        score_player2 = score_player2 + 1
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'papier' and machine_choice== 'pierre' :
        winner = player
        score_player1= score_player1+ 1
        score_player2 = score_player2 + 0
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'ciseaux' and machine_choice== 'pierre' :
        winner = player2
        score_player1= score_player1+ 0
        score_player2 = score_player2 + 1
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'ciseaux' and machine_choice== 'ciseaux' :
        winner = "aucun de vous, vous être ex æquo"
        score_player1= score_player1+ 0
        score_player2 = score_player2 + 0
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if player_choice == 'ciseaux' and machine_choice== 'papier' :
        winner = player
        score_player1= score_player1+ 1
        score_player2 = score_player2 + 0
        print("le gagnant est",winner)
        print("Les scores à l'issue de cette manche sont donc",player, score_player1, "et", player2, score_player2, "\n")

    if round_count==1 or round_count==2 or round_count==3 or round_count==4:
        gameActive= True
    if round_count==5:
        gameActive= False
        
    if round_count==1 or round_count==2 or round_count==3 or round_count==4:
        #On propose de gameActiveou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(player,player2))
        if go == 'O':
            gameActive= True
        if go == 'N':
            gameActive= False
        if go != 'O' and go != 'N':
            gameActive= True
            print("Vous ne répondez pas à la question, on continue ")
        
print("Merci d'avoir joué ! A bientôt")