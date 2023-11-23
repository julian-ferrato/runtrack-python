def supprimer_doublons(liste):
    liste_sans_doublons = []
    for element in liste:
        est_present = False
        for item in liste_sans_doublons:
            if item == element:
                est_present = True
                break
        
        if not est_present:
            liste_sans_doublons = liste_sans_doublons + [element]
    
    return liste_sans_doublons

liste_originale = [10,20,30,20,10,50,60,40,80,50,40]
resultat = supprimer_doublons(liste_originale)
print(resultat)
