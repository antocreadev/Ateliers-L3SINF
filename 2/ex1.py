# J'ai créer plusieurs versions de fonction pour la même question lorsque je me rend compte que la méthode adopté n'est pas la bonne (quand je complique les choses, quand je ne respecte pas des conventions etc.)
# CONST 
TEST_LISTE = [1,23,35,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# FINCTIONS
def somme_v1(L : list) -> float : 
    """
    Calcule la somme des éléments d'une liste.

    Args:
        L (list): La liste contenant les éléments à additionner.

    Returns:
        float: La somme des éléments de la liste.

    Examples:
        >>> somme_v1([1, 2, 3, 4, 5])
        15.0
        >>> somme_v1([0.5, 1.5, 2.5])
        4.5
    """
    result = 0
    for k in range(len(L)) : 
        result += L[k]
    return result

def somme_v2(L : list) -> float : 
    """
    Calcule la somme des éléments d'une liste.

    Args:
        L (list): La liste contenant les éléments à additionner.

    Returns:
        float: La somme des éléments de la liste.

    Examples:
        >>> somme_v2([1, 2, 3, 4, 5])
        15.0
        >>> somme_v2([0.5, 1.5, 2.5])
        4.5
    """
    result = 0
    for e in L :
        result += e
    return result

def somme_v3(L : list) -> float : 
    """
    Calcule la somme des éléments d'une liste.

    Args:
        L (list): La liste contenant les éléments à additionner.

    Returns:
        float: La somme des éléments de la liste.

    Examples:
        >>> somme_v3([1, 2, 3, 4, 5])
        15.0
        >>> somme_v3([0.5, 1.5, 2.5])
        4.5
    """
    result = 0
    counter = 0
    while counter < len(L) : 
        result += L[counter]
        counter += 1
    return result


# la version la plus adapté est la version avec la boucle for car on connait le nombre d'iteration

def  moyenne(L : list) -> float : 
    """
    Calcule la moyenne des éléments d'une liste.

    Args:
        L (list): La liste contenant les éléments pour calculer la moyenne.

    Returns:
        float: La moyenne des éléments de la liste, ou un message d'erreur si la liste est vide.

    Examples:
        >>> moyenne([1, 2, 3, 4, 5])
        3.0
        >>> moyenne([])
        "La liste est vide, impossible de calculer la moyenne."
    """
    if (len(L) == 0) : 
        return "pas de division par 0"
    return somme_v1(L) / len(L)

def nb_sup_v1 (L : list,e : int) ->  int: 
    """
    Compte le nombre d'éléments supérieurs à une valeur donnée dans une liste.

    Args:
        L (list): La liste contenant les éléments à comparer.
        e (int): La valeur de référence pour la comparaison.

    Returns:
        int: Le nombre d'éléments dans la liste qui sont supérieurs à la valeur de référence.

    Examples:
        >>> nb_sup_v1([1, 2, 3, 4, 5], 3)
        2
        >>> nb_sup_v1([0.5, 1.5, 2.5], 2)
        1
    """
    result = 0 
    for k in range(len(L)) :
        if e < L[k] : 
            result += 1 
    return result

def nb_sup_v2 (L : list,e : float) -> int : 
    """
    Compte le nombre d'éléments supérieurs à une valeur donnée dans une liste.

    Args:
        L (list): La liste contenant les éléments à comparer.
        e (float): La valeur de référence pour la comparaison.

    Returns:
        int: Le nombre d'éléments dans la liste qui sont supérieurs à la valeur de référence.

    Examples:
        >>> nb_sup_v2([1.5, 2.5, 3.5, 4.5, 5.5], 3.0)
        2
        >>> nb_sup_v2([0.5, 1.5, 2.5], 2.0)
        1
    """
    result = 0 
    for l in L :
        if e < l : 
            result += 1 
    return result


def moy_sup (L : list,e : float) -> float :
    """
    Calcule la moyenne des éléments supérieurs à une valeur donnée dans une liste.

    Args:
        L (list): La liste contenant les éléments à comparer.
        e (float): La valeur de référence pour la comparaison.

    Returns:
        float: La moyenne des éléments de la liste qui sont supérieurs à la valeur de référence, 
                ou 0.0 si aucun élément ne satisfait la condition.

    Examples:
        >>> moy_sup([1.5, 2.5, 3.5, 4.5, 5.5], 3.0)
        4.5
        >>> moy_sup([0.5, 1.5, 2.5], 2.0)
        0.0
    """
    liste_nombre_sup = []
    for k in range(len(L)) :
        # print(L[k], e)
        if e < L[k] : 
            liste_nombre_sup.append(L[k]) 
    return moyenne(liste_nombre_sup)

def moy_sup_v2 (L : list,e : float) -> float :
    """
    Calcule la moyenne des éléments supérieurs à une valeur donnée dans une liste.

    Args:
        L (list): La liste contenant les éléments à comparer.
        e (float): La valeur de référence pour la comparaison.

    Returns:
        float: La moyenne des éléments de la liste qui sont supérieurs à la valeur de référence, 
                ou un message d'erreur si aucun élément ne satisfait la condition.

    Examples:
        >>> moy_sup_v2([1.5, 2.5, 3.5, 4.5, 5.5], 3.0)
        4.5
        >>> moy_sup_v2([0.5, 1.5, 2.5], 2.0)
        "Aucun élément ne satisfait la condition."
    """
    nombre_sup = nb_sup_v1(L, e)
    counter = 0
    for k in range(len(L)) :
        if L[k] > e : 
            counter += L[k]
    if counter == 0 : 
        return "pas de division par 0"
    return counter / nombre_sup

def val_max(L : list ) -> float  : 
    """
    Trouve la valeur maximale dans une liste.

    Args:
        L (list): La liste contenant les éléments à comparer.

    Returns:
        float: La valeur maximale de la liste, ou 0.0 si la liste est vide.

    Examples:
        >>> val_max([1.5, 2.5, 3.5, 4.5, 5.5])
        5.5
        >>> val_max([])
        0.0
    """
    value_max = 0
    for k in range(len(L)) :
        # print(L[k], e)
        if value_max < L[k] : 
            value_max = L[k]
    return value_max

def ind_max(L : list ) -> int : 
    """
    Trouve l'indice de la première occurrence de la valeur maximale dans une liste.

    Args:
        L (list): La liste contenant les éléments à comparer.

    Returns:
        int: L'indice de la première occurrence de la valeur maximale dans la liste, 
                ou -1 si la liste est vide.

    Examples:
        >>> ind_max([1.5, 2.5, 3.5, 4.5, 5.5])
        4
        >>> ind_max([])
        -1
    """
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

