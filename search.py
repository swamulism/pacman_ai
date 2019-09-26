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
    q = util.Stack()
    curState = problem.getStartState()
    q.push((curState, []))
    visited = set(curState)
    while(not q.isEmpty()):
        (curState, path) = q.pop()
        if problem.isGoalState(curState):
            return path
        if curState not in visited:
            visited.add(curState)
        for successor in problem.getSuccessors(curState):
            if successor[0] not in visited:
                q.push((successor[0], path + [successor[1]]))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    q = util.Queue()
    curState = problem.getStartState()
    q.push((curState, []))
    visited = set(curState)
    while(not q.isEmpty()):
        (curState, path) = q.pop()
        if problem.isGoalState(curState):
            return path
        for successor in problem.getSuccessors(curState):
            if successor[0] not in visited:
                visited.add(successor[0])
                q.push((successor[0], path + [successor[1]]))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    q = util.PriorityQueue()
    curState = problem.getStartState()
    q.push((curState, [], 0), 0)
    visited = set(curState)
    while(not q.isEmpty()):
        (curState, path, cost) = q.pop()
        if problem.isGoalState(curState):
            return path
        for successor in problem.getSuccessors(curState):
            if successor[0] not in visited:
                visited.add(successor[0])
                q.push((successor[0], path + [successor[1]], cost + successor[2]), cost + successor[2])
                print(cost+successor[2])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # q = util.PriorityQueue()
    # curState = (problem.getStartState(), None)
    # # cost = heuristic(curState[0], problem)
    # q.push((curState, []), 0)
    # visited = [curState[0]]
    # while(not q.isEmpty()):
    #     (curState, path) = q.pop()
    #     cost = heuristic(curState[0], problem)
    #     if problem.isGoalState(curState[0]):
    #         return path
    #     successors = problem.getSuccessors(curState[0])        
    #     for successor in successors:
    #         if successor[0] not in visited:
    #             visited.append(successor[0])
    #             q.push((successor, path + [successor[1]]), len(path) + 1 + cost)
    util.raiseNotDefined()

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***""create a priotity queue and push a node and heuristic"
    # fringe = util.PriorityQueue()
    # fringe.push((problem.getStartState(), []), heuristic(problem.getStartState(), problem))
    # visited = []
    # "pop node wile fringe is not empty"
    # while not fringe.isEmpty():
    #     currentLocation, actions = fringe.pop()
    #     "only process the node never visited yet"
    #     if currentLocation in visited:
    #         continuevisited.append(currentLocation)
    #         "return actions of path if reach goal state"
    #         if problem.isGoalState(currentLocation):
    #             return actions
    #             "get the new location and collect the information then enqueue the node if not visited"
    #             for newLocation, nextAction, cost in problem.getSuccessors(currentLocation):
    #                 if not newLocation in visited:newActions = actions + [nextAction]score = problem.getCostOfActions(newActions) + heuristic(newLocation, problem)fringe.push((newLocation, newActions), score)util.raiseNotDefined()# Abbreviationsbfs = breadthFirstSearchdfs = depthFirstSearchastar = aStarSearchucs = uniformCostSearch




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
