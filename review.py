
"""
 les valeurs de x et y. Lorsque x et y sont petits, Python les met en cache et les réutilise, ce qui fait que leurs adresses mémoire sont les mêmes, d'où la condition if x is y est vraie. Cependant, une fois que les valeurs de x et y dépassent la limite de mise en cache des petits entiers, leurs adresses mémoire diffèrent, et la condition if x is y devient fausse, entraînant la sortie de la boucle.
"""

x = 0
y = 0

while True:
    x += 1
    y += 1

    if x is y:
        print(f"{x}: equal! {id(x)} & {id(y)}")
    else:
        print(f"{x} & {y}: not equal! {id(x)} & {id(y)}")
        break
