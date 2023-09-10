TEST_LISTE = [55,-8,66,0,66,0,-7, 0, 44, 39, 92 , -99, -9,88,0,0,0,11,-6]

def separation(lst : list)-> list:
    """
    Sépare les éléments d'une liste en trois groupes :
    
    1. Les éléments négatifs sont placés au début de la liste,
    2. Les zéros sont insérés juste après le dernier élément négatif
    3. Les éléments positifs sont placés à la fin de la liste

    Args:
    lst (list): La liste d'entiers à traiter.

    Returns:
    list: Une nouvelle liste avec les éléments réorganisés selon les règles ci-dessus.
    """
    LSEP = []
    counter = 0 # pour savoir le dernier nombre négatif ajouter
    for l in lst : 
        if l<0 : 
            LSEP = [l] + LSEP
            counter += 1
        elif l== 0 : 
            LSEP.insert(counter, l)
        else : 
            LSEP = LSEP + [l] 
    return LSEP
        
        

separation(TEST_LISTE)