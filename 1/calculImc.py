# CONST 

# IMC Interprétation 
# < 16,5 dénutrition ou famine -> IF

# 16,5 à 18,5 maigreur
# 18,5 à 25 corpulence normale 
# 25 à 30 surpoids 
# 30 à 35 obésité modérée 
# 35 à 40 obésité sévère 

# plus de 40 obésité morbide  -> IF

# structure : { "interprétation" : (min, max), ..."}
IMC = {
    "maigreur" : (16.5, 18.5),
    "corpulence normale" : (18.5, 25),
    "surpoids" : (25, 30),
    "obésité modérée" : (30, 35),
    "obésité sévère" : (35, 40),
}
    
    

# Functions
def message_imc(imc : float) -> str :
    """_summary_

    Args:
        imc (float): _description_

    Returns:
        str: _description_
    """
    for interpretation, (min, max) in IMC.items() :
        if imc >= min and imc < max :
            return interpretation



print(message_imc(17))