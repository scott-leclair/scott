from collections import deque

# exemple qui exploite dequeue comme une queue
# dans cet exemple on insère à la gauche et ont quitte de la droite

maqueue = deque()  #creer une queue vide
maqueue.appendleft("Paul")    # ajoute à la gauche de la queue
print( maqueue ) # voir le contenu de la queue
uneListe = ["Bob", "Joe", "Jim"]
maqueue.extendleft(uneListe)  # ajouter plusieurs valeur dans un coup
print( maqueue ) # voir le contenu de la queue
# vider la queue
while maqueue:
    v=maqueue.pop()   # enleve de la droite de la queue
    print(v, "quitte la queue.  Il en reste ", len(maqueue))
