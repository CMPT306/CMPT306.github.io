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
        self.m, self.n = start.shape # 3, 3
        
    def print_one_square(self, square):
        for i in square:        
            for j in i:
                if j:
                    print j,
                else:
                    print ' ',
            print
    
    def print_solution(self, state):
        path=[]
        directions=[]
        while state[2] is not None:
            path.append(state[0])
            directions.append(state[-1])
            for v in self.visited:
                if np.allclose(v[0], state[2]):
                    state = v
                    break
        print "start"
        self.print_one_square(self.start)
        print
        for i in range(len(path)-1,-1,-1):
            print directions[i]
            self.print_one_square(path[i])
            print

    def index(self, square, x):
        #return map(lambda x: x[0], np.where(square == x))
        tmp = np.where(square == x)
        return tmp[0][0], tmp[1][0]

    # heuristics function
    def heuristics(self, square):
        dist = 0
        if self.method == "Manhattan":
            for i in range(np.size(self.goal,0)):
                for j in range(np.size(self.goal,1)):
                    if square[i,j] != 0:
                        p, q = self.index(self.goal, square[i,j])
                        dist = dist + np.abs(i-p) + np.abs(j-q)
        elif self.method == "Hamming":
            for i in range(np.size(self.goal,0)):
                for j in range(np.size(self.goal,1)):
                    if square[i,j] and square[i,j] != self.goal[i,j]:
                        dist += 1
        return dist

    def priority(self, state):
        return state[1] + self.heuristics(state[0])

    def hasvistied(self, square):
        for v in self.visited:
            if np.allclose(v[0],square):
                return True
        return False

    def isMove(self, x, y):
        return x>=0 and x<self.m and y>=0 and y<self.n
    
    def solve(self):
        # state: current square, moves, previous square, direction
        square = self.start.copy()
        state = (square, 0, None, None)
        self.visited.append(state)
        push(self.queue, [self.priority(state), self.count, state])
        direction=["up", "down", "left", "right"]
        row = [-1,1,0,0]
        col = [0,0,-1,1]
        while True:
            tmp1, tmp2, state = pop(self.queue)
            square, move, parent = state[:-1]
            p, q = self.index(square, 0)
            
            if np.allclose(square, self.goal):
                self.print_solution(state)
                break
                
            for i in range(4):
                nextsquare = square.copy()
                nextp, nextq = p+row[i], q+col[i]
                if self.isMove(nextp, nextq):
                    nextsquare[p,q], nextsquare[nextp, nextq] = nextsquare[nextp,nextq], 0
                    if not self.hasvistied(nextsquare):
                        self.count += 1
                        currentstate=(nextsquare, move+1, square.copy(), direction[i])
                        push(self.queue, [self.priority(currentstate),self.count, currentstate])

            self.visited.append(state)       
            
    
if __name__ == "__main__":
    
    goal = np.array([[1,2,3],[4,5,6],[7,8,0]])
    start_test1 = np.array([[1,2,0],[3,4,6],[7,5,8]])
    start_test2 = np.array([[1,2,3],[0,4,6],[7,5,8]])
    method1 = "Hamming"
    method2 = "Manhattan"
    
    start_test3 = np.array([[8,0,6],[5,4,7],[2,3,1]])
    start_test4 = np.array([[1,0,3],[5,4,7],[6,8,2]])
    
    game = MoveSquare(start_test1, goal, method2)
    game.solve()
    
    