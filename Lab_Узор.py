def generate_pattern_j(rows, columns):
    pattern = "oo"
    for _ in range(rows):
        print((pattern + " ") * columns)


generate_pattern_j(5, 5)  # Узоры 5x5
