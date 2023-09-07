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
    "maigreur" : (16.5, 18.5),
    "corpulence normale" : (18.5, 25),
    "surpoids" : (25, 30),
    "obésité modérée" : (30, 35),
    "obésité sévère" : (35, 40),
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
    if imc < IMC["maigreur"][0] :
        message = "dénutrition ou famine"
    elif imc > IMC["obésité sévère"][1] :
        message = "obésité morbide"
    else :
        for interpretation, (min, max) in IMC.items() : # (min, max) -> destructuring
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
    for k in range(x) :
        imc = round(uniform(0, x),2)
        print(f"imc = {imc} : {message_imc(imc)}")

# --- MAIN ---
test_message_imc(50)