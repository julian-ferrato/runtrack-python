while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro : "))
        if N > 0:
            break
        else:
            print("Veuillez saisir un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez saisir un nombre valide.")

for i in range(1, N + 1):
    print(f"Table de multiplication de {i}:")
    for j in range(1, 11):
        resultat = i * j
        print(f"{i} x {j} = {resultat}")
    print()  
