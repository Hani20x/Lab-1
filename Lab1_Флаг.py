def generate_swiss_flag():
    # Красный фон с белым крестом
    red = '\033[41m  \033[0m'  # Красный фон
    white = '\033[47m  \033[0m'  # Белый фон
    
    flag = [
        [red] * 11,
        [red] * 4 + [white] * 3 + [red] * 4,
        [red] * 4 + [white] * 3 + [red] * 4,
        [red] * 2 + [white] * 7 + [red] * 2,
        [red] * 2 + [white] * 7 + [red] * 2,
        [red] * 4 + [white] * 3 + [red] * 4,
        [red] * 4 + [white] * 3 + [red] * 4,
        [red] * 11,
    ]

    for row in flag:
        print(''.join(row))


generate_swiss_flag()
