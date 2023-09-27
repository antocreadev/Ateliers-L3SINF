# const 
LISTE = [1,2,3,4,5,6]
LISTE2 = [[0,1,2], [1,2,3], [5,6,9]]

# Algorithme récursif

# SOMME 
def somme(lst : list) -> int: 
    if lst == [] : 
        return 0
    else :
        return lst[0] + somme(lst[1:])
# print(somme(LISTE))
# 1 (vide la liste (somme(lst[1:])) : 
    # >> [1,2,3,4,5,6]
    # >> [2,3,4,5,6]
    # >> [3,4,5,6]
    # >> [4,5,6]
    # >> [5,6]
    # >> [6]
    # >> []
        # 2 la liste est vide 
            # >> 0 
            # 3 Dépilation 
                # >> 6
                # >> 11
                # >> 15
                # >> 18 
                # >> 20 
                # >> 21 

# print(factorielle_recursive(3))

def longueur(lst : list)-> int : 
    if lst == [] :
        return 0
    else : 
        return 1 + longueur(lst[1:])
# print(longueur(LISTE))

def findMax(lst: list) -> int : 
    if lst == [] : 
        return 0
    if len(lst) == 1 : 
        return lst[0] 
    else : 
        if lst[0] > findMax(lst[1:]) :
            return lst[0] + findMax(lst[1:])
        else : 
            return findMax(lst[1:])
# print(findMax(LISTE))

def listPairs(lst: list) -> list : 
    if lst == [] : 
        return lst
    else : 
        if lst[0] %2 == 0 :
            return [lst[0]] + listPairs(lst[1:]) 
        else : 
            return listPairs(lst[1:]) 
            
# print(listPairs(LISTE))

def concat_list(llst : list) -> list : 
    if llst == [] : 
        return []
    else : 
        return llst[0] + concat_list(llst[1:])
    
print(concat_list(LISTE2))

def separe(lst : list) -> tuple : 
    if lst == [] : 
        return ([],[])
    else : 
        pile = separe(lst[1:])
        if lst[0] % 2 == 0 : 
            pile[1].append(lst[0])
        else :
            pile[0].append(lst[0])
        return pile
print(separe(LISTE))
