def places_lettre(ch: str, mot: str) -> list:
    """
    Retourne une liste des positions (indices) où la lettre 'ch' apparaît dans le mot 'mot'.

    :param ch: La lettre à rechercher.
    :type ch: str
    :param mot: Le mot dans lequel rechercher la lettre.
    :type mot: str
    :return: Liste des positions (indices) où 'ch' apparaît dans 'mot'.
    :rtype: list
    """

def test():
    """
    Fonction de test pour la fonction 'places_lettre'.
    Affiche les résultats attendus et les résultats obtenus pour quelques exemples.
    """
    print(f"input attendu : [0] ; input obtenu : {places_lettre('b', 'bonjour')}")
    print(f"input attendu : [] ; input obtenu : {places_lettre('a', 'bonjour')}")
    print(f"input attendu : [0, 2] ; input obtenu : {places_lettre('m', 'maman')}")

def outputStr(mot: str, lpos: list) -> str:
    """
    Affiche le mot 'mot' en remplaçant les lettres aux positions spécifiées dans 'lpos' par des tirets (-).

    :param mot: Le mot à afficher.
    :type mot: str
    :param lpos: Liste des positions (indices) des lettres à conserver.
    :type lpos: list
    """
    longueur = len(mot)
    print(lpos)
    for i in range(len(mot)):
        if i in lpos:
            print(mot[i], end="")
        else:
            print("-", end="")
