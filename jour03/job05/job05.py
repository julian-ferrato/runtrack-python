def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  
            return num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur non reconnu"

resultat_addition = calcule(1, '+', 12)
resultat_multiplication = calcule(9, '*', 1)
resultat_division = calcule(25, '/', 5)

print("Résultat de l'addition :", resultat_addition)
print("Résultat de la multiplication :", resultat_multiplication)
print("Résultat de la division :", resultat_division)
