import random
# Reset previousWolf List every X turns
RESET = 5

hunterTracker = [0 for i in range(10)]
wolfTracker = [0 for i in range(10)]
specialTracker = [0 for i in range(10)]
allPlayer = list(range(1,11))

previousWolf = []
counter = 0
while True :
    if counter% RESET == 0 :
        previousWolf = []

    counter+=1
   # First wolf must be someone that wasn't already selected in the last X turns
    tempList = list(set(allPlayer) ^ set(previousWolf)) 
    firstWolf = random.choice(tempList) # testing purposes
    wolvesList = [firstWolf]
    tempList2= list(set(allPlayer) ^ set(wolvesList)) 

    # Second wolf can be anyone
    secondWolf = random.choice(tempList2) # testing purposes
    wolvesList.append(secondWolf)
    previousWolf += wolvesList

    # hunter one of left

    hunter = random.choice(list(set(allPlayer) ^ set(wolvesList)))
    print(f"------- Partie {counter} --------")
    print(f"Loup premier tirage :  {firstWolf}, loup deuxième : {secondWolf}, chasseur {hunter}")
    for i in wolvesList:
        wolfTracker[i-1]+=1
    hunterTracker[hunter-1] += 1

    for i in list(set(wolvesList).union(set([hunter]))):
        specialTracker[i-1] += 1

    # Keep track of each special role per player (hunter or wolf)
    print(f"Increment loups   : {wolfTracker}")
    print(f"Increment chasseur: {hunterTracker}")
    print(f"Role special      : {specialTracker}")
    print(f"Ancien loups      : {previousWolf}")

    if input('Stop ? ') == 'y':
        break