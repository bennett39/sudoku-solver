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

    def set_neighbors(self):
        self.neighbors = [self.up, self.right, self.down, self.left]

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
                k = i * 9 + j
                if i != 0:
                    self.nodes[k].set_up(self.nodes[k-9])
                    self.nodes[k-9].set_down(self.nodes[k])
                if j != 0:
                    self.nodes[k].set_left(self.nodes[k-1])
                    self.nodes[k-1].set_right(self.nodes[k])

        for k in range(81):
            self.nodes[k].set_neighbors()

    def print_grid(self):
        r = 0
        for element in self.nodes:
            if element.row != r:
                print()
                r = element.row
            print(element.val, end="\t")
        print()


def main():
    g = Grid()
    g.print_grid()


if __name__ == "__main__":
    main()
