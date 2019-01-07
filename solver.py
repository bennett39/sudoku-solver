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
        self.rows[row-1][col-1] = value # TODO - Remove "-1", refactor

    def get_rows(self):
        return self.rows


# Functions

def main():
    g = get_user_grid()
    g.print_grid()

    p = possibilities_init()
    #  check_horizontal(g, p)
    p.print_grid()


def check_horizontal(g, p):
    rows = g.get_rows()

    for i in range(len(rows)):
        s = set(all_values).intersection(rows[i])
        
        for element in s:
            all_values.remove(element)

        for j in range(len(rows[i])):
            p.add_value(all_values, i+1, j+1)


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


def possibilities_init():
    p = Grid()
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rows = p.get_rows()

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            p.add_value(all_values, i+1, j+1)

    return p


if __name__ == "__main__":
    main()
