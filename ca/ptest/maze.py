import string

# get clean line
with open('simpleMaze.txt') as f:
    # lines = [(" ".join(line.split())).replace(" ", "") for line in f]
    lines = [line.translate({ord(c): None for c in string.whitespace}) for line in f]

print(lines)

# get length and width
length = len(lines)
width = len(lines[0])
print(length, width)

# construct grid
grid = [[c == '-' for c in line] for line in lines]
print(grid)

# get start and goal
start = (0, lines[0].index('-'))
goal = (lines[-1].index('-'), len(lines) - 1)
print(start, goal)

class Maze():
    """
    A Maze
    """

    def __init__(self, mazeHelper):
        self.grid = mazeHelper.getGrid();
        self.start = mazeHelper.getStart()
        self.goal = mazeHelper.getGoal()

    def getStart(self):
        return self.start

    def isGoal(self, state):
        return state == self.goal

    def getSuccessors(self, state):
