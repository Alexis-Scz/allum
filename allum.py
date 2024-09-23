import time
print("Début de la partie : ")
nbalum=10
print(" I "* nbalum)
joueur=1
while nbalum>0:
    tej=int(input("Combien d'allum tu veux retirer le sang ? (entre 1 et 3) "))
    if tej<=nbalum:
        if 1<=tej<=3:
            nbalum=nbalum-tej
            print(" I " * nbalum)
            print("")
            if joueur==1:
                joueur=2
            else:
                joueur=1
            print("Tour du joueur N°",str(joueur))
            
        else:
            print("azy abuse pas je t'ai dit entre 1 et 3 là ")
    else:
        print("Abuse pas frérot retire pas trop ")


print("Joueur",str(joueur), "gagne ")
   
a=5
while a>0:
        a=a-1    
        print("Fermeture dans : ", str(a))
        time.sleep(1)                   