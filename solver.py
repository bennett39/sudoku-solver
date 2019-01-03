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
    # TODO - Use get_user_input() to assign values in Grid
    return g

def get_user_input(i, j):
    entry = input(f"Row {i+1}, Col {j+1}: ")

    try:
        number = int(entry)
        if number >= 0 and number <= 9:
            return number
    except ValueError:
        print("That's not a number.")
        
    print("Invalid entry. Must be an integer 0-9.")
    get_user_input(i, j)


if __name__ == "__main__":
    main()
