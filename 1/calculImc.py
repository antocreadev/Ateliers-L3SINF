# --- IMPORT ---
from random import uniform
from math import inf

# --- CONST ---
# structure : [tuple (imc , message)]
IMC = [
    (16.5,  "dénutrition ou famine"),
    (18.5 , "maigreur" ),
    (25 , "corpulence normale"),
    (30 , "surpoids"),
    (35 , "obésité modérée"),
    (40 , "obésité sévère" ),
    (inf , "obésité morbide")
]
# --- Functions ---
def message_imc(imc : float) -> str :
    """ function that returns a message according to the imc

    Args:
        imc (float)

    Returns:
        str: iterpretation of the imc
    """
    message = IMC[0][1]
    counter = 0
    while imc >= IMC[counter][0] :
        message = IMC[counter][1]
        counter += 1
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

