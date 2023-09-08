# CONST 
TEST_LISTE = [1,23, 23, 35,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
TEST_LISTE2 = [1,2,3,4, 1]

def position_v1(lst : list ,elt : int) -> int :
    result = -1
    for k in range(len(lst)):
        if elt == lst[k] : 
            result = k 
    return result 

# cette version parcour toute la liste
def position_v2(lst : list ,elt : int) -> int :
    result = -1
    counter = 0 
    while counter < len(lst) : 
        if (lst[counter] == elt) : 
            result = counter
        counter += 1
    return result

# cette version s'arrête lorsqu'elle trouve 
# len() -> renvoie le nombre d'élement donc si le tableau son dernir élémement à pour index 19 il renvoie 20.
def position_v2_2(lst : list ,elt : int) -> int :
    counter = 0
    while counter <len(lst) and lst[counter] != elt : 
        counter += 1
    if counter == len(lst) : 
        return -1
    else : 
        return counter

def nb_occurrences(lst : list ,e : int ) -> int :
    result = 0
    for l in lst : 
        if l == e : 
            result += 1
    return result
         
# Fonctione mais n'est pas propre    
def est_triee(lst) -> bool : 
    trier = False 
    for k in range(0, len(lst)-1):
        if lst[k+1] >= lst[k] and lst[-1] >= lst[-2] : 
            trier = True 
        else : 
            return False
    return trier

# version plus optimisé 
def est_triee_v2(lst) -> bool : 
    trier = True 
    plus_petit = lst[0]
    for k in range(1, len(lst)) : 
        print()
        if plus_petit >= lst[k] : 
            return False
        plus_petit = lst[k]
    return trier 
          
print(est_triee_v2(TEST_LISTE2))