# CONST 
TEST_DATA = {
    (1, -5, 6), 
    (1, -5, 4),
    (1, 2, 5),
    (0, 2, 1)
}
def discriminant(a: float,b : float ,c : float ) -> float : 
    """ Calcul du discriminant d'une équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0)

    Args:
        a (float)
        b (float)
        c (float)

    Returns:
        float: discriminant
    """

    return b**2 - 4*a*c

def racine_unique(a : float,b : float) -> float : 
    """ Calcul de la racine unique d'une équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0)

    Args:
        a (float)
        b (float)
    Returns:
        float: racine unique
    """
    if a == 0 : 
        return "a ne doit pas être égale à 0"
    return -b / 2*a


def racine_double(a : float,b : float,delta : float ,num : int) :
    """ Calcul de la racine double d'une équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0)

    Args:
        a (float)
        b (float) 
        delta (float)
        num (int)

    Returns:
        _type_: racine double
    """

    if num == 1 : 
        return (-b + delta**0.5) / 2*a
    if num == 2 : 
        return (-b - delta**0.5) / 2*a
        
def str_equation(a : float,b : float,c : float) -> str :
    """ Retourne une chaine de caractère représentant l'équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0)

    Args:
        a (float)
        b (float)
        c (float)
    Returns:
        str: équation du second degré
    """
    return f"{a}x2 + {b}x + {c} = 0"

def solution_equation(a : float,b : float,c: float) -> str  :
    """ Retourne une chaine de caractère représentant la solution de l'équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0)

    Args:
        a (float)
        b (float)
        c (float)

    Returns:
        str: solution de l'équation du second degré
    """
    if discriminant(a,b,c) < 0 : 
        return "Pas de racine réelle si l'équation n'a pas de solution réelle"
    if discriminant(a,b,c) == 0 : 
        return f"Racine unique x = {racine_unique(a,b)}"
    if discriminant(a,b,c) > 0 : 
        return f"Racine double x1 = {racine_double(a,b, discriminant(a,b,c), 1)} ; x2 = {racine_double(a,b, discriminant(a,b,c), 2)}"


def equation(a : float,b : float,c: float) -> str: 
    """ Affiche l'équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0) et sa solution

    Args:
        a (float)
        b (float)
        c (float)

    Returns:
        str: équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0) et sa solution
    """

    print((solution_equation(a,b,c)))
    
def test(test_dict : dict ) -> str : 
    """ Teste la fonction equation (ax²+bx+c =0 avec a,b,c réels et a≠0)

    Args:
        test_dict (dict): dictionnaire de test

    Returns:
        str: test de la fonction equation
    """
    for a,b,c in test_dict : 
        equation(a,b,c)
        
test(TEST_DATA)
    
    