def ajouter_mangue():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    fruits.insert(2, "Mangue")  
    return fruits

liste_fruits = ajouter_mangue()

print(liste_fruits)
