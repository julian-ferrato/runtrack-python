def echanger_premier_dernier(liste):
    liste[0], liste[-1] = liste[-1], liste[0] 
    return liste

ma_liste = [1, 2, 3, 4, 5]

print("Liste avant l'échange :", ma_liste)

resultat = echanger_premier_dernier(ma_liste)

print("Liste après l'échange :", resultat)
