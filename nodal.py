class Node():
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col


class Grid():
    def __init__(self):
        pass


def main():
    n = Node(1, 2, 3)
    print(n.val)
    print(n.row)
    print(n.col)


if __name__ == "__main__":
    main()
