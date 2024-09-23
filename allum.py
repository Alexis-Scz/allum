import time

nb_allumette = 20
joueur = 1
seconde = 5

print("Début de la partie : ")
print(" I " * nb_allumette)

while nb_allumette > 0:
    allumette_retire = int(input("Combien d'allum tu veux retirer le sang ? (entre 1 et 3)"))
    if allumette_retire <= nb_allumette:
        if 1 <= allumette_retire <= 3 :
            nb_allumette = nb_allumette - allumette_retire
            print(" I " * nb_allumette)
            joueur += 1
            print("Tour du joueur N°", str(joueur % 2 + 1))
        else:
            print("azy abuse pas je t'ai dit entre 1 et 3 là")
    else:
        print("Abuse pas frérot retire pas trop")

print("Joueur", str(joueur % 2 + 1), "gagne ")

while seconde > 0:
        seconde = seconde - 1    
        print("Fermeture dans : ", str(seconde))
        time.sleep(1)      
