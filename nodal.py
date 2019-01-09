class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.val = None

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
        self.nodes = []
        for i in range(9):
            for j in range(9):
                self.nodes.append(Node(i, j))

    def print_nodes(self):
        i = 0
        for element in self.nodes:
            if element.row != i:
                print()
                i = element.row
            print(element.val, end="\t")
        print()


def main():
    g = Grid()
    g.print_nodes()


if __name__ == "__main__":
    main()
