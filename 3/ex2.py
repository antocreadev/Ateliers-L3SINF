def mots_Nlettres(lst_mot: list, n:int) -> list: 
    liste_longueur = []
    accumulateur = 0 
    result = []
    
    for mot in range(len(lst_mot)) : 
        for l in range(len(lst_mot[mot])) : 
            accumulateur += 1
        liste_longueur.append(accumulateur)
        accumulateur = 0
    print(liste_longueur)
    
    for k in range(len(lst_mot)) : 
        print(f"{lst_mot[k]} ---> taille : {liste_longueur[k]}")
        if liste_longueur[k] <= n : 
            result.append(lst_mot[k])
    return result
            
def mots_Nlettres_comprehnsion_list(lst_mot: list, n:int) -> list: 
    return [mot for mot in lst_mot if len(mot)<=n]
            
print(mots_Nlettres(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"], 5))

print(mots_Nlettres_comprehnsion_list(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"], 5))


def commence_par(mot, prefixe) :
    return True if mot == prefixe +mot[len(prefixe):]  else False
    
print(commence_par("Lol", "L"))