# CONST 
# structure de TEST_DATA : [tuple (a,b,c, output)]
TEST_DATA = [
    (1, -5, 6, "Racine double x1 = 3.0 ; x2 = 2.0"), 
    (1, -5, 4, "Racine double x1 = 4.0 ; x2 = 1.0 "),
    (1, 2, 5,  "Pas de racine réelle si l'équation n'a pas de solution réelle"),
    (0, 2, 1, "a ne doit pas être égale à 0")
]
# --- Functions ---
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
    if a == 0 : 
        return "a ne doit pas être égale à 0"
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
    result = None
    result_discriminant = discriminant(a,b,c)

    
    if result_discriminant < 0 : 
        result = "Pas de racine réelle si l'équation n'a pas de solution réelle"
    elif result_discriminant == 0 : 
        result = f"Racine unique x = {racine_unique(a,b)}"
    elif result_discriminant > 0 : 
        result = f"Racine double x1 = {racine_double(a,b, result_discriminant, 1)} ; x2 = {racine_double(a,b, result_discriminant, 2)}"
    else : 
        result = "Erreur"
        
    if a == 0 :
        result = "a ne doit pas être égale à 0"
        
    return result

def equation(a : float,b : float,c: float) -> str: 
    """ Affiche l'équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0) et sa solution

    Args:
        a (float)
        b (float)
        c (float)

    Returns:
        str: équation du second degré (ax²+bx+c =0 avec a,b,c réels et a≠0) et sa solution
    """

    print(f"{solution_equation(a,b,c)} \n")
    
def test(test_dict : list ) -> str : 
    """ Teste la fonction equation()

    Args:
        test_dict (list): liste de test

    Returns:
        str: test de la fonction equation
    """
    for a,b,c, output in test_dict : 
        print(f"TEST\noutput attendu :\n{output}")
        print("output obtenu :")
        equation(a,b,c)
        
test(TEST_DATA)
    
    