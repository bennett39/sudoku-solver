class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.right = None
        self.left = None
        self.up = None
        self.down = None

    def put_value(self, val):
        self.val = val


class Grid():
    def __init__(self):
        pass


def main():
    n = Node(1, 1)
    n.put_value(9)
    print(n.val)
    print(n.row)
    print(n.col)


if __name__ == "__main__":
    main()
