
liste_test = [7, -10, 13, 8, 4, -7.2, -12, -3.7, 3.5,1, -1.7, 2, 0]
def renvoie_valeur_proche_zero(liste : list) -> float :
    liste.sort()
    negatif = []
    positif = []
    for l in range(len(liste)) : 
        if liste[l] <= 0 : 
            negatif.append(liste[l])
        else : 
            positif.append(liste[l])
    if (abs(negatif[-1]) < abs(positif[0])) : 
        return negatif[-1]
    else : 
        return positif[0]

            

print(renvoie_valeur_proche_zero(liste_test))