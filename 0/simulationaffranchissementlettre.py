# CONST
# structure : TYPES_LETTERS = { type : [(poids, prix), (poids, prix), ...], type : [(poids, prix), (poids, prix), ...], ...}
TYPES_LETTERS = {
    "VERTE": [(20, 1.16), (100, 2.32), (250, 4), (500, 6), (1000, 7.5), (3000, 10.5)],
    "PRIORITAIRE" : [(20, 1.43), (100, 2.86), (250, 5.26), (500, 7.89), (3000, 11.44)],
    "ECOPLI" : [(20, 1.14), (100, 2.28), (250, 3.92)],
}

# FUNCTIONS
def affranchissement_lettre(type : str , poids : int) -> float : 
    """
    Calcule le prix d'affranchissement(float) d'une lettre en fonction de son type(int) et de son poids(int)
    type : str
    poids : int
    """
    # example : prix = TYPES_LETTERS[type][0][1]
    
    # if poid exceed the max weight for this type of letter
    if poids > TYPES_LETTERS[type][-1][0] :
        return f"Vous dépasser le poid maximum qui est {TYPES_LETTERS[type][-1][0]}g pour ce type de lettre"
 
    for i in range(len(TYPES_LETTERS[type])):
        # if poid is in the range of the current weight
        if poids <= TYPES_LETTERS[type][i][0]:
            return f"{TYPES_LETTERS[type][i][1]}€"


# EXECUTION
input_type = input("Quel est le type de votre lettre ? (verte, prioritaire, ecopli) : ").upper().strip()
# loop to check if input_poids is correct
while input_type not in TYPES_LETTERS:
    print("Vous n'avez pas choisi un type de lettre, on continue ")
    input_type = input("Quel est le type de votre lettre ? (verte, prioritaire, ecopli) : ").upper().strip()
input_poids = int(input("Quel est le poids de votre lettre ? : "))
    
print(affranchissement_lettre(input_type, input_poids))
    
    
