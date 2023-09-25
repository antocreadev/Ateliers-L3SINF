from numpy import array, searchsorted,size, where, int64, ndarray, ndenumerate, shape, zeros

liste_sommets = [0,1,2,3,4]
lsite_arcs = [(0,1), (0,2), (1,2),(1,4), (2,3), (3,4), (4,2)]
lsite_arcs_pond = [(0,1, 33), (0,2, 44), (1,2, 55),(1,4, 38), (2,3, 20), (3,4,66), (4,2,12)]


def matriceAdjacence(sommets,arcs) : 
    result = zeros((len(sommets),len(sommets) ), dtype=int64)
    for k in range(len(arcs)) : 
        colonne = arcs[k][0]
        ligne = arcs[k][1]
        result[colonne][ligne] = 1
    return result
print(matriceAdjacence(liste_sommets, lsite_arcs))

def matriceAdjacence_v2(sommets,arcs) : 
    result = zeros((len(sommets),len(sommets) ), dtype=int64)
    for row, col in arcs: 
        result[row][col] = 1
    return result
print(matriceAdjacence_v2(liste_sommets, lsite_arcs))

def matriceAdjacencePond(sommets,arcs) : 
    result = zeros((len(sommets),len(sommets) ), dtype=int64)
    for row, col, pond in arcs: 
        result[row][col] = pond
    return result
print(matriceAdjacencePond(liste_sommets, lsite_arcs_pond))

def lireMatriceFichier(nomfichier) : 
    pass
