def my_sort(arr):
    count = 0 
    sorted = False 

    while not sorted:  
        sorted = True  

        for i in range(len(arr) - 1): 
            if arr[i] > arr[i + 1]:  
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  
                sorted = False  
                count += 1  

    return arr, count 

liste = [1, 12, 9, 4, 5]
resultat, coups = my_sort(liste)
print("Liste triée :", resultat)
print("Nombre de permutations :", coups)
