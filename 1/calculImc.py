# --- IMPORT ---
from random import uniform

# --- UTILS --- :
    # On peut parcourir un dictionnaire avec les méthodes suivantes (on ne peut pas parcourir un dictionnaire avec une boucle for classique car un dict n'est pas une sséquence et n'est pas indexé)
    # keys() : parcourt les clés.
    # values() : parcourt les valeurs.
    # items() : parcourt les couples clé-valeur
    
    # uniform fonctionne comme randint mais avec des float
    
    # (min, max) -> destructuring dans la boucle sont des variables temporaires à la boucle
    
    
# --- CONST ---
# structure : { "interprétation" : (min, max), ..."}
IMC = {
    (0, 16.5) : "dénutrition ou famine",
    (16.5, 18.5) : "maigreur", 
    (18.5, 25) : "corpulence normale", 
    (25, 30) : "surpoids", 
    (30, 35) : "obésité modérée",
    (35, 40) : "obésité sévère", 
    (40, 999) : "obésité morbide"
}

# --- Functions ---
def message_imc(imc : float) -> str :
    """ function that returns a message according to the imc

    Args:
        imc (float)

    Returns:
        str: iterpretation of the imc
    """
    message = None
    for (min, max), interpretation,  in IMC.items() :
        if imc >= min and imc < max :
            message = interpretation
    return message

def test_message_imc(x : int ) -> str:
    """ function that tests the function message_imc
    
        Args:
            x (int) : number of tests

        Returns:
            str: iterpretation of the imc
    """
    for k in range(x): 
        imc = round(uniform(0, 120),2)
        print(f"imc = {imc} : {message_imc(imc)}")

# --- MAIN ---
test_message_imc(100)

