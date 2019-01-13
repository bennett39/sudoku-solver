from models import Node, Grid

def main():
    g = Grid()
    get_grid_from_file(g, "puzzles/p1.txt")

    g.print_grid()
    print()
    g.print_grid('possible')


def get_grid_from_file(g, source):
    with open(source, mode='r') as f:
        id = 0
        for line in f.readlines():
            clean_line = line.strip()
            for char in clean_line:
                if is_int(char):
                    set_grid_val(g, g.nodes[id], int(char))
                id += 1


def is_int(a):
    try:
        int(a)
        return True
    except ValueError:
        return False


def set_grid_val(grid, node, val):
    node.set_val(val)
    node.empty_possibles()
    rm_horizontal(grid, node)
    rm_vertical(grid, node)
    rm_box(grid, node)


def rm_horizontal(grid, node):
    for i in range(81):
        if grid.nodes[i].row == node.row:
            grid.nodes[i].rm_possible(node.val)


def rm_vertical(grid, node):
    for i in range(81):
        if grid.nodes[i].col == node.col:
            grid.nodes[i].rm_possible(node.val)


def rm_box(grid, node):
    for i in range(81):
        if grid.nodes[i].box == node.box:
            grid.nodes[i].rm_possible(node.val)


if __name__ == "__main__":
    main()
