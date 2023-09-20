from random import randint
from time import perf_counter
from matplotlib import pyplot 

def sort_list(liste: list)-> list:
    liste_copy = list(liste)
    return [liste_copy.pop(liste_copy.index(min(liste_copy))) for i in range(len(liste_copy))]
    # .pop(index) -> supprime et renvoie la valeur supprimé 
   
   
   
# functions
def perf(function1 : callable, function2 : callable, taille_list : int):
    moyenne_elapsed_time_pc_mix_list = 0
    moyenne_elapsed_time_pc_mix_suffle = 0
    LIST_TEST = [randint(0,1)] * taille_list
    for k in range(1, 11) : 
        #fucntion 1
        start_pc_mix_list = perf_counter()
        function1(LIST_TEST)
        end_pc_mix_list = perf_counter() 
        elapsed_time_pc_mix_list = end_pc_mix_list-start_pc_mix_list 
        moyenne_elapsed_time_pc_mix_list += elapsed_time_pc_mix_list
    
        # function 2
        start_pc_perf_suffle = perf_counter()
        function2(LIST_TEST)
        end_pc_perf_shuffle = perf_counter() 
        elapsed_time_pc_suffle = end_pc_perf_shuffle-start_pc_perf_suffle
        moyenne_elapsed_time_pc_mix_suffle += elapsed_time_pc_suffle 
    return [moyenne_elapsed_time_pc_mix_list, moyenne_elapsed_time_pc_mix_suffle]   
   
def main() : 
    TEMPS_EXEC = [perf(sorted, sort_list, 10), perf(sorted, sort_list, 50), perf(sorted, sort_list, 500), perf(sorted, sort_list, 5000), perf(sorted, sort_list, 10000)]
    
    TEMPS_EXEC_SORTED = [TEMPS_EXEC[0][0], TEMPS_EXEC[1][0], TEMPS_EXEC[2][0], TEMPS_EXEC[3][0], TEMPS_EXEC[4][0]]
    
    TEMPS_EXEC_SORT_LIST = [TEMPS_EXEC[0][1], TEMPS_EXEC[1][1], TEMPS_EXEC[2][1], TEMPS_EXEC[3][1], TEMPS_EXEC[4][1]]
    
    NOMBRE_ELEMENT =[10, 50, 500, 5000, 10000] 
    # x_axis_list_mix = numpy.arange(0,moyenne_elapsed_time_pc_mix_list/100,0.0000001) #(debut, fin, pas)
    fig, ax = pyplot.subplots() 
    ax.plot(NOMBRE_ELEMENT,TEMPS_EXEC_SORTED, 'r*-', label='MIX_LIST')  #(abscisse, ordonnée, couleur, label )
    ax.plot(NOMBRE_ELEMENT,TEMPS_EXEC_SORT_LIST,'g*-', label='SUFFLE') 
    
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y', 
        title='SUFFLE, MIX_LIST') 
    
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 
    fig.savefig("temps_exec.png") 
    pyplot.show() 
    
main()
print(sort_list([88,3,6,9,8,9,7,66,1]))

print(perf(sorted, sort_list, 100))

