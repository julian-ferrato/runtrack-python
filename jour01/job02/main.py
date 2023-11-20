print(10 + 3)

import string

alphabet_minuscules = string.ascii_lowercase
print(alphabet_minuscules)

alphabet_majuscules = string.ascii_uppercase
print(alphabet_majuscules)

alphabet_minuscules_inverse = string.ascii_lowercase[::-1]
print(alphabet_minuscules_inverse)

alphabet_majuscules_inverse = string.ascii_uppercase[::-1]
print(alphabet_majuscules_inverse)

ma_string = "je suis une String"
print(ma_string)

num1 = 40
num2 = 2

somme = num1 + num2

print("La somme de num1 et num2 est :", somme)


num1 = 3
num2 = 14

produit = num1 * num2

print("Le produit de num1 et num2 est :", produit)


nom_produit = "Ordinateur portable"
prix_unitaire = 1200.0
quantite_stock = 50

print("Informations du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} €")
print(f"Quantité en stock : {quantite_stock}")

achat = int(input("Combien de produits souhaitez-vous acheter ? "))
quantite_stock += achat

prix_unitaire *= 1.10  

print("\nInformations mises à jour du produit après achat et inflation :")
print(f"Nom du produit : {nom_produit}")
print(f"Nouveau prix unitaire après inflation : {prix_unitaire:.2f} €")
print(f"Nouvelle quantité en stock : {quantite_stock}")


montant_initial = 10000  
taux_rendement_annuel = 5  


gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Le gain annuel avec un taux de rendement de {taux_rendement_annuel}% est de : {gain_annuel} euros")


montant_initial += 5000  
taux_rendement_annuel += 2  
nouveau_gain_annuel = montant_initial * (taux_rendement_annuel / 100)
print(f"Après l'augmentation du capital et du taux de rendement, le gain annuel est de : {nouveau_gain_annuel} euros")


retrait = montant_initial * 0.10  
montant_initial -= retrait
taux_rendement_annuel -= 1 

nouveau_gain_annuel_apres_retrait = montant_initial * (taux_rendement_annuel / 100)
print(f"Après le retrait et la diminution du taux de rendement, le nouveau gain annuel est de : {nouveau_gain_annuel_apres_retrait} euros")



chaine = (input("Entrer une chaîne (un mot ou une phrase par exemple : "))

if 'e' in chaine:
    print("La chaîne contient le caractère 'e'")
else:
    print("La chaîne ne contient pas le caractère 'e'")
