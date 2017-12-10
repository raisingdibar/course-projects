from random import *
import copy

class test_network_generator:
    def __init__(self):
        self.vertices = {} # Will hold a dictionary of all vertices and the vertices they are connected to
        self.edges = [] # Each edge will be represented by tuples
                        # The first two numbers are the vertexes that are connected by an edge
                        # The third number is the current flow through that edge, and the fourth is the capacity for that edge

        # Randomly pick an upper bound on the number of vertices in the graph.
        randomVertices = randint(7,15)

        # This creates a dictionary of keys representing a random amount of vertices between 7 and 15
        # At this step, the vertices will have no values
        for i in range(2,randomVertices):
            self.vertices[i] = []

        for vertex in self.vertices:
            if randomVertices < 9:
                randomEdges = randint(1, 2)
            else:
                randomEdges = randint(2, 3)
            for x in range(randomEdges):
                randomConnect = randint(2, randomVertices-1)
                if (randomConnect in self.vertices[vertex] or randomConnect == vertex):
                    continue
                self.vertices[vertex].append(randomConnect)
                self.vertices[randomConnect].append(vertex)
                edge = (vertex, randomConnect, 0, randint(5, 20))
                self.edges.append(edge)

        final = [1, randomVertices]
        for vertex in final:
            self.vertices[vertex] = []
            randomEdges = randint(2,3)
            for x in range(randomEdges):
                randomConnect = randint(2, randomVertices-1)
                while (randomConnect in self.vertices[vertex]):
                    randomConnect = randint(2, randomVertices-1)
                self.vertices[vertex].append(randomConnect)
                self.vertices[randomConnect].append(vertex)
                if (vertex == 1):
                    edge = (vertex, randomConnect, 0, randint(5, 20))
                else:
                    edge = (randomConnect, vertex, 0, randint(5, 20))
                self.edges.append(edge)
