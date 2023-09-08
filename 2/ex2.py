# J'ai créer plusieurs versions de fonction pour la même question lorsque je me rend compte que la méthode adopté n'est pas la bonne (quand je complique les choses ou quand je ne respecte pas des conventions etc.)

# NOTES PERSO 
#len() -> renvoie le nombre d'élement donc si le tableau son dernier élémement à pour index 19 il renvoie 20.

# CONST 
TEST_LISTE = [1,23, 23, 35,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
TEST_LISTE2 = [1,2,3]

def position_v1(lst : list ,elt : int) -> int :
    result = -1
    for k in range(len(lst)):
        if elt == lst[k] : 
            result = k 
    return result 

# cette version parcours toute la liste
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
         
# Fonctione mais n'est pas propre (condition pour rien + trop compliqué)
def est_triee(lst) -> bool : 
    trier = False 
    for k in range(0, len(lst)-1):
        if lst[k+1] >= lst[k] and lst[-1] >= lst[-2] : 
            trier = True 
        else : 
            return False
    return trier

# version (une condition en moins et plus lisible) (éviter erreur k+1 quand on arrive à la dernière itéraction )
def est_triee_v2(lst) -> bool : 
    last = lst[0]
    for k in range(1, len(lst)) : 
        if last >= lst[k] : 
            return False
        last = lst[k]
    return True 

# version plus optimisé : dans la version v2 la variable last garde en mémoire k-1, mais on peut accéder à k-1, pas besoin de créer une variable
def est_triee_v3(lst) -> bool : 
    for k in range(1, len(lst)) : 
        if lst[k-1] >= lst[k] : 
            return False
    return True
 
def est_triee_with_while(lst) -> bool : 
    i = 1
    while i <len(lst) and lst[i-1]<= lst[i] : 
        i += 1
    if i == len(lst) : 
        return True
    else : 
        return False