def main():
    g = get_user_grid()
    for row in g:
        print(row)


def get_user_grid():
    rows = []
    for i in range(9):
        rows.append([])
        for j in range(9):
            rows[i].append(get_user_input(i, j))
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
