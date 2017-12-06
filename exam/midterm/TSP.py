import numpy as np

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
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
            (firstVertex, secondVertex, cost) = line.split()
        
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
                self.adjacencyList[firstVertex] = { }

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex][secondVertex] = int(cost)
            
        self.vertices = list(set(self.vertices))
        
        graphFile.close()
            
    ## Minimal Change
    def permutate(self, name):

        '''
        Simple example - this returns what the permutations()
        function in the itertools package. Your implementation
        of this function should return the same unordered list 
        tuples. (i.e. the tuples can be in any order.)
        '''
        value = len(name)

        if value == 1:
            return [(name[-1],)]

        tmp = self.permutate(name[:-1])
        result = []
        flag = True
        for item in tmp:
            for i in range(value): 
                if flag: # right to left
                    result.append(item[:value-i-1] + (name[-1],) + item[value-i-1:])
                else: # left to right
                    result.append(item[:i] + (name[-1],) + item[i:])
            flag = not flag

        return result
    
    def findroute(self, startcity_index):
        allroutewo = self.permutate(self.vertices[:startcity_index] + self.vertices[startcity_index+1:])
        allroute = []
        startcity = self.vertices[startcity_index]
        for route in allroutewo:
            allroute.append((startcity,) + route + (startcity,))
        return allroute
    
    def solve(self):
        cost = np.inf
        path = []
        for i in range(len(self.vertices)):
            allroute = self.findroute(i)
            for route in allroute:
                tmpcost = 0
                for j in range(len(route)-1):
                    tmpcost += self.adjacencyList[route[j]][route[j+1]]
                if tmpcost < cost:
                    cost = tmpcost
                    path = route[:]
        return cost, path
                
        
if __name__ == '__main__':
    
    g = GraphAlgorithms('vt.txt')
    print g.solve()
    