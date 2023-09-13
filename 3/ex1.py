def full_name(str_arg:str)->str :
    counter = 0
    nom = ""
    while len(str_arg) > counter and str_arg[counter] != " ":
        nom += chr(ord(str_arg[counter])-32)
        counter += 1
    return nom +" " +chr(ord(str_arg[counter:][1])-32) + str_arg[counter+2:]
print(full_name("menghi anthony"))

# ord() -> retourne le code ascii d'un caractère (en décimal) 
# chr() -> transforme un code ascii (en décimal) en caractère
# -32 pour passer de minuscule à majuscule

def full_name_v2(str_arg:str)->str : 
    str_arg = str_arg.split() 
    return str_arg[0].upper() + " " + str_arg[1][0].upper()+str_arg[1][1:]

# split() -> detecte les espaces et transforme la chaîne de carctère en list
# la valeur minimum de split() c'est un car s'il trouve pas le séparateur il renvoie la chaîne entière
print(full_name_v2("menghi anthony"))

def is_mail(str_arg:str) -> tuple[int, int]: 
    result = (1, 0)
    liste_corps_domaine = str_arg.split(sep="@")
    if len(liste_corps_domaine) != 2 : 
        result = (0,2)
    else : 
        corps = liste_corps_domaine[0]
        domaine = liste_corps_domaine[1]
        # corps
        if "." in corps[0] or  "." in corps[-1] or ".." in corps : 
            result = (0,1)
        #domaine
        if "." in domaine[0] or  "." in domaine[-1] or ".." in domaine or "_" in domaine : 
            result = (0,3)
        # si il n'y a pas de point -> erreur car il n'a pas de trouver le séparateur 
        elif len(domaine.split(".")) == 1 : 
            result = (0,3)
    return result


print(is_mail("aaa@mom.fr"))