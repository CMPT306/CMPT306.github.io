class board:
    
    def __init__(self, row_of_hole, col_of_hole):
        self.size = 5
        self.posHole = [row_of_hole, col_of_hole]
        # 1 is peg. 0 is hole.
        # For example, this is one board: [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1, 1]]
        self.board = [[1 for j in range(i+1)] for i in range(self.size)]
        self.board[self.posHole[0]][self.posHole[1]] = 0
            
    def drawBoard(self):
        for i in range(self.size):
            for j in range(self.size-i-1):
                print '',
            for j in self.board[i]:
                if j == 1:
                    print '*',
                else:
                    print 'o',
            print 
        
    def success(self):
        for i in self.board:
            for j in i:
                if j:
                    return False
        return True
        
    def solve(self):
        if self.success():
            return
        # your code goes here

                
                
    
    
    
b = board(4,2)
b.drawBoard()
                
        
    