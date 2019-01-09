class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.box = None

    def put_value(self, val):
        self.val = val

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_up(self, up):
        self.up = up

    def set_box(self, box):
        self.box = box

    def set_down(self, down):
        self.down = down


class Grid():
    def __init__(self):
        for i in range(9):
            for j in range(9):
                pass


def main():
    m = Node(1, 1)
    m.put_value(8)

    n = Node(2, 2)
    n.put_value(9)

    n.set_left(m)
    m.set_right(n)

    print(n.val)
    print(n.left.val)
    print(m.val)
    print(m.right.val)


if __name__ == "__main__":
    main()
