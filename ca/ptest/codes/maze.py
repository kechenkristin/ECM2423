import string
import util
import time


class Maze:
    def __init__(self, sourceFile, costFn=lambda x: 1):
        """

        A maze is made of a two-dimensional array

        sourceFile: the file required to generate the maze
        """
        self.costFn = costFn
        self.sourceFile = sourceFile
        self.lines = self.generateFileLines()

        self.length = len(self.lines)
        self.width = len(self.lines[0])

        # construct start and goal (tuple)
        # start node are at the top (0, 1)
        self.start = (0, self.lines[0].index('-'))
        # goal node are at the bottom (2, 3)
        self.goal = (len(self.lines) - 1, self.lines[-1].index('-'))

        # construct grid, false - wall, true - path
        # [[False, True, False, False, False], [False, True, True, False, False], [False, False, True, False, False], [False, False, True, False, False]]
        self.grid = [[c == '-' for c in line] for line in self.lines]


    def generateFileLines(self):
        """
        open the sourcefile and generate the clean lines
        ['#-###', '#--##', '##-##', '##-##']
        """
        # further thinking of the file path
        with open(self.sourceFile) as f:
            # lines = [(" ".join(line.split())).replace(" ", "") for line in f]
            lines = [line.translate({ord(c): None for c in string.whitespace}) for line in f]
        return lines

    def size(self):
        """
        returns the size of the maze
        """
        return self.width * self.length

    def vertices(self):
        """
        returns the total number of vertices in the maze
        """
        return self.width * self.length

    def getStartState(self):
        """
        returns the startState of the maze
        """
        return self.start

    def getGoalState(self):
        return self.goal

    def isGoalState(self, location):
        """
        returns true if the location(x, y) is goal state
        """
        return location == self.goal

    def inBounds(self, location):
        """
        returns true if the location(x, y) is in bounds
        """
        x, y = location
        return 0 <= x <= (self.length - 1) and 0 <= y <= (self.width - 1)
        # return not((x == -1) or (x == self.width) or (y == -1) or (y == self.length))

    def isPath(self, location):
        """
        returns true if the location(x, y) is a path, not wall
        """
        x, y = location
        return self.grid[x][y]

    def getSuccessors(self, location):
        """
        Returns successor states, the actions they require, and a cost of 1.
         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """
        x, y = location
        successors = []

        if self.inBounds((x - 1, y)):
            if self.isPath((x - 1, y)):
                nextState = (x - 1, y)
                successors.append((nextState, nextState, self.costFn(nextState)))

        if self.inBounds((x + 1, y)):
            if self.isPath((x + 1, y)):
                nextState = (x + 1, y)
                successors.append((nextState, nextState, self.costFn(nextState)))

        if self.inBounds((x, y - 1)):
            if self.isPath((x, y - 1)):
                nextState = (x, y - 1)
                successors.append((nextState, nextState, self.costFn(nextState)))

        if self.inBounds((x, y + 1)):
            if self.isPath((x, y + 1)):
                nextState = (x, y + 1)
                successors.append((nextState, nextState, self.costFn(nextState)))

        return successors


def depthFirstSearch(maze: Maze):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    frontier = util.Stack()
    reached = set()

    startState = maze.getStartState()
    frontier.push((startState, [startState]))

    while not frontier.isEmpty():
        current, path = frontier.pop()

        if maze.isGoalState(current):
            return path

        if current not in reached:
            reached.add(current)
            successors = maze.getSuccessors(current)
            for nextTuple in successors:
                frontier.push((nextTuple[0], path + [nextTuple[1]]))
    return []


def depthFirstSearch2(maze: Maze):
    """
    Updated version of dfs, 
    Can calculate some statistics about its performance.
    The number of nodes explored to find the path,
    the time of the execution,
    and the number of steps in the resulting path.
    return a list contains two items: a dictionary stores all the info above
    a path list
    """
    start_time = time.time()
    frontier = util.Stack()
    reached = set()

    startState = maze.getStartState()
    frontier.push((startState, [startState]))
    exploredNodeCount = 0
    ret = []

    while not frontier.isEmpty():
        current, path = frontier.pop()

        if maze.isGoalState(current):
            end_time = time.time()
            # print(reached)
            # print(exploredNodeCount)
            ret.append(
                {'exporedNode': exploredNodeCount, 'executionTime': end_time - start_time, 'numOfSteps': len(reached)})
            ret.append(path)
            return ret

        if current not in reached:
            reached.add(current)
            successors = maze.getSuccessors(current)
            for nextTuple in successors:
                frontier.push((nextTuple[0], path + [nextTuple[1]]))
                exploredNodeCount += 1
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(position, maze):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position
    xy2 = maze.getGoalState()
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


def aStarSearchUpdated(maze, heuristic=manhattanHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start_time = time.time()
    frontier = util.PriorityQueue()
    reached = set()

    startState = maze.getStartState()
    frontier.push((startState, [startState], 0), 0)
    exploredNodeCount = 0
    ret = []

    while not frontier.isEmpty():
        current, path, costSoFar = frontier.pop()

        if maze.isGoalState(current):
            end_time = time.time()
            ret.append(
                {'exporedNode': exploredNodeCount, 'executionTime': end_time - start_time, 'numOfSteps': len(reached)})
            ret.append(path)
            return ret

        if current not in reached:
            reached.add(current)
            for nextTuple in maze.getSuccessors(current):
                # frontier.push((nextNode, newPath, newCost), priority)
                # newCost = costSoFar + stepCost
                # F(x) = g(x) + h(x)
                # g(x) : backword cost = newCost = costSoFar + stepCost
                # priority = newCost + h(x)
                newCost = costSoFar + nextTuple[2]
                frontier.push((nextTuple[0], path + [nextTuple[1]], newCost), newCost + heuristic(nextTuple[0], maze))
                exploredNodeCount += 1

    return []


def aStarSearch(maze, heuristic=manhattanHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    reached = set()

    startState = maze.getStartState()
    frontier.push((startState, [startState], 0), 0)

    while not frontier.isEmpty():
        current, path, costSoFar = frontier.pop()

        if maze.isGoalState(current):
            return path

        if current not in reached:
            reached.add(current)
            for nextTuple in maze.getSuccessors(current):
                # frontier.push((nextNode, newPath, newCost), priority)
                # newCost = costSoFar + stepCost
                # F(x) = g(x) + h(x)
                # g(x) : backword cost = newCost = costSoFar + stepCost
                # priority = newCost + h(x)
                newCost = costSoFar + nextTuple[2]
                frontier.push((nextTuple[0], path + [nextTuple[1]], newCost), newCost + heuristic(nextTuple[0], maze))

    return []


if __name__ == '__main__':
    maze = Maze('../mazeFiles/maze-Easy.txt')
    # dfsPath = depthFirstSearch2(maze)
    # print(dfsPath)
    astarPath = aStarSearchUpdated(maze)
    print(astarPath)
