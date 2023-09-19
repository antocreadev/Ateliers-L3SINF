def mots_Nlettres(lst_mot: list, n:int) -> list: 
    """
    Retourne une liste de mots de la liste 'lst_mot' qui ont une longueur inférieure ou égale à 'n'.

    :param lst_mot: Liste de mots à filtrer.
    :type lst_mot: list
    :param n: Longueur maximale des mots à conserver.
    :type n: int
    :return: Liste des mots de 'lst_mot' dont la longueur est inférieure ou égale à 'n'.
    :rtype: list
    """
    return [mot for mot in lst_mot if len(mot)<=n]

def commence_par(mot: str, prefixe : str) -> bool :
    """
    Vérifie si le mot 'mot' commence par le préfixe 'prefixe'.

    :param mot: Mot à vérifier.
    :type mot: str
    :param prefixe: Préfixe à rechercher au début du mot.
    :type prefixe: str
    :return: True si 'mot' commence par 'prefixe', False sinon.
    :rtype: bool
    """
    return mot == prefixe +mot[len(prefixe):] 

def finit_par(mot :str, suffixe: str) -> bool :
    """
    Vérifie si le mot 'mot' se termine par le suffixe 'suffixe'.

    :param mot: Mot à vérifier.
    :type mot: str
    :param suffixe: Suffixe à rechercher à la fin du mot.
    :type suffixe: str
    :return: True si 'mot' se termine par 'suffixe', False sinon.
    :rtype: bool
    """
    return mot == mot[:len(mot)-len(suffixe)] + suffixe
    
def finissent_par(lst_mot : list, suffixe: str) -> list: 
    """
    Retourne une liste de mots de la liste 'lst_mot' qui se terminent par 'suffixe'.

    :param lst_mot: Liste de mots à filtrer.
    :type lst_mot: list
    :param suffixe: Suffixe à rechercher à la fin des mots.
    :type suffixe: str
    :return: Liste des mots de 'lst_mot' se terminant par 'suffixe'.
    :rtype: list
    """
    return [mot for mot in lst_mot if finit_par(mot, suffixe)]

def commencent_par(lst_mot :list, prefixe:str) -> list : 
    """
    Retourne une liste de mots de la liste 'lst_mot' qui commencent par 'prefixe'.

    :param lst_mot: Liste de mots à filtrer.
    :type lst_mot: list
    :param prefixe: Préfixe à rechercher au début des mots.
    :type prefixe: str
    :return: Liste des mots de 'lst_mot' commençant par 'prefixe'.
    :rtype: list
    """
    return [mot for mot in lst_mot if commence_par(mot, prefixe)]

def liste_mots (lst_mot : list, prefixe : str, suffixe :str, n :int) -> list: 
    """
    Retourne une liste de mots de la liste 'lst_mot' qui ont une longueur inférieure ou égale à 'n',
    commencent par 'prefixe' et se terminent par 'suffixe'.

    :param lst_mot: Liste de mots à filtrer.
    :type lst_mot: list
    :param prefixe: Préfixe à rechercher au début des mots.
    :type prefixe: str
    :param suffixe: Suffixe à rechercher à la fin des mots.
    :type suffixe: str
    :param n: Longueur maximale des mots à conserver.
    :type n: int
    :return: Liste des mots de 'lst_mot' satisfaisant toutes les conditions.
    :rtype: list
    """
    return finissent_par(commencent_par(mots_Nlettres(lst_mot, 5), prefixe),suffixe)

def dictionnaire(fichier) -> list:
    """
    Lit un fichier texte 'fichier' et retourne son contenu sous forme de liste de lignes.

    :param fichier: Chemin vers le fichier texte à lire.
    :type fichier: str
    :return: Liste des lignes lues depuis le fichier.
    :rtype: list
    """
    with open(fichier,"r") as file : #with : Le fichier est automatiquement fermé à la fin du bloc "with"
        return [ligne.rstrip("\n") for ligne in file]
print(dictionnaire("littre.txt"))
# .rstrip() -> supprimer toute la partie droite lorque qu'il trouve le séparateur (par défaut les espaces)