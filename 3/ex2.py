def mots_Nlettres(lst_mot: list, n:int) -> list: 
    return [mot for mot in lst_mot if len(mot)<=n]

def commence_par(mot: str, prefixe : str) -> bool :
    # return True if mot == prefixe +mot[len(prefixe):]  else False
    return mot == prefixe +mot[len(prefixe):] 

print(commence_par("aa", "a"))

def finit_par(mot :str, suffixe: str) -> bool :
    # return True if mot == mot[:len(mot)-len(suffixe)] + suffixe else False
    return mot == mot[:len(mot)-len(suffixe)] + suffixe
    
def finissent_par(lst_mot : list, suffixe: str) -> list: 
    return [mot for mot in lst_mot if finit_par(mot, suffixe)]

def commencent_par(lst_mot :list, prefixe:str) -> list : 
    return [mot for mot in lst_mot if commence_par(mot, prefixe)]

def liste_mots (lst_mot : list, prefixe : str, suffixe :str, n :int) -> list: 
    return finissent_par(commencent_par(mots_Nlettres(lst_mot, 5), prefixe),suffixe)

def dictionnaire(fichier) -> list:
    with open(fichier,"r") as file : #with : Le fichier est automatiquement fermé à la fin du bloc "with"
        return [ligne.rstrip("\n") for ligne in file]
print(dictionnaire("littre.txt"))
# .rstrip() -> supprimer toute la partie droite lorque qu'il trouve le séparateur (par défaut les espaces)