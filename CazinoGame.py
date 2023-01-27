import math
import os
import package.learn as module
import random

if __name__=="__main__":
    print("__________________BIENVENU DANS ZCASINO_____________")
    is_true = True
    argent_mise = 0
    val = 0
    while is_true:
        try:
            argent_mise = int(input("Entrez votre argent a mise pour le jeu "))
            val = int(input("Entrez le numero mise entre 0 et 49 "))
            if argent_mise <= 0:
                raise ValueError("argent inferieure ou égale à 0")
            elif val < 0 or val > 49:
                raise ValueError("Valeur misee invalide")
        except ValueError as e:
            print(e)
        else:
            is_true = False
            
    nbre = random.randrange(50)
    if nbre == val:
        argent_mise = argent_mise*3
        print("Vous avez gagné ! Votre compte actuellemnt ",argent_mise," $")
    elif nbre%2 == val%2:
        argent_mise = (math.ceil(argent_mise/2))
        print("Vous avez partiellement gagné ! Votre compte actuellemnt ",argent_mise)
    else:
        argent_mise = 0
        print("You are lost ",argent_mise)
    
    os.system("pause")


