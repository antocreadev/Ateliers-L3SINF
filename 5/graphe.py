from numpy import array, searchsorted,size, where, int64, ndarray, ndenumerate, shape, zeros

liste_sommets = [0,1,2,3,4]
lsite_arcs = [(0,1), (0,2), (1,2),(1,4), (2,3), (3,4), (4,2)]
lsite_arcs_symetrique = [(1,2), (1,3), (1,4),(2,1), (2,4), (3,1), (3,4), (4,1), (4,2), (4,3)]
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

print("\n", "----------", "\n")

def lireMatriceFichier(nomfichier) : 
    with open(nomfichier,"r") as file : #with : Le fichier est automatiquement fermé à la fin du bloc "with"
        return array([ligne.rstrip("\n") for ligne in file])
# print(lireMatriceFichier("./5/graph0.txt"))
 
def tousLesSommets(mat) : 
    return [i for i in range(mat.shape[0])]

# print(tousLesSommets(matriceAdjacencePond(liste_sommets, lsite_arcs_pond)))

# matrice.shape -> renvoie ligne, colonne (row,col)
def listeArcs(mat) : 
    row, col = mat.shape 
    result = []
    for k in range(row) : 
        for i in range(col) : 
            if (mat[k][i] != 0) : 
                result.append((k, i))
    return result

print("arcs : ")          
print(listeArcs(matriceAdjacencePond(liste_sommets, lsite_arcs_pond)))

def est_symetrique(mat) : 
    row, col = mat.shape
    for k in range(row) : 
        for i in range(col) : 
            if mat[k][i] != mat[i][k] : 
                return False
    return True

def matriceIncidence(mat) :
    pass

matriceIncidence(matriceAdjacence(liste_sommets, lsite_arcs))

# def matriceIncidence(mat) :
#     row, col = mat.shape 
#     arcs = 0
#     sommets = row 
#     for k in range(row) : 
#         for i in range(col) : 
#             if (mat[k][i] >0) : 
#                 arcs += 1
#     if est_symetrique(mat) : 
#         arcs = arcs//2
#     mat_incidence = zeros((sommets, arcs))
#     # mat_incidence = []
#     # for k in range(sommets) :
#     #     mat_incidence.append([])
#     #     for i in range(arcs) : 
#     #         mat_incidence[k].append(0)
#     j= 0 
#     for x in range(row) : 
#         for y in range(col) : 
#             if (mat[x][y] ==1) : 
#                 mat_incidence[x][j] = 1
#                 mat_incidence[y][x] = -1
#                 j += 1
#     return mat_incidence
# print(matriceIncidence(matriceAdjacence(liste_sommets, lsite_arcs)))

def matriceIncidence_v2(mat) :
    all_arcs = listeArcs(mat)
    nombre_arc = len(all_arcs)
    mat_incidence = zeros(( mat.shape[0], nombre_arc))
    for arc in range(nombre_arc) :
        mat_incidence[all_arcs[arc][0]][arc] = 1
        mat_incidence[all_arcs[arc][1]][arc] = -1
        pass
    return mat_incidence

print(matriceIncidence_v2(matriceAdjacence(liste_sommets, lsite_arcs)))
