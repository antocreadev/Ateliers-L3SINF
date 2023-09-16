def  places_lettre(ch : str, mot : str) -> list : 
    return [l for l in range(len(mot)) if mot[l]== ch]

def test() : 
    print(f"input à avoir : [0] ; input de la fonction testé : {places_lettre('b', 'bonjour')}")
    print(f"input à avoir : [] ; input de la fonction testé : {places_lettre('a', 'bonjour')}")
    print(f"input à avoir : [0,2] ; input de la fonction testé : {places_lettre('m', 'maman')}")
    
test()

def outputStr(mot:str, lpos:list)-> str: 
    longueur = len(mot)
    print(lpos)
    for i in range(len(mot)) : 
        if i in lpos : 
            print(mot[i], end="")
        else : 
            print("-", end="")
    

outputStr("bonjour", places_lettre("b", "bonjour"))


def runGame() : 