for nombre in range(2, 1001):
    est_premier = True
    for diviseur in range(2, int(nombre ** 0.5) + 1):
        if nombre % diviseur == 0:
            est_premier = False
            break
    if est_premier:
        print(nombre)
