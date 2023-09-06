

# CONST
TYPES_LETTERS = {
    "VERTE": [(20, 1.16), (100, 2.32), (250, 4), (500, 6), (1000, 7.5), (3000, 10.5)],
    "PRIORITAIRE" : [(20, 1.43), (100, 2.86), (250, 5.26), (500, 7.89), (3000, 11.44)],
    "ECOPLI" : [(20, 1.14), (100, 2.28), (250, 3.92)],
}

PRIX_SUIVI = 0.5
# FUNCTIONS



def affranchissement_lettre(type : str , poid : int) -> float : 
    """
    Calcule le prix d'affranchissement(float) d'une lettre en fonction de son type(int) et de son poids(int)
    type : str
    poids : int
    """
    type = type.upper()
    # exemple : prix = TYPES_LETTERS[type][0][1]
    for i in range(len(TYPES_LETTERS[type])):
        if poid <= TYPES_LETTERS[type][i][0]:
            return TYPES_LETTERS[type][i][1]

# EXECUTION
input_type = input("Quel est le type de votre lettre ? (verte, prioritaire, ecopli) : ")
input_poinds = int(input("Quel est le poids de votre lettre ? : "))

print(affranchissement_lettre(input_type, input_poinds))
    
    
