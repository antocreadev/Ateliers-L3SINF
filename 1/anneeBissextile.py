# import 
from random import randint 


# CONST 
annees_test = {
    2000: True,
    1900: False,
    2004: True,
    2100: False,
    2012: True,
    2022: False
}

def est_bissextile(annee : int) -> bool : 
    """prend  en  paramètre  un  nombre  entier  représentant 
une année et renvoie un booléen indiquant si l'année considérée est bissextile ou non.  

    Args:
        annee (int) : l'annee à tester

    Returns:
        bool: if bissextile True else False 
    """
    if annee % 4 ==0 and annee % 100 != 0 or annee % 400 ==0 : 
        return True 
    else : 
        return False 

def test_est_bissextile(x : int ) -> str:
    """Fonction de test pour la fonction est_bissextile()

    Args:
        x (int): nombre de test aléatoire

    Returns:
        str: retour du test
    """
    
    print("test aléatoire")
    for k in range(x): 
        annee = randint(0, 10000)
        print(f"L'annee {annee} est t-elle bissextile ?  {est_bissextile(annee)}")
        
    print("test anticipé")
    for annee_test in annees_test.items() : 
        if est_bissextile(annee_test[0]) == annee_test[1] : 
            print(f"\n \n D'après les données pour les tests anticipé : {annee_test[0]} est t-elle bissextile ? {annee_test[1]} \n d'après le programme l'année {annee_test[0]} est t'elle bissextile ? {est_bissextile(annee_test[0])} \n le test est validé")
        
# test_est_bissextile(2000)

