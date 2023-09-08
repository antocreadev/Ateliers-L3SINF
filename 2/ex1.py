# J'ai créer plusieurs versions de fonction pour la même question lorsque je me rend compte que la méthode adopté n'est pas la bonne (quand je complique les choses ou quand je ne respecte pas des conventions etc.)
# CONST 
# la liste doit être trié du plus petit au plus grand 
TEST_LISTE = [1,23,35,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# FINCTIONS
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
    if (len(L) == 0) : 
        return "pas de division par 0"
    return somme_v1(L) / len(L)

def nb_sup_v1 (L : list,e : int) ->  int: 
    """_summary_

    Args:
        L (list): _description_
        e (int): _description_

    Returns:
        int: _description_
    """
    result = 0 
    for k in range(len(L)) :
        if e < L[k] : 
            result += 1 
    return result

def nb_sup_v2 (L : list,e : float) -> int : 
    """

    Args:
        L (list): _description_
        e (float): _description_

    Returns:
        int: _description_
    """
    result = 0 
    for l in L :
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

def moy_sup_v2 (L : list,e : float) -> float :
    nombre_sup = nb_sup_v1(L, e)
    counter = 0
    for k in range(len(L)) :
        if L[k] > e : 
            counter += L[k]
    if counter == 0 : 
        return "pas de division par 0"
    return counter / nombre_sup

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
        # print(f"indice : {k}, value : {L[k]}")
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
    
    
    print("TEST moyenne") 
    #test liste vide 
    print("Test liste vide : ", moyenne([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", moyenne(lst2test1), "\n")
    
    print("TEST nb_sup_v1") 
    #test liste vide 
    print("Test liste vide : ", nb_sup_v1([],5)) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", nb_sup_v1(lst2test1,5), "\n")
    
    print("TEST nb_sup_v2") 
    #test liste vide 
    print("Test liste vide : ", nb_sup_v2([],5)) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", nb_sup_v2(lst2test1,5), "\n")
    
    print("TEST moy_sup") 
    #test liste vide 
    print("Test liste vide : ", moy_sup([],5)) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", moy_sup(lst2test1,5), "\n")
    
    print("TEST moy_sup_v2") 
    #test liste vide 
    print("Test liste vide : ", moy_sup_v2([],5)) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", moy_sup_v2(lst2test1,5), "\n")
    
    print("TEST val_max") 
    #test liste vide 
    print("Test liste vide : ", val_max([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", val_max(lst2test1), "\n")

    print("TEST ind_max") 
    #test liste vide 
    print("Test liste vide : ", ind_max([])) 
    #test somme 11111 
    lst2test1=[1,10,100, 1000,10000] 
    print("Test somme 1111 : ", ind_max(lst2test1), "\n")


test_exercice1()

