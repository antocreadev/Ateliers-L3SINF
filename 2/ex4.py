from matplotlib import pyplot as plt

TEST_LISTE = [1, 5, 5, 5, 9, 11, 11, 15, 15, 15]
TEST_LISTE2 = [0, 1, 2, 3, 4, 5]

def histo(F: list) -> list:
    """
    Calcule l'histogramme d'une liste d'entiers.

    Args:
        F (list): Une liste d'entiers.

    Returns:
        list: Une liste représentant l'histogramme des valeurs de F.
    """
    minimum = 0
    maximum = 0
    for k in range(len(F)):
        if F[k] > maximum:
            maximum = F[k]
        if F[k] < minimum:
            minimum = F[k]
    H = [0] * (maximum + 1)

    for f in range(len(F)):
        H[F[f]] += 1
    return H

def est_injective(F: list) -> bool:
    """
    Vérifie si une fonction représentée sous forme d'histogramme est injective.

    Args:
        F (list): Une liste d'entiers représentant l'histogramme d'une fonction.

    Returns:
        bool: True si la fonction est injective, False sinon.
    """
    counter = 0
    result = True
    F = histo(F)
    while counter < len(F) and result:
        if F[counter] > 1:
            result = False
        counter += 1
    return result

def est_surjective(F: list) -> bool:
    """
    Vérifie si une fonction représentée sous forme d'histogramme est surjective.

    Args:
        F (list): Une liste d'entiers représentant l'histogramme d'une fonction.

    Returns:
        bool: True si la fonction est surjective, False sinon.
    """
    counter = 0
    result = True
    F = histo(F)
    while counter < len(F) and result:
        if F[counter] < 1:
            result = False
        counter += 1
    return result

def est_bijective(F: list) -> bool:
    """
    Vérifie si une fonction représentée sous forme d'histogramme est bijective.

    Args:
        F (list): Une liste d'entiers représentant l'histogramme d'une fonction.

    Returns:
        bool: True si la fonction est bijective, False sinon.
    """
    F = histo(F)
    return est_surjective(F) and est_injective(F)

def afficheHisto(F: list) -> None:
    """
    Affiche l'histogramme d'une liste d'entiers.

    Args:
        F (list): Une liste d'entiers.

    Returns:
        None
    """
    print("TEST HISTOGRAMME \n")
    print(f"F={F} \n")
    print("HISTOGRAMME\n")
    histogramme = histo(F)

    max_histo = max(histogramme)

    for li in range(max_histo, -1, -1):
        print()
        for col in range(len(histogramme)):
            if histogramme[col] - li >= 1:
                print(" # ", end="")
            else:
                print("   ", end="")

    print()
    for h in range(len(histogramme)):
        print("--|", end="")

    print()
    for h in range(len(histogramme)):
        if h < 10:
            print(f" {h} ", end="")
        else:
            print(f" {h}", end="")
    return None

def hist(F: list) -> None:
    """
    Affiche un histogramme à partir d'une liste d'entiers en utilisant matplotlib.

    Args:
        F (list): Une liste d'entiers.

    Returns:
        None
    """
    plt.hist(F)
    plt.show()

def test():
    """
    Fonction de test pour les fonctions définies.
    """
    print("Test de la fonction histo:")
    print(histo(TEST_LISTE))
    print(histo(TEST_LISTE2))

    print("\nTest de la fonction est_injective:")
    print(est_injective(TEST_LISTE))
    print(est_injective(TEST_LISTE2))

    print("\nTest de la fonction est_surjective:")
    print(est_surjective(TEST_LISTE))
    print(est_surjective(TEST_LISTE2))

    print("\nTest de la fonction est_bijective:")
    print(est_bijective(TEST_LISTE))
    print(est_bijective(TEST_LISTE2))

    print("\nTest de la fonction afficheHisto:")
    afficheHisto(TEST_LISTE)
    afficheHisto(TEST_LISTE2)

    print("\nTest de la fonction hist:")
    hist(TEST_LISTE)
    hist(TEST_LISTE2)

test()

