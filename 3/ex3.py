

def  places_lettre(ch : str, mot : str) -> list : 
    return [l for l in range(len(mot)) if mot[l]== ch]

print(places_lettre("m", "maman"))
