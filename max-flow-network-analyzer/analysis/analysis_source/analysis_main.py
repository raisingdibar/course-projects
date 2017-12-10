from analysis_network_generator import *
from max_flow_generator import *
import matplotlib.pyplot as plt
import numpy as np
import copy
import os

def testFileCreation(network, graphNum, graphType):
    '''
    A class that creates an output dot file based on the test network created

    network - the test_network_generator class being converted to dot file
    graphNum - Number of graph so each is unique
    '''

    string = "digraph g{\n\nrankdir = LR\n\n"
    for tup in network.edges:
        string += '{} -> {} [label = " {} "];\n'.format(tup[0], tup[1], tup[3])

    string += '\nlabel = "graph {:02d}{}"\n'.format(graphNum, graphType)
    string += '}'
    print(string, "\n")

    fileName = "../input_graphs/graph{}{}.dot".format(graphNum, graphType)
    file = open(fileName, 'w+')
    file.write(string)

    file.close()

    filenameIn = "../input_graphs/graph{}{}.dot".format(graphNum, graphType)
    filenameOut = "../input_graphs/graph{}{}.png".format(graphNum, graphType)

    os.environ['PATH'] += ":"+"/usr/local/bin"
    print(os.system("dot -Tpng " +filenameIn+ " -o" +filenameOut))

def maxFileCreation(maxGen, graphNum, graphType):
    '''
    A class that creates an output dot file based on the max network created

    network - the max_flow_generator class being converted to dot file
    graphNum - Number of graph so each is unique
    '''
    network = maxGen.network

    string = "digraph g{\n\nrankdir = LR\n\n"
    for tup in network.edges:
        string += '{} -> {} [label = " {}/{} "];\n'.format(tup[0], tup[1], tup[2], tup[3])

    string += '\nlabel = "graph {:02d}{}: maximum flow = {}, runtime to calculate flow = {} "\n'.format(graphNum, graphType, maxGen.max_flow, maxGen.elapsedTime)
    string += '}'
    print(string, "\n")

    fileName = "../output_graphs/graph{}{}.dot".format(graphNum, graphType)
    file = open(fileName, 'w+')
    file.write(string)

    file.close()

    filenameIn = "../output_graphs/graph{}{}.dot".format(graphNum, graphType)
    filenameOut = "../output_graphs/graph{}{}.png".format(graphNum, graphType)

    os.environ['PATH'] += ":"+"/usr/local/bin"
    print(os.system("dot -Tpng " +filenameIn+ " -o" +filenameOut))

def generateAndSave(filename, numA, numB, numC, type):
    #Create a figure with a certain size
    plt.figure(figsize = (14, 6))

    iter, A, B, C = np.loadtxt(filename + '.txt', delimiter=' ', unpack=True)

    #Plot x versus y
    plt.plot(iter, A, color = "blue", label="For {} Starting {}".format(numA, type))
    plt.plot(iter, B, color = "red", label="For {} Starting {}".format(numB, type))
    plt.plot(iter, C, color = "green", label="For {} Starting {}".format(numC, type))

    plt.xlabel('Number of Iterations')
    plt.ylabel('Runtime in (s)')

    #Save the figure
    plt.savefig(filename + ".png", dpi = 300)

    #Show the figure
    plt.legend()
    #plt.show()

def main():

    for j in range(0, 5):
        numVA = 8
        numVB = 10
        numVC = 12
        string = ""

        # Testing effect of adding edges to a connected graph with a fixed number of vertices = numV.
        edgeGraphA = edge_network_generator(numVA)
        testFileCreation(edgeGraphA, 0, "edgeA")
        edgeGraphB = edge_network_generator(numVB)
        testFileCreation(edgeGraphB, 0, "edgeB")
        edgeGraphC = edge_network_generator(numVC)
        testFileCreation(edgeGraphC, 0, "edgeC")

        netCopyA = copy.deepcopy(edgeGraphA)
        netCopyB = copy.deepcopy(edgeGraphB)
        netCopyC = copy.deepcopy(edgeGraphC)

        max_flowA = max_flow_generator(edgeGraphA)
        maxFileCreation(max_flowA, 0, "maxedgeA")
        max_flowB = max_flow_generator(edgeGraphB)
        maxFileCreation(max_flowB, 0, "maxedgeB")
        max_flowC = max_flow_generator(edgeGraphC)
        maxFileCreation(max_flowC, 0, "maxedgeC")

        edgeGraphA = netCopyA
        edgeGraphB = netCopyB
        edgeGraphC = netCopyC

        for i in range(1, 15):
            isFullA = edgeGraphA.augmentNetwork()
            testFileCreation(edgeGraphA, i, "edgeA")
            isFullB = edgeGraphB.augmentNetwork()
            testFileCreation(edgeGraphB, i, "edgeB")
            isFullC = edgeGraphC.augmentNetwork()
            testFileCreation(edgeGraphC, i, "edgeC")

            netCopyA = copy.deepcopy(edgeGraphA)
            netCopyB = copy.deepcopy(edgeGraphB)
            netCopyC = copy.deepcopy(edgeGraphC)

            max_flowA = max_flow_generator(edgeGraphA)
            maxFileCreation(max_flowA, i, "maxedgeA")
            max_flowB = max_flow_generator(edgeGraphB)
            maxFileCreation(max_flowB, i, "maxedgeB")
            max_flowC = max_flow_generator(edgeGraphC)
            maxFileCreation(max_flowC, i, "maxedgeC")

            string += "{} {} {} {}\n".format(i, max_flowA.elapsedTime, max_flowB.elapsedTime, max_flowC.elapsedTime)

            if isFullA:
                print("Graph A is full.")
                break
            if isFullB:
                print("Graph B is full.")
                break
            if isFullC:
                print("Graph C is full.")
                break

            edgeGraphA = netCopyA
            edgeGraphB = netCopyB
            edgeGraphC = netCopyC

        fileName = "../data/edgegraphcomparison" + str(j)
        file = open(fileName + ".txt", 'w+')
        file.write(string)
        file.close()
        generateAndSave(fileName, numVA, numVB, numVC, "Edges")
        string = ""

        # Testing effect of adding and connecting vertices to a connected graph with starting number of vertices = numV.
        vertexGraphA = vertex_network_generator(numVA)
        testFileCreation(vertexGraphA, 0, "vertexA")
        vertexGraphB = vertex_network_generator(numVB)
        testFileCreation(vertexGraphB, 0, "vertexB")
        vertexGraphC = vertex_network_generator(numVC)
        testFileCreation(vertexGraphC, 0, "vertexC")

        netCopyA = copy.deepcopy(vertexGraphA)
        netCopyB = copy.deepcopy(vertexGraphB)
        netCopyC = copy.deepcopy(vertexGraphC)

        max_flowA = max_flow_generator(vertexGraphA)
        maxFileCreation(max_flowA, 0, "maxvertexA")
        max_flowB = max_flow_generator(vertexGraphB)
        maxFileCreation(max_flowB, 0, "maxvertexB")
        max_flowC = max_flow_generator(vertexGraphC)
        maxFileCreation(max_flowC, 0, "maxvertexC")

        vertexGraphA = netCopyA
        vertexGraphB = netCopyB
        vertexGraphC = netCopyC

        for i in range(1, 15):
            vertexGraphA.augmentNetwork()
            testFileCreation(vertexGraphA, i, "vertexA")
            vertexGraphB.augmentNetwork()
            testFileCreation(vertexGraphB, i, "vertexB")
            vertexGraphC.augmentNetwork()
            testFileCreation(vertexGraphC, i, "vertexC")

            netCopyA = copy.deepcopy(vertexGraphA)
            netCopyB = copy.deepcopy(vertexGraphB)
            netCopyC = copy.deepcopy(vertexGraphC)

            max_flowA = max_flow_generator(vertexGraphA)
            maxFileCreation(max_flowA, i, "maxvertexA")
            max_flowB = max_flow_generator(vertexGraphB)
            maxFileCreation(max_flowB, i, "maxvertexB")
            max_flowC = max_flow_generator(vertexGraphC)
            maxFileCreation(max_flowC, i, "maxvertexC")

            string += "{} {} {} {}\n".format(i, max_flowA.elapsedTime, max_flowB.elapsedTime, max_flowC.elapsedTime)

            vertexGraphA = netCopyA
            vertexGraphB = netCopyB
            vertexGraphC = netCopyC

        fileName = "../data/vertexgraphcomparison"  + str(j)
        file = open(fileName + ".txt", 'w+')
        file.write(string)
        file.close()
        generateAndSave(fileName, numVA, numVB, numVC, "Vertices")

main()
