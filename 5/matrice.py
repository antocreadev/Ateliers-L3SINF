from numpy import array, searchsorted,size
from random import randint

arr = array([randint(0, 999) for _ in range(100000)])
arr2 = array([[1, 2, 3], [4, 5, 6]]) 
# searchsorted() -> une methode de l'objet numpy permet de chercher un élément et renvoyer son indice

print(array([1, 2, 3, 4, 5][1:]))


def searchsorted_perso(arr : array, searched : int, acc=0) -> int : 
    if arr.size == 0 : 
        return "Error" 
    else :
        if arr[0] == searched : 
            return acc
        else : 
            return lambda: searchsorted_perso(arr[1:], searched,acc+1)

def trampoline(func):
    while callable(func):
        func = func()
    return func
print(trampoline(lambda: searchsorted_perso(arr, 20,)))


