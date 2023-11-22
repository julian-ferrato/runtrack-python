chaine = "abcdefghijklmnopqrstuvwxyz"
longueur_chaine = len(chaine)

for i in range(1, longueur_chaine * 2):
    if i <= longueur_chaine:
        print(chaine[:i].center(longueur_chaine * 2 - 1))
    else:
        print(chaine[:longueur_chaine * 2 - i].center(longueur_chaine * 2 - 1))
