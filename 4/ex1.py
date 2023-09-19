from random import randint

def gen_list_random_int(int_binf: int=0, int_bsup: int=10)-> list : 
    """
    Génère une liste de nombres entiers aléatoires compris entre 'int_binf' (inclus) et 'int_bsup' (inclus).

    :param int_binf: Limite inférieure de la plage des nombres aléatoires (inclus).
    :type int_binf: int
    :param int_bsup: Limite supérieure de la plage des nombres aléatoires (inclus).
    :type int_bsup: int
    :return: Liste de nombres entiers aléatoires.
    :rtype: list
    """
    return [randint(int_binf, int_bsup) for i in range(int_bsup)]

# print(gen_list_random_int(0,10))

def mix_list(list_to_mix) : 
    """
    Mélange les éléments d'une liste 'list_to_mix' de manière aléatoire et renvoie la nouvelle liste mélangée.

    :param list_to_mix: Liste à mélanger.
    :type list_to_mix: list
    :return: Liste mélangée.
    :rtype: list
    """
    new_liste = []
    while len(new_liste) < len(list_to_mix) : 
        indice_random = randint(0,len(list_to_mix)-1)
        if list_to_mix[indice_random] not in  new_liste: 
            new_liste.append(list_to_mix[indice_random])
    return new_liste

print([1,2,3,4,5,6,7,8,9,10])
print(mix_list([1,2,3,4,5,6,7,8,9,10]))


def choose_element_list(list_in_which_to_choose : list) : 
    """
    Sélectionne aléatoirement un élément de la liste 'list_in_which_to_choose' et le renvoie.

    :param list_in_which_to_choose: Liste dans laquelle choisir un élément.
    :type list_in_which_to_choose: list
    :return: Élément sélectionné aléatoirement.
    :rtype: any
    """
    return list_in_which_to_choose[randint(0, len(list_in_which_to_choose))-1]

def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extrac : int):
    """
    Extrait un nombre donné d'éléments aléatoires de la liste 'list_in_which_to_choose' et les renvoie dans une nouvelle liste.

    :param list_in_which_to_choose: Liste dans laquelle extraire les éléments.
    :type list_in_which_to_choose: list
    :param int_nbr_of_element_to_extract: Nombre d'éléments à extraire.
    :type int_nbr_of_element_to_extract: int
    :return: Liste des éléments extraits aléatoirement.
    :rtype: list
    """
    return [choose_element_list(list_in_which_to_choose) for i in range(int_nbr_of_element_to_extrac)]

def test():
    """
    Fonction de test pour les fonctions 'mix_list', 'choose_element_list' et 'extract_elements_list'.
    Affiche les résultats attendus et effectue des vérifications sur les fonctions.
    """
    # Test de votre code 
    lst_sorted=[i for i in range(10)] 
    print(lst_sorted) 
    print('Liste triée de départ',lst_sorted) 
    mixed_list=mix_list(lst_sorted) 
    print('Liste mélangée obtenue',mixed_list) 
    print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted) 
    #assert (cf. doc en ligne) permet de vérifier qu’une condition  
    #est vérifiée en mode debug (désactivable) 
    assert lst_sorted != mixed_list,"Les deux listes doivent être différente après l'appel à mixList..." 
    
    
    # Test de votre code 
    print('Liste triée de départ',lst_sorted) 
    e1 = choose_element_list(lst_sorted) 
    print('A la première exécution',e1,'a été sélectionné') 
    e2 = choose_element_list(lst_sorted) 
    print('A la deuxième exécution',e2,'a été sélectionné') 
    assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"
    
    # Test de votre code 
    print('Liste de départ',lst_sorted) 
    sublist = extract_elements_list(lst_sorted,5) 
    print('La sous liste extraite est',sublist) 
    print('Liste de départ après appel de la fonction est',lst_sorted)
    
test()