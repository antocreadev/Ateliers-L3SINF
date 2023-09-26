import random
# const
lst =["paris","londres","madrid","berlin","new-york"] 
lst_len = len(lst) 

draw_errors = [["|---] ", "|   ", "|  ","|    "],
               ["|---] ", "| O ", "|  ","|    "],
               ["|---] ", "| O ", "| | ","|    "],
               ["|---] ", "| O ", "| T ","|    "],
               ["|---] ", "| O ", "| T ","|/   "],
               ["|---] ", "| O ", "| T ","|/ \ "] ]

def places_lettre(ch: str, mot: str) -> list:
    """
    Retourne une liste des positions (indices) où la lettre 'ch' apparaît dans le mot 'mot'.

    :param ch: La lettre à rechercher.
    :type ch: str
    :param mot: Le mot dans lequel rechercher la lettre.
    :type mot: str
    :return: Liste des positions (indices) où 'ch' apparaît dans 'mot'.
    :rtype: list
    """
    result = []
    for k in range(len(mot)) : 
        if mot[k] == ch : 
            result.append(k)
    return result

def test():
    """
    Fonction de test pour la fonction 'places_lettre'.
    Affiche les résultats attendus et les résultats obtenus pour quelques exemples.
    """
    print(f"input attendu : [0] ; input obtenu : {places_lettre('b', 'bonjour')}")
    print(f"input attendu : [] ; input obtenu : {places_lettre('a', 'bonjour')}")
    print(f"input attendu : [0, 2] ; input obtenu : {places_lettre('m', 'maman')}")

def outputStr(mot: str, lpos: list) -> str:
    """
    Affiche le mot 'mot' en remplaçant les lettres aux positions spécifiées dans 'lpos' par des tirets (-).

    :param mot: Le mot à afficher.
    :type mot: str
    :param lpos: Liste des positions (indices) des lettres à conserver.
    :type lpos: list
    """
    longueur = len(mot)
    result = ""
    for i in range(longueur):
        if i in lpos:
            result += (mot[i])
        else:
            result += "-"
    return result
            

# concat_outputStr(outputStr("bonjour", [0, 1]),outputStr("bonjour", places_lettre("o", "bonjour")) )

def runGame() : 
    error = 0
    # choice word in liste
    indice_word_random = random.randint(0, lst_len)
    word = lst[indice_word_random]
    
    concat_indice = []
    letter_find = []
    
    while error < 5 and len(letter_find) != len(word): 
        #choice word
        letter = input("choisi lettre : ")

        # si la lettre n'est pas dans le mot
        if places_lettre(letter, word) == [] : 
            error += 1
            for k in range(len(draw_errors[error])) : 
                print(draw_errors[error][k])
            print(outputStr(word, concat_indice))
            
        # la lettre est dans le motn mais il a déjà choisi
        elif letter in letter_find : 
            error += 1
            
        # la lettre est dans le mot il l'user de ne l'a pas encore choisi
        else :
            concat_indice += places_lettre(letter, word)
            letter_find.append(letter)
            
            for k in range(len(draw_errors[error])) : 
                print(draw_errors[error][k])
            print(outputStr(word, concat_indice))
            
    if error == 5 : 
        print('perdu')
    else  : 
        print('gagné')
            

            
runGame()
            
        
        