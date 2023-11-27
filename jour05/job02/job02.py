def draw_rectangle(width, height):
    horizontal_line = '|' + '-' * (width - 2) + '|'
    print(horizontal_line) 

    for _ in range(height - 2):
        vertical_line = '|' + ' ' * (width - 2) + '|'
        print(vertical_line)  

    if height > 1:
        print(horizontal_line)  

draw_rectangle(10, 3)
