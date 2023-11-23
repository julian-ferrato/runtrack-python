def tri_bulles(arr):
    n = 0
    for x in arr:
        n += 1

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

liste = [12, 1, 9, 5, 4, 7, 90]
tri_bulles(liste)
print("Liste triée:", liste)
