def tri_bulles(arr):
    n = 0
    for x in arr:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def arrondir_et_trier_liste(liste):
    arr = []  
    n = 0
    for elem in liste:
        n += 1
        arr = arr + [int(elem + 0.5)]  

    tri_bulles(arr) 

    return arr  
liste_initiale = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

resultat = arrondir_et_trier_liste(liste_initiale)

print("Liste arrondie et triée :", resultat)
