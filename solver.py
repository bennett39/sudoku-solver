def main():
    g = get_user_grid()
    for row in g:
       print(row)
    
    possible_values = create_grid()
    print(possible_values)

def create_grid():
    rows = []
    for i in range(9):
        rows.append([])
    return rows


def get_user_grid():
    grid = create_grid()
    print(grid)
    for i in range(9):
        for j in range(9):
            grid[i].append(get_user_input(i, j))
    return rows


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
