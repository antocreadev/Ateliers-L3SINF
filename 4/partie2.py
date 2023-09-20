# Import 
from partie1 import mix_list, extract_elements_list
from random import shuffle
from time import perf_counter
from matplotlib import pyplot 
import numpy 
import random

# functions
def perf_mix(mix_list : callable, shuffle : callable, taille_list : int):
    moyenne_elapsed_time_pc_mix_list = 0
    moyenne_elapsed_time_pc_mix_suffle = 0
    LIST_TEST = [random.randint(0,1)] * taille_list
    for k in range(1, 101) : 
        # mix_list()
        start_pc_mix_list = perf_counter()
        mix_list(LIST_TEST)
        end_pc_mix_list = perf_counter() 
        elapsed_time_pc_mix_list = end_pc_mix_list-start_pc_mix_list 
        moyenne_elapsed_time_pc_mix_list += elapsed_time_pc_mix_list
    
        # shuffle
        start_pc_perf_suffle = perf_counter()
        shuffle(LIST_TEST)
        end_pc_perf_shuffle = perf_counter() 
        elapsed_time_pc_suffle = end_pc_perf_shuffle-start_pc_perf_suffle
        moyenne_elapsed_time_pc_mix_suffle += elapsed_time_pc_suffle 
    return [moyenne_elapsed_time_pc_mix_list, moyenne_elapsed_time_pc_mix_suffle]

def main() : 
    TEMPS_EXEC = [perf_mix(mix_list, shuffle, 10), perf_mix(mix_list, shuffle, 500), perf_mix(mix_list, shuffle, 5000), perf_mix(mix_list, shuffle, 50000), perf_mix(mix_list, shuffle, 100000)]
    
    TEMPS_EXEC_MIX_LIST = [TEMPS_EXEC[0][0], TEMPS_EXEC[1][0], TEMPS_EXEC[2][0], TEMPS_EXEC[3][0], TEMPS_EXEC[4][0]]
    
    TEMPS_EXEC_SHUFFLE = [TEMPS_EXEC[0][1], TEMPS_EXEC[1][1], TEMPS_EXEC[2][1], TEMPS_EXEC[3][1], TEMPS_EXEC[4][1]]
    
    NOMBRE_ELEMENT =[10, 500, 5000, 50000, 100000] 
    # x_axis_list_mix = numpy.arange(0,moyenne_elapsed_time_pc_mix_list/100,0.0000001) #(debut, fin, pas)
    fig, ax = pyplot.subplots() 
    ax.plot(NOMBRE_ELEMENT,TEMPS_EXEC_MIX_LIST, 'r*-', label='MIX_LIST')  #(abscisse, ordonnée, couleur, label )
    ax.plot(NOMBRE_ELEMENT,TEMPS_EXEC_SHUFFLE,'g*-', label='SUFFLE') 
    
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y', 
        title='SUFFLE, MIX_LIST') 
    
    ax.legend(loc='upper center', shadow=True, fontsize='x-large') 
    fig.savefig("temps_exec_shuffle_mixList.png") 
    pyplot.show() 
    
main()