"""
Auteur original: Paul Paiement

Modifications par: Scott Le Clair
Date: 2020-03-23

     Descrption: Ce programme simule une file d'attente à un comptoir
                 de service.   Le file d'attente contient des clients
                 ayant un numéro.  Ex: "Client 1", "Client 2", "Client 3".
                 Le programme demande l'information suivante:

                 1) Le nombre d'événements à simuler

                 Suite à cette information, le programme génère des
                 événement à l'aide de nombre alléatoire.  Le événements
                 sont les suivants:
                 
                    typeEvenement est entre 1 et 3 - un client arrive
                    typeEvenement égale 4 - un client se fait servir
                    typeEvenement égale 5 - client à la fin de la file abandonne
                                            

                 Pour chaque événement, le programme doit:

                    afficher un message qui indique l'événement:

                    ex:  client 1 arrive,   client 4 abandonne, client 1 quitte

                    affiche le contenu de la file d'attente.

"""

from collections import deque
import random


# Programme principal

# variables  (vous pouvez ajouter des variables)

nombreDeClients = 0  # le nombre de clients dans la file d'attente
typeEvenement = 0    # 0 = aucun  1 à 3 client arrive
                     # 4 = client servit et 5 client abandonne
noEvenement = 0      # compte le nombre d'événenment
sommeEvenement = 0   # le nombre d'événements à générer
numeroDuProchainClient = 1  # indique le numéro du prochain client

# Demander combien d'événements générer
while True:
    try:
        sommeEvenement = int(input("entre un nombre d'événements"))
        break
    except ValueError:
        while True:
            try:
                sommeEvenement = int(input("entre un nombre d'événements"))
                break
            except ValueError:
                break

# Créer la queue

maQueue = deque()

# Boucle de simulation 
while noEvenement <= sommeEvenement:
    
    # générer un événement
    evenementValide = False
    while not evenementValide:
        typeEvenement=random.randint(1,5)
        if typeEvenement >= 1 and typeEvenement <= 3:
            evenementValide = True
            print("Un nouveau client arrive.", end=' ')
        elif typeEvenement == 4:  # il faut un client dans la queue pour qu'un client se fasse servir
            evenementValide = True
            print("Le client en avant se fait servir.", end=' ')
        elif nombreDeClients > 1:        # il faut plus d'un client pour abandonner
            print("Le client à la fin est frustré et quitte")
            evenementValide = True

    # à ce point il y a un événement a traiter
    if typeEvenement==4 and nombreDeClients > 0:
        # un client se fait servir donc quitte le devant de la file
        maQueue.popleft()
        nombreDeClients-=1

    elif typeEvenement==5 and nombreDeClients > 0:
        # un client abandonne donc quitte la fin de la file
        maQueue.pop()
        nombreDeClients-=1

    else:   # un nouveau client arrive donc l'ajouter à la fin de la file
        maQueue.append(numeroDuProchainClient)
        numeroDuProchainClient+= 1

    noEvenement+= 1
    nombreDeClients+=1
    print(maQueue)
    
print("Fin du programme")
