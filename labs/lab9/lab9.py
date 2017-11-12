from copy import deepcopy as copy
import numpy as np

class linkedlist():
    def __init__(self, board):
        self.val = copy(board)
        self.child = None # jump to this child from current board
        self.jumpfrom = None
        self.jumpto = None
        
class board:
    def __init__(self, row_of_hole, col_of_hole):
        self.size = 5
        self.HolePos = [row_of_hole, col_of_hole]
        # 1 is peg. 0 is hole.
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[row_of_hole][col_of_hole] = 0
        self.start = linkedlist(self.board)
        self.current = self.start
            
    def drawBoard(self, board):
        for i in range(self.size):
            for j in range(self.size-i-1):
                print '',
            for j in board[i]:
                if j == 1:
                    print '+',
                else:
                    print 'o',
            print 
        
    def success(self):
        tmp = sum([sum(i) for i in self.board])
        if tmp==1:
            return True
        return False
    
    def printSolution(self):
        if self.success():
            self.current = self.start
            while self.current.child:
                self.drawBoard(self.current.val)
                print self.current.jumpfrom, "to ", self.current.jumpto
                self.current = self.current.child
            self.drawBoard(self.current.val)
        else:
            print "No solution has been found yet!" 
        
    def solve(self):
        if self.success():
            return True
        
        # loop over all positions to find next available position to jump one peg
        # check six directions for each position: left, right, top-left, top-right, bottom-left, bottom-right        
        
            # if one peg can be jumped from this position:
                # update self.board and .child, .jumpfrom, .jumpto of current parent node

                # recursively call self.solve()
                    # return true if it finds one solution

                # withdraw the previous updating if it does not find one solution

                # return false if no available position on current board
        

startHoleRow, startHoleCol = np.inf, np.inf
while startHoleRow > 4:
    startHoleRow = int(raw_input("Please input row of the hole (<=4):"))
while startHoleCol > startHoleRow:
    startHoleCol = int(raw_input("Please input column of the hole (<=row):"))
    
game=board(startHoleRow, startHoleCol)
game.solve()
game.printSolution()
        
    