def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("Le nombre est égal à zéro")

verifier_nombre(112)
verifier_nombre(-9)
verifier_nombre(0)
