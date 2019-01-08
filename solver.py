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
        self.rows[row-1][col-1] = value # TODO - Remove "-1", refactor

    def get_rows(self):
        return self.rows


# Functions

def main():
    g = get_user_grid()
    g.print_grid()

    p = possibilities_init()
    check_horizontal(g, p)
    p.print_grid()


def check_horizontal(g, p):
    g_rows = g.get_rows()
    p_rows = p.get_rows()

    for i in range(len(g_rows)):
        for j in range(len(g_rows[i])):
            for k in range(len(p_rows[i])):
                # TODO - Figure out what's wrong with line 45
                print(p_rows[i][k])
                if g_rows[i][j] in p_rows[i][k]:
                    p.put_value(p_rows[i][k].remove(g_rows[i][j]), \
                            i+1,j+1)


def get_user_grid():
    g = Grid()
    more_values = True

    while more_values:
        prompt = input("Do you have values to add to the grid (y/n)? ")

        # TODO - Add more error checking for keyboard entries not n/N
        if prompt == 'n' or prompt == 'N':
            more_values = False
            break
        else:
            u = get_user_input()
            g.put_value(u['val'], u['row'], u['col'])

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
    rows = p.get_rows()

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            # Cannot create the list as a variable bc they'll all be 
            # linked as references to that same variable.
            p.put_value([1, 2, 3, 4, 5, 6, 7, 8, 9], i+1, j+1)

    return p


if __name__ == "__main__":
    main()
