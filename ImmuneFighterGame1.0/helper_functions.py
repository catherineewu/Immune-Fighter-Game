def find_centered_x_coordinate(screen_width, object_width):
    x_coord = (screen_width / 2) - (object_width / 2)
    return x_coord


def main():
    running = True
    while running:
        print(f'Options:\n\t1. Centered X-Coord:\n')
        option = input()
        if option == '1':
            screen_width = int(input("Enter screen width: "))
            object_width = int(input("Enter object width: "))
            x_coord = find_centered_x_coordinate(screen_width, object_width)
            print(f'{x_coord}\n')


if __name__ == "__main__":
    main()

