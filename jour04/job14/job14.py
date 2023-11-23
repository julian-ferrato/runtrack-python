def my_long_word(longueur, chaine):
    mots = ""
    mot_actuel = ""
    for char in chaine:
        if char != ' ':
            mot_actuel += char
        else:
            longueur_mot = 0
            for _ in mot_actuel:
                longueur_mot += 1

            if longueur_mot > longueur:
                mots += mot_actuel + ' '
            mot_actuel = ""

    longueur_mot = 0
    for _ in mot_actuel:
        longueur_mot += 1

    if longueur_mot > longueur:
        mots += mot_actuel

    return mots

resultat = my_long_word(5, "Kurumi est un personnage dont la personnalité est difficile à cerner. Elle possède une aversion de l'humanité qui se rapproche de la méfiance, qu'elle partage avec la plupart des autres esprits dans leurs débuts.")
print(resultat)
