class Node():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.val = None

        self.right = None
        self.left = None
        self.up = None
        self.down = None

        self.box = self.set_box()

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

    def set_down(self, down):
        self.down = down

    def set_box(self):
        if self.row < 3 and self.col < 3: return 1
        elif self.row < 3 and 3 <= self.col < 6: return 2
        elif self.row < 3 and 6 <= self.col: return 3
        elif 3 <= self.row < 6 and self.col < 3: return 4
        elif 3 <= self.row < 6 and 3 <= self.col < 6: return 5
        elif 3 <= self.row < 6 and 6 <= self.col: return 6
        elif 6 <= self.row and self.col < 3: return 7
        elif 6 <= self.row and 3 <= self.col < 6: return 8
        elif 6 <= self.row and 6 <= self.col: return 9


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
        for n in self.nodes:
            n.set_neighbors()

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
