# Class definition

class Grid():
    def __init__(self):
        self.rows = []
        for i in range(9):
            self.rows.append([])
            for j in range(9):
                self.rows[i].append(None)
    
    def print_grid(self):
        for row in self.rows:
            for value in row:
                print(f"{value}", end='\t')
            print()
        print("---")

    def put_value(self, value, row, col):
        self.rows[row][col] = value 


# Functions

def main():
    g = get_user_grid()
    g.print_grid()

    p = possibilities_init()
    check_horizontal(g, p)
    p.print_grid()


def check_horizontal(g, p):
    for i in range(len(g.rows)):
        for j in range(len(g.rows[i])):
            for k in range(len(p.rows[i])):
                if g.rows[i][j] in p.rows[i][k]:
                    p.rows[i][k].remove(g.rows[i][j])


def get_user_grid():
    g = Grid()
    more_values = True

    while more_values:
        prompt = input("Do you have values to add to the grid (y/n)? ")

        if prompt == 'n' or prompt == 'N':
            more_values = False
            break
        elif prompt == 'y' or prompt == 'Y':
            u = get_user_input()
            g.put_value(u['val'], u['row']-1, u['col']-1)
        else:
            print("Invalid input. Usage: 'y' or 'n'.")


    return g


def get_user_input():
    try:
        row = int(input("Row: "))
        col = int(input("Column: "))
        val = int(input("Value: "))
        if val > 0 and val <= 9:
            return {'row': row, 'col': col, 'val': val}
    except ValueError:
        print("That's not a number.")
        
    print("Invalid entry. Must be an integer 0-9.")
    get_user_input()


def possibilities_init():
    p = Grid()

    for i in range(len(p.rows)):
        for j in range(len(p.rows[i])):
            # Cannot create the list as a variable bc they'll all be 
            # linked as references to that same variable.
            p.put_value([1, 2, 3, 4, 5, 6, 7, 8, 9], i, j)

    return p


if __name__ == "__main__":
    main()
