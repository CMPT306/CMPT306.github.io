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

def main(inputFile, startingVertex):
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

    # initialize path and heap

    while heap:
        pass

    print path

# update distance of one node in the heap
def heapupdate(heap, node):
    d, vertex = node
    for i in range(len(heap)):
        if heap[i][1] == vertex:
            heap[i][0] = d
            break
    heapq.heapify(heap)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print 'Usage python lab11.py [input file] [starting vertex]'
        quit()

    main(sys.argv[1], sys.argv[2])
