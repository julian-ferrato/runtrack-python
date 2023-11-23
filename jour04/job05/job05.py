def remplacer_element(liste):
        print("Première liste :", liste)
        
        print("Deuxième valeur de la première liste :", liste[1])

        liste[3] = liste[2] + liste[4]
        print("Tableau après remplacement de L[3] :", liste)

        print("Dernière valeur de la deuxième liste :", liste[-1])

L = [1, 2, 3, 4, 5]

remplacer_element(L)
