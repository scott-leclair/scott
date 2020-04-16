"""
Auteur: Scott Le Clair
créé le 2020-04-13

Ce programme, avec l'aide de la fonction "trouveNoeudLeger",
utilise une sorte d'algorithme Djikstra pour trouver la voie le plus
efficace dans un diagramme des noeuds.
"""

monGraphe = { "START": { "A":10 }, "A" : { "C":20 }, "B": { "A":1 },
              "C" : { "B" : 1, "FIN" : 30 }, "FIN": None }

couts = { "A":10 ,  "B" : float("inf"), "C":float("inf"), "FIN" : float("inf") }

parents = { "A" : "START", "B": None, "C" : None, "FIN": None }

dejaTraite = []

###############################################################
#trouveNoeudLeger( c, dt )
#
#Description: Utilise deux arguments pour trouver la voie la plus
#           # efficace dans un diagramme des noeuds.
#           # 
#
#Paramètres:
#   #c: Un dictionnaire qui décrit les poids des voies en rélation
#           # au début.
#
#   #dt: Une liste des noeuds déjà traitée.
#
#
#Retourne:
#   #Si la recherche réussit il retourne True.
#
###############################################################

def trouveNoeudLeger( c, dt ):
    noeudPlusLeger=None
    poidsPlusLeger=float("inf")
    for n in c.keys():
        if n not in dt:
           if c[n]<poidsPlusLeger:
               poidsPlusLeger=c[n]
               noeudPlusLeger=n
    return noeudPlusLeger

       
noeud = trouveNoeudLeger( couts, dejaTraite )
while noeud is not None:
    cout = couts[noeud]
    voisins = monGraphe[noeud]
    if voisins is not None:
        for n in voisins.keys():
            nouveauCout = cout + voisins[n]
            if couts[n] > nouveauCout:
                couts[n] = nouveauCout
                parents[n] = noeud
    dejaTraite.append(noeud)
    noeud = trouveNoeudLeger(couts, dejaTraite )

print( "La route la plus courte est : ", couts["FIN"] )
piste = ["FIN"]
cle = "FIN"
while cle != "START":
    piste= [parents[cle]] + piste
    cle = parents[cle]
print( piste )
