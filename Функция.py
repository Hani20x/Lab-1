def plot_function():
    max_height = 9  # Минимум 9 строк
    max_width = 30  # Ширина графика
    print(" " * 5 + "y = x / 3")  # Подпись графика

    for y in range(max_height, -1, -1):
        line = ""
        for x in range(max_width + 1):
            if y == round(x / 3):
                line += "*"
            else:
                line += " "
        print(line)


plot_function()
