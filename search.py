# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
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
    
    from util import Stack
    open=Stack()
    close=[]
    open.push((problem.getStartState(),[]))
    successor=[]
    while(not open.isEmpty()):
        current_node=open.pop()
        state=current_node[0]
        directions=current_node[1]
        if problem.isGoalState(state):  
            return directions
        else:
            close.append(state)
            successor=problem.getSuccessors(state)
            for i in successor:
                if i[0] not in close:
                    list=i[1].split('\n')
                    open.push((i[0],directions+list))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    startNode = problem.getStartState()

    # Queue Of Paths
    queueOfPaths = util.Queue()
    # push the path into queueOfPaths
    queueOfPaths.push([(startNode, '')])
    visitedNodes = []
    resultPath = []

    while queueOfPaths.isEmpty() is False:
        # pop the first path
        path = queueOfPaths.pop()
        # peek last node in the popped path
        lastNode = path[-1][0]
        # path found if last node equals goal state
        if problem.isGoalState(lastNode):
            resultPath = path
            break

        if lastNode not in visitedNodes:
            adjacentNodes = problem.getSuccessors(lastNode);
            for adjacentNode in adjacentNodes:
                newPath = list(path)
                newPath.append((adjacentNode[0], adjacentNode[1]))
                queueOfPaths.push(newPath)
            visitedNodes.append(lastNode)

        if len(resultPath) != 0:
            break

    return constructPath(resultPath)


def constructPath(resultPath):
    path = []

    for i in range(1, len(resultPath)):
        currentNode = resultPath[i]
        direction = currentNode[1]
        path.append(direction)

    return path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    openKey = util.PriorityQueue()
    closedKey = util.Queue()
    open = {}
    visited = {}
    openList = []

    open.update({problem.getStartState(): ((problem.getStartState(), '', 0), None)})
    openKey.push(problem.getStartState(), 0)
    openList.append(problem.getStartState())
    while not openKey.isEmpty():
        currentKey = openKey.pop()
        currentNode = open[currentKey]
        parentNode = currentNode[1]
        openList.remove(currentKey)
        if problem.isGoalState(currentNode[0][0]):
            visited.update({currentNode[0][0]: currentNode})
            path = [currentNode[0][1]]
            while parentNode is not None:
                if parentNode[1] is not '':
                    path.insert(0, parentNode[1])
                parentNode = visited[parentNode[0]][1]
            return path
        else:
            closedKey.push(currentNode[0][0])
            visited.update({currentNode[0][0]: currentNode})
            children = problem.getSuccessors(currentNode[0][0])
            for child in children:
                if child[0] not in closedKey.list:
                    if child[0] not in openList:
                        openKey.update(child[0], child[2] + currentNode[0][2])
                        open.update({child[0]: ((child[0], child[1], child[2] + currentNode[0][2]), currentNode[0])})
                        openList.append(child[0])
                    else:
                        if (child[2] + currentNode[0][2]) < open[child[0]][0][2]:
                            open.update({child[0]: ((child[0], child[1], child[2] + currentNode[0][2]), currentNode[0])})

    return "Goal not found"

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
