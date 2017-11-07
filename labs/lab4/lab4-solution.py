
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def init(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
    
        print 'DFS Traversal'

        # creates a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()
        
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        
        self.path = ""
        self.immediateParent = {}

    '''
    depth-first traversal of specified graph

    This is likely the function representing the recursive portion
    of the DFS algorithm
    '''
    def DFS(self, method):
        if method is 'recursive':
            for vertex in self.vertices:
                if vertex in self.unVisitedVertices:
                    self.DFS_recur(vertex)
                    self.path += ', '
            print "DFS using recursive: ", self.path
        elif method is 'stack':
            for vertex in self.vertices:
                if vertex in self.unVisitedVertices:
                    self.DFS_stack(vertex)
                    self.path += ', '
            print "DFS using stack: ", self.path
            
    def DFS_recur(self,vertex):
        self.path += vertex
        self.unVisitedVertices.remove(vertex)
        children = self.adjacencyList[vertex]
        children.sort()
        for child in children:
            if child in self.unVisitedVertices:
                self.immediateParent[child] = vertex
                self.DFS_recur(child)
            elif vertex in self.immediateParent and child is not self.immediateParent[vertex]:
                self.path += '(' + child + ')'
                
    def DFS_stack(self,vertex):
        stack=[]
        stack.append(vertex)            
        while stack:
            vertex = stack.pop()
            if vertex in self.unVisitedVertices:
                self.path += vertex
                self.unVisitedVertices.remove(vertex)
                children = self.adjacencyList[vertex]
                children.sort(reverse=True)
                backedge = []
                for child in children:
                    if child in self.unVisitedVertices:
                        self.immediateParent[child] = vertex
                        stack.append(child)
                    elif vertex in self.immediateParent and child is not self.immediateParent[vertex]:
                        backedge.append(child)
                for child in backedge[::-1]:
                    self.path += '(' + child + ')'
                
    def BFSInit(self):
    
        print 'BFS Traversal'

        # creates a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()
        
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        
        self.path = ""
        self.immediateParent = {}   
        
    def BFS(self):
        queue = []
        for start in self.vertices:
            if start in self.unVisitedVertices:
                self.unVisitedVertices.remove(start)
                queue.append(start)
                self.path += start
            
                while queue:
                    vertex = queue.pop()
                    children = self.adjacencyList[vertex]
                    children.sort()
                    for child in children:
                        if child in self.unVisitedVertices:
                            self.unVisitedVertices.remove(child)
                            self.immediateParent[child] = vertex
                            queue.insert(0,child)
                            self.path += child
                        elif vertex in self.immediateParent and child is not self.immediateParent[vertex]:
                            self.path += '(' + child + ')'
                            
                self.path += ', '
                
        print "BFS using queue: ", self.path
         
if __name__ == '__main__':
        
    ga = GraphAlgorithms()
    
    filename = raw_input('Please input filename:')
    #filename='graph-3.txt'
    ga.init(filename)
    
    # Construct a depth-first search

    ga.DFSInit()   
    ga.DFS('recursive')
    ga.DFSInit() 
    ga.DFS('stack')
    ga.BFSInit()
    ga.BFS()
