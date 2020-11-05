class Baby(object):

    def __init__(self):
        super(Baby, self).__init__()
        self.dimension = tuple()
        self.cells = set()
        self.cells_positions = set()
        self.neighbours = set()
        self.name = ''

    def calculate_positions_and_neighbours_set(self):
        self.cells_positions.clear()
        self.neighbours.clear()
        for cell in self.cells:
            self.cells_positions.add(cell.position)
            self.neighbours = self.neighbours.union(cell.neighbours)