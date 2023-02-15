import util
from maze import Maze

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
    "*** YOUR CODE HERE ***"
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
            for nextTuple in maze.getSuccessors(current):
                frontier.push((nextTuple[0], path + [nextTuple[1]]))
    return []

if __name__ == '__main__':
    maze = Maze('simpleMaze.txt')
    path = depthFirstSearch(maze)
    print(path)
