"""
Auteur: Scott Le Clair
créé le 2020-04-02

Ce programme, avec l'aide de la fonction "recherche", accepte deux noms (nomSource, nomDestination)
donnés par l'utilisateur, et utilise monGraphe pour rechercher si il existe une rélation entre
les deux noms donnés.
"""

from collections import deque

###############################################################
#recherche( nomSource, nomDestination, monGraphe )
#
#Description: Utilise trois arguments pour utiliser un recherche
#           # en largeur dans un graphe et trouver un relation
#           # entre deux noms.
#
#Paramètres:
#   #nomSource: Un string qui désigne le nom avec lequel on commence
#           #   la recherche.
#
#   #nomDestination: Un string qui désigne le nom avec lequel la recherche
#           #        s'arrête, la destination.
#
#   #monGraphe: Un dictionnaire qui contient des noms associés avec
#           #   listes des rélations.
#
#Retourne:
#   #Si la recherche réussit il retourne True.
#
#   #Si nomDestination n'est pas dans monGraphe, la fonction retourne False.
#
#   #Si OSError, retourne False.
###############################################################

def recherche( nomSource, nomDestination, monGraphe ):

    try:
        maQueue = deque()
        visite = []
        noeudCourant = nomSource
        maQueue.append(nomSource)
#visiter (visite) et explorer (maQueue)
        while maQueue:

            if noeudCourant not in visite:

                if noeudCourant == nomDestination:
                    return True
                else:
                    maQueue.extend(monGraphe[noeudCourant])
                    visite.append(noeudCourant)
            noeudCourant = maQueue.popleft()

        if nomDestination not in monGraphe:
            return False

    except OSError:
        return False

#Programme principal

fortnite = { "Paul":[ "Connor", "Seb A." ], "Connor":[ "Dylan", "Austin", "Brandon", "Paul" ],
             "Dylan":[ "Kyler", "Connor" ], "Kyler":[ "Dylan", "Brandon" ],
             "Brandon":[ "Kyler", "Seb A.", "Connor" ], "Seb A.":[ "Brandon", "Paul", "Austin" ],
             "Austin":[ "Kyler", "Seb A.", "Connor"]
             }

minecraft = { "Paul":[ "Martin", "Scott" ], "Martin":[ "Lentini", "Paul" ],
              "Lentini":[ "Seb L.", "Martin" ], "Seb L.":[ "Lentini", "Noah", "Scott", "Martin" ],
              "Noah":[ "Scott", "Seb L." ], "Scott":[ "Noah", "Paul", "Martin", "Seb L." ]
              }

#Initializer variables
nomSource = ""
nomDestination = ""
verification = False
interruption = False

print( "\n Appuyer sur cntrl-c n'importe quand pour fermer la programme \n" )
print( "--------------------------------------------------------------\n" )

#while True:
 #   if interruption == True:
  #      break
    
    #Remettre variables    
    #nomSource = ""
    #nomDestination = ""
    #verification = False

while verification == False:
    try:
        if nomSource != "":
            while nomDestination == "":
                nomDestination = input( "Entre le deuxieme nom : " ) 
                nomDestination = nomDestination.strip()
                if nomDestination == "":
                    print( "ERREUR : aucune valeur" )
                if nomDestination == nomSource:
                    nomDestination = ""
                    print( "ERREUR : SVP entrer un nom différent" )

        while nomSource == "":
            nomSource = input( "Entre le premier nom : " ) 
            nomSource = nomSource.strip()
            if nomSource == "":
                print( "ERREUR : aucune valeur" )

        if nomSource and nomDestination != "":
            verification = True

    except KeyboardInterrupt:
        print( "Interruption clavière, fin du programme")
        interruption = True
        break

if not interruption == True:
    try:
        try:
            try:
                if recherche( nomSource, nomDestination, fortnite ) == True:
                    print( "Oui ... fortnite" )
                else:
                    if recherche( nomSource, nomDestination, minecraft ) == True:
                        print( "Oui ... minecraft" )
                    else:
                        print( "Aucune rélation" )
                    
            except KeyError:
                if recherche( nomSource, nomDestination, minecraft ) == True:
                    print( "Oui ... minecraft" )
                else:
                    print( "Aucune rélation" )

        except KeyError:
            déclencheur = recherche( nomSource, nomDestination, fortnite )
            print( "Aucune rélation" )
                
    except KeyError:
        print( "Un ou deux des noms est/sont introuvable(s), essaye encore" )

    #except KeyboardInterrupt:
     #   print( "Interruption clavière, fin du programme")
      #  break

    
                    
                    
                    
                
        
        
