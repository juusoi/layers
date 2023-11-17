from layers import create_layers


def main():
    while True:
        layers = input("How many layers (1-26), exit with 0: ")
        if layers.isnumeric() and int(layers) == 0:
            print("Exiting...")
            break
        elif layers.isnumeric() and 0 < int(layers) <= 26:
            layers = int(layers)
            print("You have chosen {} layers.".format(layers))
            print(create_layers(layers))
        else:
            print("Invalid input. Try again." + "\n")


if __name__ == "__main__":
    main()
