"""
Python script that reads in a graph with specified starting and goal states.

The objective is to design search algorithms that find a path from the start
to goal state. Algorithms include:

Author: [YOUR NAME GOES HERE]

(1) Depth-frist search
(2) Breadth-first search
(3) uniform cost search
(4) Best Fit Search
(5) A* search

"""

import sys
import heapq


'''
A class representing a search problem
'''

class SearchProblem:

    def __init__(self):
        self.startState = None
        self.goalState = None
        self.numberOfRows = 0
        self.numberOfColumns = 0
        self.mazeAsDictionary = { }

    '''
    Reads in the maze and returns a dictionary that maps
    the maze as a dictionary.
    '''

    def initializeMaze(self, fileName):

        self.fileName = fileName

        with open(fileName) as maze:
            row = 0
            for line in maze:
                for col in range(0,len(line)-1):
                    # set up the dictionary
                    self.mazeAsDictionary[(row,col)] = line[col]

                    # determine the start and goal states
                    if line[col] == 'S':
                        self.startState = (row,col)
                    if line[col] == 'G':
                        self.goalState = (row,col)

                row += 1

        # set the number of rows and columns in the maze
        self.numberOfRows = row - 1
        self.numberOfColumns = col


    '''
    returns a list of successors we can reach
    from the current state
    '''
    def isSafe(self, row, col):
        return row >=0 and row<=self.numberOfRows and col>=0 and col<=self.numberOfColumns

    def getSuccessors(self):

        mazeWithSuccessors = { }
        direction = ['WEST', 'EAST', 'North', 'SOUTH']
        rowmove = [0,0,-1,1]
        colmove = [-1,1,0,0]
        for (currentRow, currentCol) in self.mazeAsDictionary.keys():
            # where can we go?
            successors = []
            nextState = ()
            for i in range(4):
                newRow, newCol = currentRow+rowmove[i], currentCol+colmove[i]
                if self.isSafe(newRow, newCol) and self.mazeAsDictionary[(newRow, newCol)] != '%':
                        nextState = (newRow, newCol)
                        cost = getCost(newRow, newCol)
                        successors.append( (cost, nextState, direction[i]) )
            '''
            we only need to populate if there are successors
            from (newRow, newCol)
            '''
            if successors:
                mazeWithSuccessors[(currentRow, currentCol)] = successors

        return mazeWithSuccessors

    '''
    Returns the start state
    '''
    def getStartState(self):
        return self.startState

    '''
    Returns the goal state
    '''
    def getGoalState(self):
        return self.goalState

    """
    UGLY ..... but it works.

    This function is passed a list of states and outputs
    the path taken from the starting state to goal state

    states is a list containing (row,column) tuples.
    """
    def reportGraph(self, states):
        rows = [ ]

        with open(self.fileName) as maze:
            for line in maze:
                row = []
                for c in line[:-1]:
                    row.append(c)
                rows.append(row)

        # highlight each state that is along the path
        for (row,col) in states:
            rows[row][col] = '.'

        # ensure start and goal states are identified
        (startRow, startColumn) = self.startState
        rows[startRow][startColumn] = 'S'
        (goalRow, goalColumn) = self.goalState
        rows[goalRow][goalColumn] = 'G'

        # output the maze with the path
        for row in rows:
            print "".join(row)

"""
This represents a node in the search tree
"""
class Node:
    """
    pathCost - the cost of reaching this node from the starting node
    state - the state (row,col)
    direction - the direction we came from
    parent - the parent of this node
    """
    def __init__(self, pathCost, state, direction = None, parent = None):
        self.state = state
        self.direction = direction
        self.parent = parent

        if parent:
            self.pathCost = parent.pathCost + pathCost
        else:
            self.pathCost = pathCost


'''
determine the cost of reaching this (row,col) state
'''
def getCost(row,col):
    pass

"""
the heuristic for a-star search algorithm.

(point1, point2) are tuples of type (row,col)

this can be any admisssable heuristic such
as the Manhattan distance between the pair of points
"""
def heuristic(point1, point2):
    # use the following Manhattan distance heuristic for a-star
    pass

def search(problem, maze, algorithm):
    if algorithm == 'dfs': print 'DFS'
    elif algorithm == 'bfs': print 'BFS'
    elif algorithm == 'ucs': print 'UCS'
    elif algorithm == 'bestfit': print 'BestFit'
    elif algorithm == 'astar': print 'A*'
    else: return 'Error: Unimplemented Algorithm'

    problem.initializeMaze(maze)
    startState = problem.getStartState()
    goalState = problem.getGoalState()
    mazeWithSuccessors = problem.getSuccessors()

    states = []
    container = []

    while container:
        pass

    return states

if __name__ == "__main__":

    filenames = ['astarMaze.txt']
    algorithms = ['bfs', 'dfs', 'ucs', 'bestfit', 'astar']

    ## use these lines to test one algorithm
    #problem = SearchProblem()
    #problem.reportGraph( search(problem, 'astarMaze.txt', 'bestfit') )

    ## use these lines to run all of them
    for maze in filenames:
        print maze
        for algorithm in algorithms:
            problem = SearchProblem()
            # Table only
            search(problem, maze, algorithm)
            # Draw graph
            #problem.reportGraph( search(problem, maze, algorithm) )
        print
