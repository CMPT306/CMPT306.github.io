'''
Constructs the shortest path from a designated
starting vertex to all other vertices in the graph
using Dijkstra's Algorithm.

This algorithm will work with either a directed or
undirected graph.

@date - Nov 2017.

@author: Jingsai Liang
'''

import sys
import heapq

def main(inputFile, startingVertex, method):
    '''
    input file containing directed-graph with positive weights

    file contents is
    [begin vertex] [end vertex] [cost]
    '''
    graph = open(inputFile)

    '''
    an initially empty dictionary containing mapping
    [vertex]:[adjacency list]
    '''
    adjacency = { }

    # priority queue
    heap = [ ]

    # collection of vertices
    vertices = [ ]

    '''
    shortest path graph
    Each dictionary entry contains mapping of [vertex]:(cost,previous vertex)
    '''
    path = { }

    '''
    The following reads in the input file
    and constructs an adjacency list of
    the graph.
    '''
    for line in graph:
        entry = line.split()

        # get the vertices
        vertices.append(entry[0])
        vertices.append(entry[1])

        if entry[0] not in adjacency:
            adjacency[entry[0]] = []

        # construct an edge for the adjacency list
        edge = (entry[1], int(entry[2]))
        adjacency[entry[0]].append(edge)

    # construct the set of unknown vertices
    unVisited = set(vertices)

    if startingVertex not in unVisited:
        print 'Starting vertex', startingVertex, 'not present in graph', graph
        quit()

    # update the heap with new lower distance
    if method == 1:
        # initialize
        heapq.heappush(heap, [0, startingVertex])
        path[startingVertex] = [0, None]
        for vertex in unVisited:
            if vertex != startingVertex:
                heapq.heappush(heap, [float("inf"), vertex])
                path[vertex] = [float("inf"), None]

        while heap:
            dtoparent, parent = heapq.heappop(heap)
            unVisited.remove(parent)
            if parent in adjacency:
                for child, weight in adjacency[parent]:
                    if child in unVisited:
                        d = path[child][0]
                        if weight+dtoparent < d:
                            d = weight+dtoparent
                            path[child] = [d, parent]
                            heapupdate(heap, [d, child])
    # add an element with new distance into heap. donot remove or update any element.
    # pop the element with smallest distance. ignore all elements of the same node. 
    elif method == 2:
        for vertex in unVisited:
            heapq.heappush(heap, [float("inf"), vertex, None])
        heapq.heappush(heap, [0, startingVertex, None])

        while heap:
            dtovertex, vertex, parent = heapq.heappop(heap)
            if vertex in unVisited:
                unVisited.remove(vertex)
                path[vertex] = [dtovertex, parent]
                if vertex in adjacency:
                    for child, weight in adjacency[vertex]:
                        d = weight+dtovertex
                        heapq.heappush(heap, [d, child, vertex])
    print path

def heapupdate(heap, node):
    d, vertex = node
    for i in range(len(heap)):
        if heap[i][1] == vertex:
            heap[i][0] = d
            break
    heapq.heapify(heap)

def heapdelete(heap, vertex):
    for x,y in heap:
        if y == vertex:
            break
    heap.remove((x,y))
    heapq.heapify(heap)
    return x

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print 'Usage python readit.py [input file] [starting vertex]'
        quit()

    method = 2
    main(sys.argv[1], sys.argv[2], method)
