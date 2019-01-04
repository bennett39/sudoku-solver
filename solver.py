def main():
    g = get_user_grid()
    g.print_grid()


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

    def add_value(self, value, row, col):
        print(f"{value} added at row {row}, column {col}")
        self.rows[row-1][col-1] = value
        

def get_user_grid():
    g = Grid()
    more_values = True

    while more_values:
        prompt = input("Do you have values to add to the grid (y/n)? ")
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
