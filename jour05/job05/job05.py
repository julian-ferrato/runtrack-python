def decale_cesar(message, decalage):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    resultat = ''
    
    for lettre in message:
        if lettre.isalpha():
            index = (alphabet.index(lettre.lower()) + decalage) % 26
            if lettre.isupper():
                resultat += alphabet[index].upper()
            else:
                resultat += alphabet[index]
        else:
            resultat += lettre
    
    print(resultat) 
    return resultat

decale_cesar("C", 3)
