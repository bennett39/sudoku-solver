class Node():
    def __init__(self, id):
        self.id = id
        self.row = id // 9
        self.col = id % 9

        self.val = None
        self.possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.box = self.set_box()
    
    def empty_possibles(self):
        self.possibles = []

    def rm_possible(self, rval):
        try: self.possibles.remove(rval)
        except Exception: pass

    def set_val(self, val):
        self.val = val

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
        for k in range(81):
            self.nodes.append(Node(k))

    def print_grid(self, element=''):
        r = 0
        for node in self.nodes:
            if node.row != r:
                print()
                r = node.row
            if element == 'possible':
                print(node.possibles, end="\t")
            else:
                print(node.val, end="\t")
        print()
