from models import Node, Grid

def main():
    """
    A program to find the solution to a sudoku.
    """
    g = Grid()
    get_grid_from_file(g, "puzzles/p1.txt")

    print("Input:")
    g.print_grid()

    discover_vals(g)
    print("---\nSolution:")
    g.print_grid()


def discover_vals(g):
    """
    Takes a paritally-filled Grid object and discovers new values until
    there are none remaining.
    """
    more_vals = True
    while more_vals:
        more_vals = False
        for node in g.nodes:
            if len(node.possibles) == 1:
                val = node.possibles[0]
                set_grid_val(g, node, val)
                more_vals = True


def get_grid_from_file(g, source):
    """
    Opens a .txt file that stores a sudoku.
    If character in file is '.' then that location in the grid is empty.
    """
    with open(source, mode='r') as f:
        id = 0
        for line in f.readlines():
            clean_line = line.strip()
            for char in clean_line:
                if is_int(char):
                    set_grid_val(g, g.nodes[id], int(char))
                id += 1


def is_int(a):
    """
    Helper function to determine if char is an int.
    """
    try:
        int(a)
        return True
    except ValueError:
        return False


def set_grid_val(grid, node, val):
    """
    Put a value into a grid and remove that value from the possibilities
    of the relevant row, column, and box.
    """
    node.set_val(val)
    node.empty_possibles()
    rm_horizontal(grid, node)
    rm_vertical(grid, node)
    rm_box(grid, node)


def rm_horizontal(grid, node):
    """
    Removes a new node's val from the possible values in the nodes in
    that row.
    """
    for i in range(81):
        if grid.nodes[i].row == node.row:
            grid.nodes[i].rm_possible(node.val)


def rm_vertical(grid, node):
    """
    Removes a new node's val from the possible values in the nodes in
    that column.
    """
    for i in range(81):
        if grid.nodes[i].col == node.col:
            grid.nodes[i].rm_possible(node.val)


def rm_box(grid, node):
    """
    Removes a new node's val from the possible values in the nodes in
    that box.
    """
    for i in range(81):
        if grid.nodes[i].box == node.box:
            grid.nodes[i].rm_possible(node.val)


if __name__ == "__main__":
    main()
