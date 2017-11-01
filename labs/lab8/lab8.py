import numpy as np
from heapq import heappush as push
from heapq import heappop as pop

class MoveSquare(object):
    
    def __init__(self, start, goal, method):
        self.start = start
        self.goal = goal
        self.queue = [] # priority queue
        self.count = 1
        self.visited = []
        self.method = method
        
    def print_one_square(self, square):
        for i in square:        
            for j in i:
                if j:
                    print j,
                else:
                    print ' ',
            print
    
    def print_solution(self, state):
        tmp=[]
        tmpd=[]
        while state[2] is not None:
            tmp.append(state[0])
            tmpd.append(state[-1])
            for vv in self.visited:
                if np.allclose(vv[0], state[2]):
                    state = vv
                    break
        print "start"
        self.print_one_square(start)
        print
        for i in range(len(tmp)-1,-1,-1):
            print tmpd[i]
            self.print_one_square(tmp[i])
            print

    def index(self, square, x):
        return map(lambda x: x[0], np.where(square == x))

    # heuristics function
    def heuristics(self, square):
        dist = 0
        if self.method == "Hamming":
            pass
        elif self.method == "Manhattan":
            pass
        return dist

    def priority(self, state):
        # f = g + h
        # g: how many steps are needed to reach from start to current state
        # h: how many steps are needed to reach from current state to the goal
        pass

    def hasvistied(self, square):
        pass

    def solve(self):
        m,n = self.start.shape # m and n are all 3 here.
        
        # state: a 3*3 square, how many steps to reach this quare from start,
        #        parent square, direction from parent to child
        square = self.start.copy()
        state = (square, 0, None, None)
        self.visited.append(state)  # append whole state, not current square
        # push: (queue, [priority of current state, count, current state])
        push(self.queue, [self.priority(state), self.count, state])
        
        while True:
            # do some initialitions here:
            
            
            
            # print solution
            if np.allclose(square, self.goal):
                self.print_solution(state)
                break
                
            # your core part of code goes here:

            
                   
    
if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    start_test1 = np.array([[1,2,0],[3,4,6],[7,5,8]])
    start_test2 = np.array([[1,2,3],[0,4,6],[7,5,8]])
    method1 = "Hamming"
    method2 = "Manhattan"
    
    game = MoveSquare(start_test1, goal, method1)
    game.solve()
    
    