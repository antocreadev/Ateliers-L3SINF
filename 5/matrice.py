from numpy import array, searchsorted,size, where, int64, ndarray, ndenumerate, shape, zeros
from random import randint

arr = array([randint(0, 999) for _ in range(1000000)])
arr2 = array([[9, 8, 2],
              [3, 4, 5]])    
arr3 = array([])
arr4 = array([[1, 2, 3],
              [4, 5, 6], ])

# print(where(arr2==4)) # renvoie les indices 
# searchsorted() -> une methode de l'objet numpy permet de chercher un élément et renvoyer son indice

# une dimension et un élément
def searchsorted_perso(arr : array, searched : int, acc=0) : 
    if arr.size == 0 : 
        return -1
    else :
        if arr[0] == searched : 
            return acc
        else : 
            return lambda : searchsorted_perso(arr[1:], searched,acc+1) # Continuation-passing style
# trampoline pattern 
def trampoline(func):
    while callable(func):
        func = func()
    return func


def where_perso(arr: array, searched :int) :
    result = []
    for index, element in ndenumerate(arr):
        if element == searched:
            result.append(index)
    return result

def where_perso_v2(arr: array, searched :int) :
    result = []
    counter = 0
    for i in range(len(arr)) : 
        for k in range(len(arr[i])) : 
            if searched == arr[i][k] : 
                result.append((i, k))
    return result

def where_perso_recursive(arr, searched, i=0, k=0, result=None):
    if result is None:
        result = []
    if i < len(arr):
        if k < len(arr[i]):
            if searched == arr[i][k]:
                result.append((i, k))
            where_perso_recursive(arr, searched, i, k + 1, result)
        else:
            where_perso_recursive(arr, searched, i + 1, 0, result)
    return result


def addition(arr1, arr2) : 
    result = ValueError("Les deux tableaux doivent avoir la même taille")
    if (arr1.shape == arr2.shape) : 
        result = []
        for i in range(len(arr1)) : 
            result.append([])
            for k in range(len(arr1[i])) :
                result[i].append(arr1[i][k] + arr2[i][k])
    return array(result)
    
def addition_v2(arr1, arr2) : 
    result = ValueError("Les deux tableaux doivent avoir la même taille")
    if (arr1.shape == arr2.shape) : 
        #np.zeros(arr1.shape) -> créer matrice rempli de zéro de la shape donnée 
        result = zeros(arr1.shape, dtype=int64)
        for i in range(len(arr1)) : 
            for k in range(len(arr1[i])) :
                result[i][k] = arr1[i][k] + arr2[i][k]
    return result
print(addition_v2(arr2, arr4))

# autres exercies 

# Exercice 2 : Manipulations avancées
def matrice_trace(matrice) : 
    pass

def est_symetrique(matrice) : 
    pass

def  produit_diagonal(matrice) : 
    pass

