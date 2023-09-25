from numpy import array, searchsorted,size, where
from random import randint

arr = array([randint(0, 999) for _ in range(1000000)])
print(arr)
arr2 = array([[1, 2, 3], [4, 5, 6]]) 
print(where(arr2==4)) # renvoie les indices 
# searchsorted() -> une methode de l'objet numpy permet de chercher un élément et renvoyer son indice
print(array([1, 2, 3, 4, 5][1:]))

# une dimension et un élément
def searchsorted_perso(arr : array, searched : int, acc=0) : 
    if arr.size == 0 : 
        return -1
    else :
        if arr[0] == searched : 
            return acc
        else : 
            return lambda: searchsorted_perso(arr[1:], searched,acc+1) # Continuation-passing style

# trampoline pattern 
def trampoline(func):
    while callable(func):
        func = func()
    return func
print(trampoline(lambda: searchsorted_perso(arr, 20)))


def where_perso(arr: array, searched :int) :
    pass


