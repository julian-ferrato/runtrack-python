def distance_toilettes(marches, hauteur_marche):
    distance = (marches * hauteur_marche * 2) / 100  
    distance_semaine = distance * 5 * 7  
    return distance_semaine

nb_marches = 100
hauteur_marche_cm = 20
distance_totale = distance_toilettes(nb_marches, hauteur_marche_cm)
print(f"Pour {nb_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
