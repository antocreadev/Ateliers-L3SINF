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
    """
    Calcule le discriminant d'une équation quadratique de la forme ax^2 + bx + c.

    Args:
        a (float): Le coefficient de x^2.
        b (float): Le coefficient de x.
        c (float): Le coefficient constant.

    Returns:
        float: La valeur du discriminant.

    Examples:
        >>> discriminant(1.0, -2.0, 1.0)
        4.0
        >>> discriminant(1.0, 2.0, 1.0)
        0.0
    """
    return b**2 - 4*a*c

def racine_unique(a : float,b : float) -> float : 
    """
    Calcule la racine unique d'une équation linéaire de la forme ax + b = 0.

    Args:
        a (float): Le coefficient de x.
        b (float): Le coefficient constant.

    Returns:
        float: La valeur de la racine unique.

    Examples:
        >>> racine_unique(2.0, -4.0)
        2.0
        >>> racine_unique(0.0, 5.0)
        "Le coefficient 'a' ne doit pas être égal à 0."
    """
    if a == 0 : 
        return "a ne doit pas être égale à 0"
    return -b / 2*a


def racine_double(a : float,b : float,delta : float ,num : int) :
    """
    Calcule les racines d'une équation quadratique de la forme ax^2 + bx + c = 0.

    Args:
        a (float): Le coefficient de x^2.
        b (float): Le coefficient de x.
        delta (float): La valeur du discriminant.
        num (int): Le numéro de la racine (1 ou 2).

    Returns:
        float: La valeur de la racine correspondante.

    Examples:
        >>> racine_double(1.0, -2.0, 0.0, 1)
        2.0
        >>> racine_double(2.0, 4.0, -16.0, 2)
        -4.0
        >>> racine_double(0.0, 5.0, 25.0, 1)
        "Le coefficient 'a' ne doit pas être égal à 0."
    """
    if a == 0 : 
        return "a ne doit pas être égale à 0"
    if num == 1 : 
        return (-b + delta**0.5) / 2*a
    if num == 2 : 
        return (-b - delta**0.5) / 2*a
        
def str_equation(a : float,b : float,c : float) -> str :
    """
    Génère une représentation textuelle d'une équation quadratique de la forme ax^2 + bx + c = 0.

    Args:
        a (float): Le coefficient de x^2.
        b (float): Le coefficient de x.
        c (float): Le coefficient constant.

    Returns:
        str: La représentation textuelle de l'équation.

    Examples:
        >>> str_equation(1.0, -2.0, 1.0)
        "1.0x^2 - 2.0x + 1.0 = 0"
        >>> str_equation(2.0, 4.0, -16.0)
        "2.0x^2 + 4.0x - 16.0 = 0"
    """
    return f"{a}x2 + {b}x + {c} = 0"

def solution_equation(a : float,b : float,c: float) -> str  :
    """
    Détermine les solutions d'une équation quadratique de la forme ax^2 + bx + c = 0.

    Args:
        a (float): Le coefficient de x^2.
        b (float): Le coefficient de x.
        c (float): Le coefficient constant.

    Returns:
        str: Une chaîne de caractères décrivant les solutions de l'équation.

    Examples:
        >>> solution_equation(1.0, -2.0, 1.0)
        "Racine unique x = 1.0"
        >>> solution_equation(2.0, 4.0, -16.0)
        "Racine double x1 = 2.0 ; x2 = -4.0"
        >>> solution_equation(0.0, 5.0, 25.0)
        "Le coefficient 'a' ne doit pas être égal à 0."
        >>> solution_equation(1.0, 2.0, 1.0)
        "Racine unique x = -1.0"
        >>> solution_equation(1.0, -3.0, 2.0)
        "Racine double x1 = 2.0 ; x2 = 1.0"
        >>> solution_equation(1.0, 2.0, 3.0)
        "Pas de racine réelle si l'équation n'a pas de solution réelle"
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
    """
    Affiche les solutions d'une équation quadratique de la forme ax^2 + bx + c = 0.

    Args:
        a (float): Le coefficient de x^2.
        b (float): Le coefficient de x.
        c (float): Le coefficient constant.

    Returns:
        None

    Examples:
        >>> equation(1.0, -2.0, 1.0)
        Racine unique x = 1.0

        >>> equation(2.0, 4.0, -16.0)
        Racine double x1 = 2.0 ; x2 = -4.0

        >>> equation(0.0, 5.0, 25.0)
        Le coefficient 'a' ne doit pas être égal à 0.

        >>> equation(1.0, 2.0, 1.0)
        Racine unique x = -1.0

        >>> equation(1.0, -3.0, 2.0)
        Racine double x1 = 2.0 ; x2 = 1.0

        >>> equation(1.0, 2.0, 3.0)
        Pas de racine réelle si l'équation n'a pas de solution réelle
    """
    print(f"{solution_equation(a,b,c)} \n")
    
def test(test_dict : list ) -> str : 
    """
    Teste plusieurs équations quadratiques et affiche les résultats attendus et obtenus.

    Args:
        test_dict (list): Une liste de tuples contenant les coefficients a, b, c et le résultat attendu.

    Returns:
        None

    Examples:
        >>> test([(1.0, -2.0, 1.0, "Racine unique x = 1.0"),
        >>>       (2.0, 4.0, -16.0, "Racine double x1 = 2.0 ; x2 = -4.0"),
        >>>       (0.0, 5.0, 25.0, "Le coefficient 'a' ne doit pas être égal à 0."),
        >>>       (1.0, 2.0, 1.0, "Racine unique x = -1.0"),
        >>>       (1.0, -3.0, 2.0, "Racine double x1 = 2.0 ; x2 = 1.0"),
        >>>       (1.0, 2.0, 3.0, "Pas de racine réelle si l'équation n'a pas de solution réelle")]
        )
    """
    for a,b,c, output in test_dict : 
        print(f"TEST\noutput attendu :\n{output}")
        print("output obtenu :")
        equation(a,b,c)
        
test(TEST_DATA)
    
    