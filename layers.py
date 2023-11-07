def create_layers(layers):
    """
    Create an output according to the given number of layers, with 'A' as the outermost layer
    and subsequent layers moving inward with the next letters in the alphabet.
    """
    # Calculate the size of the grid
    size = layers * 2 - 1
    grid = [[" " for _ in range(size)] for _ in range(size)]

    # Fill the grid with characters, starting from the outer layer
    for i in range(layers):
        character = chr(ord("A") + layers - i - 1)
        # Top and bottom
        for j in range(i, size - i):
            grid[i][j] = character
            grid[size - i - 1][j] = character
        # Left and right
        for j in range(i + 1, size - i - 1):
            grid[j][i] = character
            grid[j][size - i - 1] = character

    # Convert the grid to a string for printing
    return "\n".join("".join(row) for row in grid)


if __name__ == "__main__":
    while True:
        layers = input("How many layers (1-26), exit with 0: ")
        if layers.isnumeric() and int(layers) > 0 and int(layers) <= 26:
            layers = int(layers)
            print("You have chosen {} layers.".format(layers))
            print(create_layers(layers))
        elif layers == "0":
            print("Exiting...")
            break
        else:
            print("Invalid input. Try again." + "\n")
