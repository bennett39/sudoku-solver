from models import Node, Grid

def main():
    g = Grid()
    get_user_grid(g)
    g.print_grid()

    #  p = Grid()
    #  p.print_grid()


def get_user_grid(g):
    more_values = True

    while more_values:
        prompt = input("Do you have values to add to the grid (y/n)? ")
        
        if prompt == 'n' or prompt == 'N':
            more_values = False
            break
        elif prompt == 'y' or prompt == 'Y':
            u = get_user_input()
            g.nodes[u['id']].set_val(u['val'])
        else:
            print("Invalid input. Usage: 'y' or 'n'.")


def get_user_input():
    try:
        row = int(input("Row: ")) - 1 # Row/col numbers start at 0
        if not 0 <= row < 9:
            raise ValueError

        col = int(input("Column: ")) - 1
        if not 0 <= col < 9:
            raise ValueError

        val = int(input("Value: "))
        if not 0 < val <= 9:
            raise ValueError

        if 0 <= row < 9 and 0 <= col < 9 and 0 < val <= 9:
            return {'id': row * 9 + col, 'val': val}

    except ValueError:
        print("That's not a valid entry. Must be 1-9.")
    
    get_user_input()

        
if __name__ == "__main__":
    main()
