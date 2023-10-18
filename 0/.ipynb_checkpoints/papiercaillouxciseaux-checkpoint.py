from random import randint 

# init variables
input_init = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " ).upper()

score_player1= 0
score_player2 = 0

round_count= 0
gameActive = False

items_game = ['pierre', 'papier', 'ciseaux', 'puit']

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
        

# game loop
while gameActive== True:
    
    round_count+= 1 
    
    player_choice = input(f"{player} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ").lower()
    
    # loop to check if player choice is correct
    if player_choice not in items_game:
                player_choiceok = False
                print("Je n'ai pas compris votre réponse")
                
                while player_choiceok == False :
                    print("Joueur ", player)
                    player_choice = input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ").lower()
                    if player_choice in items_game: 
                        player_choiceok = True
    # choice of the machine
    if input_init == 'O': 
       player2_choice = ['papier','pierre','ciseaux'][randint(0, 2)]

    # choice of the second player
    if input_init == 'N':
        print("Joueur", player2)
        player2_choice= input("faîtes votre choix parmi (pierre, papier, ciseaux, puit): ").lower()
        
        # loop to check if player2 choice is correct
        if player2_choice not in items_game:
                    player2_choiceok = False
                    print("Je n'ai pas compris votre réponse")
                    while player2_choiceok == False:
                        print("Joueur ", player2)
                        player2_choice= input(" faîtes votre choix parmi (pierre, papier, ciseaux, puit): ")
                        if player2_choice in items_game: 
                            player2_choiceok = True
                                    

    # show choices
    print("Si on récapitule :",player, player_choice, "et", player2, player_choice,"\n")

    # dict to check who win
    gagnants = {
    ('pierre', 'pierre'): "aucun de vous, vous êtes exequo",
    ('pierre', 'ciseaux'): player,
    ('pierre', 'papier'): player2,
    ('papier', 'pierre'): player,
    ('papier', 'ciseaux'): player2,
    ('papier', 'papier'): "aucun de vous, vous êtes exequo",
    ('ciseaux', 'pierre'): player2,
    ('ciseaux', 'ciseaux'): "aucun de vous, vous êtes exequo",
    ('ciseaux', 'papier'): player,
    ('puit', 'pierre'): player,
    ('pierre', 'puit'): player2,
    ('puit', 'ciseaux'): player,
    ('ciseaux', 'puit'): player2,
    ('puit', 'papier'): player2,
    ('papier', 'puit'): player,
    ('puit', 'puit'): "aucun de vous, vous êtes exequo"
}
    
    # determine the winner using the dict
    winner = gagnants[(player_choice, player2_choice)]
    
    print(" -> ", player_choice, player2_choice)
    print(f"{winner} a gagné cette manche ! \n")
    
    # determine the score
    if winner == player:
        score_player1 += 1
    elif winner == player2:
        score_player2 += 1
        
    print(f"Le score est de {score_player1} pour {player} et {score_player2} pour {player2} \n")    
   
    # STOP GAME 
    if round_count==5:
        gameActive= False
        
    # RESTART ROUND
    if round_count<5:
        input_init = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(player,player2)).upper()
        # loop to check if player choice is correct
        if input_init == 'O':
            gameActive= True
        if input_init == 'N':
            gameActive= False
        if input_init != 'O' and input_init != 'N':
            gameActive= True
            print("Vous ne répondez pas à la question, on continue ")
        
print("Merci d'avoir joué ! A bientôt")