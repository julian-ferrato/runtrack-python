def draw_triangle(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        if i == 0:
            print(spaces + '_')
        elif i == (height-1):
            print(spaces + '/' + '_' * (2 * i - 1) + '\\')
        else:
            print(spaces + '/' + ' ' * (2 * i - 1) + '\\')

try:
    user_input = int(input("Entrez la hauteur du triangle : "))
    draw_triangle(user_input)
except ValueError:
    print("Veuillez entrer un nombre entier.")
