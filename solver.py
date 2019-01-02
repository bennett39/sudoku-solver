def main():
    g = get_user_grid()
    print(g)


def get_user_grid():
    rows = []
    for i in range(9):
        rows.append([])
        print(rows[i]) 
        for j in range(9):
            rows[i].append(input(f"Row {i+1}, Col {j+1}: "))
    return rows


if __name__ == "__main__":
    main()
