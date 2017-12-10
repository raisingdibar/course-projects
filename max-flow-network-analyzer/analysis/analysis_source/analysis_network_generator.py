from random import *
import copy
import math

class edge_network_generator:
    def __init__(self, numV):
        self.vertices = {} # Will hold a dictionary of all vertices and the vertices they are connected to
        self.edges = [] # Each edge will be represented by tuples
                        # The first two numbers are the vertexes that are connected by an edge
                        # The third number is the current flow through that edge, and the fourth is the capacity for that edge

        self.numVert = numV
        self.numEdge = numV -1
        self.source = 1
        self.sink = self.numVert
        self.maxEdge = self.calcMaxEdges(self.numVert)
        self.maxConx = self.numVert - 1
        numAdded = 0

        # At this step, the vertices will have no values
        for i in range(1, self.sink + 1):
            self.vertices[i] = []

        for vertex in self.vertices:
            if vertex == self.sink:
                continue
            connect = vertex + 1
            self.vertices[vertex].append(connect)
            self.vertices[connect].append(vertex)
            edge = (vertex, connect, 0, randint(5, 20))
            self.edges.append(edge)
            numAdded += 1

        print("\nGraph created with edges: {}\nGraph's vertices are: {}\n\n".format(self.edges, self.vertices))

    def augmentNetwork(self):
        desEdge = math.ceil(self.numEdge * 1.1)
        toAdd = desEdge - self.numEdge
        graphFull = False

        while toAdd > 0:
            print("{} edges remaining to add. {} edges currently in graph. {} edges possible in total.\n".format(toAdd, self.numEdge, self.maxEdge))
            if self.numEdge == self.maxEdge:
                graphFull = True
                break
            elif len(self.vertices[self.source]) < self.maxConx:
                connect = 3
                while connect in self.vertices[self.source]:
                    connect += 1
                self.vertices[self.source].append(connect)
                self.vertices[connect].append(self.source)
                edge = (self.source, connect, 0, randint(5, 20))
                self.edges.append(edge)
                print("Added edge {}.\n".format(edge))
            elif len(self.vertices[self.sink]) < self.maxConx:
                connect = 2
                while connect in self.vertices[self.sink]:
                    connect += 1
                self.vertices[self.sink].append(connect)
                self.vertices[connect].append(self.sink)
                edge = (connect, self.sink, 0, randint(5, 20))
                self.edges.append(edge)
                print("Added edge {}.\n".format(edge))
            else:
                start = randint(2, self.sink - 1)
                while len(self.vertices[start]) == self.maxConx:
                    start = randint(2, self.sink - 1)
                end = randint(2, self.sink - 1)
                while end in self.vertices[start] or end == start:
                    end = randint(2, self.sink - 1)
                self.vertices[start].append(end)
                self.vertices[end].append(start)
                edge = (start, end, 0, randint(5, 20))
                self.edges.append(edge)
                print("Added edge {}.\n".format(edge))
            toAdd -= 1
            self.numEdge += 1

        if graphFull:
            print("Graph is full, with {} edges. Cannot add any more edges.\n".format(self.maxEdge))
            return True
        else:
            print("\nGraph now contains edges: {}\nGraph vertices are: {}\n".format(self.edges, self.vertices))
            return False

    def calcMaxEdges(self, numV):
        if numV == 1:
            return 0
        else:
            return (numV-1) + self.calcMaxEdges(numV-1)

class vertex_network_generator:
    def __init__(self, numV):
        self.vertices = {} # Will hold a dictionary of all vertices and the vertices they are connected to
        self.edges = [] # Each edge will be represented by tuples
                        # The first two numbers are the vertexes that are connected by an edge
                        # The third number is the current flow through that edge, and the fourth is the capacity for that edge

        self.numVert = numV
        self.source = 1
        self.sink = self.numVert

        # At this step, the vertices will have no values
        for i in range(1, self.sink + 1):
            self.vertices[i] = []

        for vertex in self.vertices:
            if vertex == self.sink:
                continue
            connect = vertex + 1
            self.vertices[vertex].append(connect)
            self.vertices[connect].append(vertex)
            edge = (vertex, connect, 0, randint(5, 20))
            self.edges.append(edge)

        print("\nGraph created with edges: {}\nGraph's vertices are: {}\n\n".format(self.edges, self.vertices))

    def augmentNetwork(self):
        desVert = math.ceil(self.numVert * 1.1)
        toAdd = desVert - self.numVert

        while toAdd > 0:
            vertex = self.numVert + 1
            self.vertices[vertex] = []

            entering = randint(1, len(self.vertices))
            while entering == self.sink or entering == vertex:
                entering = randint(1, len(self.vertices))
            self.vertices[vertex].append(entering)
            self.vertices[entering].append(vertex)
            edge = (entering, vertex, 0, randint(5, 20))
            self.edges.append(edge)
            print("Added incoming edge {}.\n".format(edge))

            leaving = randint(2, len(self.vertices))
            while leaving == vertex or leaving in self.vertices[vertex]:
                leaving = randint(2, len(self.vertices))
            self.vertices[vertex].append(leaving)
            self.vertices[leaving].append(vertex)
            edge = (vertex, leaving, 0, randint(5, 20))
            self.edges.append(edge)
            print("Added outgoing edge {}.\n".format(edge))

            toAdd -= 1
            self.numVert += 1

        print("Graph now contains edges: {}\n\nGraph vertices are: {}\n".format(self.edges, self.vertices))
