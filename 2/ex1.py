# la liste doit être trié du plus petit au plus grand 
TEST_LISTE = [1,23,35,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def somme_v1(L : list) -> float : 
    """_summary_

    Args:
        L (list): _description_

    Returns:
        float: _description_
    """
    result = 0
    for k in range(len(L)) : 
        result += L[k]
    return result

def somme_v2(L : list) -> float : 
    """_summary_

    Args:
        L (list): _description_

    Returns:
        float: _description_
    """
    result = 0
    for e in L :
        result += e
    return result

def somme_v3(L : list) -> float : 
    """_summary_

    Args:
        L (list): _description_

    Returns:
        float: _description_
    """
    result = 0
    counter = 0
    while counter < len(L) : 
        result += L[counter]
        counter += 1
    return result


# la version la plus adapté est la version avec la boucle for car on connait le nombre d'iteration

def  moyenne(L : list) -> float : 
    """_summary_

    Args:
        L (list): _description_

    Returns:
        float: _description_
    """
    return somme_v1(L) / len(L)

def nb_sup_v1 (L : list,e : float) -> float : 
    """_summary_

    Args:
        L (list): _description_
        e (float): _description_

    Returns:
        float: _description_
    """
    result = 0 
    for k in range(len(L)) :
        # print(L[k], e)
        if e < L[k] : 
            result += 1 
    return result

def nb_sup_v2 (L : list,e : float) -> int : 
    """retourne la moyenne des valeurs de la liste strictement supérieures à e.

    Args:
        L (list): _description_
        e (float): _description_

    Returns:
        int: _description_
    """
    result = 0 
    for l in L :
        # print(L[k], e)
        if e < l : 
            result += 1 
    return result


def moy_sup (L : list,e : float) -> float :
    liste_nombre_sup = []
    for k in range(len(L)) :
        # print(L[k], e)
        if e < L[k] : 
            liste_nombre_sup.append(L[k]) 
    return moyenne(liste_nombre_sup)

def val_max(L : list ) -> float  : 
    value_max = 0
    for k in range(len(L)) :
        # print(L[k], e)
        if value_max < L[k] : 
            value_max = L[k]
    return value_max

def ind_max(L : list ) -> int : 
    value_indice = 0 
    value_max = val_max(L)
    # print(f"max : {value_max} ")
    for k in range(len(L)) : 
        print(f"indice : {k}, value : {L[k]}")
        if L[k] == value_max : 
            value_indice = k 
    return value_indice


# --- TEST ---
def test_exercice1 (): 
    print("TEST SOMME V1") 
    #test liste vide 
    print("Test liste vide : ", somme_v1([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", somme_v1(lst2test1), "\n")
    
    print("TEST SOMME V2") 
    #test liste vide 
    print("Test liste vide : ", somme_v2([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", somme_v2(lst2test1), "\n")
    
    
    print("TEST SOMME V3") 
    #test liste vide 
    print("Test liste vide : ", somme_v3([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", somme_v3(lst2test1), "\n")

# test_exercice1()

