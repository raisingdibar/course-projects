from random import *
import copy
import math

class max_flow_generator:
    def __init__(self, network):
        self.network = network # Holds the network
        self.sink = self.findSink()
        self.source = self.findSource()
        self.max_flow = self.solveMaxFlow(self.source, self.sink, self.network.edges, math.inf)
        self.removeEmpty()

    def solveMaxFlow(self, vertex, end, edgelist, bottleneck, path=[], visited=[]):
        #If we reach the sink from the source edit flows
        visited.append(vertex)
        if vertex == end:
            self.updatePath(path, bottleneck)
            return bottleneck
        #Traverse the graph
        addedFlow = 0
        for edge in edgelist:
            #Check for edges going out
            if bottleneck == 0:
                break
            remCap = self.getEdgeRemaining(edge)
            if edge[0] == vertex and edge[1] not in visited and remCap != 0:
                ind = edgelist.index(edge)
                path.append(ind)
                oldBottleneck = None
                if remCap < bottleneck:
                    oldBottleneck = bottleneck
                    bottleneck = remCap
                val = self.solveMaxFlow(edge[1], end, edgelist, bottleneck, path)
                if val == 0 and oldBottleneck != None: bottleneck = oldBottleneck
                addedFlow += val
                bottleneck -= val
                path.remove(ind)
                visited.pop()
        return addedFlow

    def getEdgeRemaining(self, edge):
        cap = edge[3]
        flow = edge[2]
        diff = cap - flow
        return diff

    def removeEmpty(self):
        toRemove = []
        for edge in self.network.edges:
            if (edge[2] == 0):
                toRemove.append(edge)
        for edge in toRemove:
            self.network.edges.remove(edge)

    def updatePath(self, path, bottleneck):
        for ind in path:
            self.updateEdge(ind, bottleneck)

    def updateEdge(self, ind, amt):
        edge = self.network.edges[ind]
        print("adding {} to edge {}".format(amt, edge))
        self.network.edges[ind] = (edge[0], edge[1], edge[2] + amt, edge[3])

    def findSource(self):
        return 1

    def findSink(self):
        return len(self.network.vertices)
