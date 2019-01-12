from models import Node, Grid

def main():
    g = Grid()
    get_user_grid(g)

    g.print_grid()
    print()
    g.print_grid('possible')

#  TODO - change to accept a text file instead
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
            g.nodes[u['id']].empty_possibles()
            rm_horizontal(g, g.nodes[u['id']])
            rm_vertical(g, g.nodes[u['id']])
            rm_box(g, g.nodes[u['id']])
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


def rm_horizontal(grid, node):
    for i in range(81):
        if grid.nodes[i].row == node.row:
            grid.nodes[i].rm_possible(node.val)


def rm_vertical(grid, node):
    for i in range(81):
        if grid.nodes[i].col == node.col:
            grid.nodes[i].rm_possible(node.val)


def rm_box(grid, node):
    for i in range(81):
        if grid.nodes[i].box == node.box:
            grid.nodes[i].rm_possible(node.val)


if __name__ == "__main__":
    main()
