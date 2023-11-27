def tapis_diagonale(n):
    for i in range(n+1):
        for j in range(n+1):
            if j == n - i:
                print("", end=" ")
            else:
                print("#", end=" ")
        print()

tapis_diagonale(10)
