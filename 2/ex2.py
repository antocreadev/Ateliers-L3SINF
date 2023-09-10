# J'ai créer plusieurs versions de fonction pour la même question lorsque je me rend compte que la méthode adopté n'est pas la bonne (quand je complique les choses, quand je ne respecte pas des conventions etc.)

# NOTES PERSO 
#len() -> renvoie le nombre d'élement donc si le tableau son dernier élémement à pour index 19 il renvoie 20.

# CONST 
TEST_LISTE = [1,23, 23, 35,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
TEST_LISTE2 = [1, 2, 8, 12, 34, 44, 55, 101]
def position_v1(lst : list ,elt : int) -> int :
    """
    Trouve la position de la dernière occurrence d'un élément dans une liste.

    Args:
        lst (list): La liste dans laquelle rechercher.
        elt (int): L'élément dont on veut trouver la position.

    Returns:
        int: La position de la dernière occurrence de l'élément dans la liste, ou -1 s'il n'est pas présent.

    Examples:
        >>> position_v1([1, 2, 3, 4, 5, 2, 3], 2)
        5
        >>> position_v1([5, 4, 3, 2, 1], 6)
        -1
    """
    result = -1
    for k in range(len(lst)):
        if elt == lst[k] : 
            result = k 
    return result 

# cette version parcours toute la liste
def position_v2(lst : list ,elt : int) -> int :
    """
    Trouve la position de la dernière occurrence d'un élément dans une liste.

    Args:
        lst (list): La liste dans laquelle rechercher.
        elt (int): L'élément dont on veut trouver la position.

    Returns:
        int: La position de la dernière occurrence de l'élément dans la liste, ou -1 s'il n'est pas présent.

    Examples:
        >>> position_v2([1, 2, 3, 4, 5, 2, 3], 2)
        5
        >>> position_v2([5, 4, 3, 2, 1], 6)
        -1
    """
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
    """
    Trouve la position de la première occurrence d'un élément dans une liste.

    Args:
        lst (list): La liste dans laquelle rechercher.
        elt (int): L'élément dont on veut trouver la position.

    Returns:
        int: La position de la première occurrence de l'élément dans la liste, ou -1 s'il n'est pas présent.

    Examples:
        >>> position_v2_2([1, 2, 3, 4, 5], 3)
        2
        >>> position_v2_2([5, 4, 3, 2, 1], 6)
        -1
    """
    counter = 0
    while counter <len(lst) and lst[counter] != elt : 
        counter += 1
    if counter == len(lst) : 
        return -1
    else : 
        return counter

def nb_occurrences(lst : list ,e : int ) -> int :
    """
    Compte le nombre d'occurrences d'un élément donné dans une liste.

    Args:
        lst (list): La liste dans laquelle rechercher.
        e (int): L'élément à compter dans la liste.

    Returns:
        int: Le nombre d'occurrences de l'élément dans la liste.

    Examples:
        >>> nb_occurrences([1, 2, 2, 3, 4, 2], 2)
        3
        >>> nb_occurrences([5, 5, 5, 5, 5], 3)
        0
    """
    result = 0
    for l in lst : 
        if l == e : 
            result += 1
    return result
         
# Fonctione mais n'est pas propre (condition pour rien + trop compliqué)
def est_triee(lst) -> bool : 
    """
    Vérifie si une liste est triée de manière croissante.

    Args:
        lst (list): La liste à vérifier.

    Returns:
        bool: True si la liste est triée de manière croissante, False sinon.

    Examples:
        >>> est_triee([1, 2, 3, 4, 5])
        True
        >>> est_triee([5, 4, 3, 2, 1])
        False
    """
    trier = False 
    for k in range(0, len(lst)-1):
        if lst[k+1] >= lst[k] and lst[-1] >= lst[-2] : 
            trier = True 
        else : 
            return False
    return trier

# version (une condition en moins et plus lisible) (éviter erreur k+1 quand on arrive à la dernière itéraction )
def est_triee_v2(lst) -> bool : 
    """
    Vérifie si une liste est triée de manière croissante.

    Args:
        lst (list): La liste à vérifier.

    Returns:
        bool: True si la liste est triée de manière croissante, False sinon.

    Examples:
        >>> est_triee_v2([1, 2, 3, 4, 5])
        True
        >>> est_triee_v2([5, 4, 3, 2, 1])
        False
    """
    last = lst[0]
    for k in range(1, len(lst)) : 
        if last >= lst[k] : 
            return False
        last = lst[k]
    return True 

# version plus optimisé : dans la version v2 la variable last garde en mémoire k-1, mais on peut accéder à k-1, pas besoin de créer une variable
def est_triee_v3(lst) -> bool : 
    """
    Vérifie si une liste est triée de manière croissante.

    Args:
        lst (list): La liste à vérifier.

    Returns:
        bool: True si la liste est triée de manière croissante, False sinon.

    Examples:
        >>> est_triee_v3([1, 2, 3, 4, 5])
        True
        >>> est_triee_v3([5, 4, 3, 2, 1])
        False
    """
    for k in range(1, len(lst)) : 
        if lst[k-1] >= lst[k] : 
            return False
    return True

def est_triee_with_while(lst) -> bool : 
    """
    Vérifie si une liste est triée de manière croissante.

    Args:
        lst (list): La liste à vérifier.

    Returns:
        bool: True si la liste est triée de manière croissante, False sinon.

    Examples:
        >>> est_triee_with_while([1, 2, 3, 4, 5])
        True
        >>> est_triee_with_while([5, 4, 3, 2, 1])
        False
    """
    i = 1
    while i <len(lst) and lst[i-1]<= lst[i] : 
        i += 1
    if i == len(lst) : 
        return True
    else : 
        return False

# la version avec la boucle for est plus visible et a moins de variable

# Fonction qui n'est pas demander dans l'Atelier (recherche dichotomique(binaire) -> renvoie l'index de l'élément trouvé sinon -1
def recherche_dichotomique(lst : list,e : int, compteur : int=0 ) -> int:
    """
    Effectue une recherche dichotomique récursive d'un élément dans une liste triée.

    Args:
        lst (list): La liste triée dans laquelle effectuer la recherche.
        e (int): L'élément à rechercher dans la liste.
        compteur (int, optional): Un compteur utilisé pour suivre l'index dans la liste d'origine (par défaut 0).

    Returns:
        int: L'indice de l'élément recherché dans la liste d'origine, -1 s'il n'est pas trouvé.

    Note:
        La fonction recherche un élément dans une liste triée en divisant la liste en deux à chaque
        étape, puis en comparant l'élément avec l'élément central. Si l'élément est trouvé, la fonction
        renvoie son indice dans la liste d'origine. Sinon, elle continue la recherche dans la moitié
        appropriée de la liste jusqu'à ce que l'élément soit trouvé ou que la liste soit épuisée.

    Exemple:
        >>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> recherche_dichotomique(lst, 5)
        4
        >>> recherche_dichotomique(lst, 10)
        -1
    """
    # si la liste est vide
    if not lst:
        return -1
    m = len(lst)//2
    mid_element = lst[m]
    
    # si l'élément est celui du milieu 
    if e == mid_element:
        return m + compteur
    # si le dernier élément ne correspond pas
    if len(lst) == 1:
        return -1
    
    # si l'élément recherché est plus petit que l'élément du milieu donc l'élément est à gauche
    if e < mid_element:
        return recherche_dichotomique(lst[:m], e, compteur)
    # si l'élément recherché est plus grand que l'élément du milieu donc l'élément est à droite
    if e > mid_element:
        return recherche_dichotomique(lst[m:], e , compteur + m)


def position_tri_exo2_q4(lst : list,e :int) -> int : 
    """
    Recherche la position de l'élément 'e' dans la liste triée 'lst'.

    Args:
    lst (list): Une liste triée de manière ascendante.
    e (int): L'élément que l'on souhaite trouver dans la liste.

    Returns:
    int: La position de 'e' dans la liste 'lst'. Si 'e' n'est pas présent, renvoie -1.

    Note:
    La fonction utilise une recherche binaire pour optimiser la recherche dans la liste triée.
    Elle commence par comparer 'e' à l'élément médian de la liste, puis réduit la plage de recherche
    de manière itérative jusqu'à ce que l'élément soit trouvé ou que la plage de recherche devienne vide.

    Exemple:
    >>> lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> position_tri_exo2_q4(lst, 5)
    4  # '5' est à la position 4 dans la liste 'lst'
    
    >>> position_tri_exo2_q4(lst, 10)
    -1  # '10' n'est pas dans la liste 'lst', donc renvoie -1.
    """
    compteur = 0
    while e != lst[len(lst)//2]: 
        taille_lst = len(lst)
        m = taille_lst//2
        mid_element = lst[m]
        if taille_lst == 1 : 
            return -1
        if e < mid_element : 
            lst =lst[:m]
        if e > mid_element: 
            lst = lst[m:]
            compteur += m
    return compteur + m//2


def a_repetitions(lst : list) -> bool :
    """
    Vérifie s'il y a des éléments répétés dans la liste 'lst'.

    Args:
    lst (list): Une liste d'éléments à vérifier.

    Returns:
    bool: True si la liste contient au moins un élément répété, False sinon.

    Note:
    La fonction parcourt la liste 'lst' en maintenant une liste auxiliaire 'T' pour suivre
    les éléments déjà rencontrés. Si un élément est rencontré pour la deuxième fois,
    la fonction renvoie True, indiquant la présence d'éléments répétés. Sinon, elle parcourt
    toute la liste et renvoie False si aucun élément n'est répété.

    Exemple:
    >>> a_repetitions([1, 2, 3, 4, 5])
    False  # Aucun élément n'est répété.

    >>> a_repetitions([1, 2, 3, 2, 4, 5])
    True  # L'élément '2' est répété dans la liste.
    """
    T = []
    counter = 0 
    while counter < len(lst) :
        if lst[counter] not in  T : 
            T.append(lst[counter])
        else : 
            return True
        counter += 1
    return False