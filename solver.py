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
                print(f"{value}\t", end='')
            print()
        print("---")

    def add_value(self, value, row, col):
        self.rows[row-1][col-1] = value
        #  print(f"{value} added at row {row}, column {col}")

    def get_rows(self):
        return self.rows


# Functions

def main():
    g = get_user_grid() # g for "grid", as in "user grid"
    g.print_grid()

    p = Grid() # p as in "possible values"
    check_horizontal(g, p)
    p.print_grid()


def check_horizontal(g, p):
    rows = g.get_rows()

    for row_i in range(len(rows)):
        all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        s = set(all_values).intersection(rows[row_i])
        
        for element in s:
            all_values.remove(element)

        for col_j in range(len(rows[row_i])):
            p.add_value(all_values, row_i+1, col_j+1)


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
            g.add_value(u['val'], u['row'], u['col'])

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


if __name__ == "__main__":
    main()
