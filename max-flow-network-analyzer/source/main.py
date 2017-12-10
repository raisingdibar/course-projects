from max_flow_generator import *
from test_network_generator import *
import os

def testFileCreation(network, graphNum):
    '''
    A class that creates an output dot file based on the test network created

    network - the test_network_generator class being converted to dot file
    graphNum - Number of graph so each is unique
    '''

    string = "digraph g{\n\nrankdir = LR\n\n"
    for tup in network.edges:
        string += '{} -> {} [label = " {} "];\n'.format(tup[0], tup[1], tup[3])

    string += '\nlabel = "graph {:02d}"\n'.format(graphNum)
    string += '}'
    print(string, "\n")

    fileName = "../input_graphs/graph{}.dot".format(graphNum)
    file = open(fileName, 'w+')
    file.write(string)

    file.close()

def maxFileCreation(maxGen, graphNum):
    '''
    A class that creates an output dot file based on the max network created

    network - the max_flow_generator class being converted to dot file
    graphNum - Number of graph so each is unique
    '''
    network = maxGen.network

    string = "digraph g{\n\nrankdir = LR\n\n"
    for tup in network.edges:
        string += '{} -> {} [label = " {}/{} "];\n'.format(tup[0], tup[1], tup[2], tup[3])

    string += '\nlabel = "graph {:02d}: maximum flow = {} "\n'.format(graphNum, maxGen.max_flow)
    string += '}'
    print(string, "\n")

    fileName = "../output_graphs/graph{}.dot".format(graphNum)
    file = open(fileName, 'w+')
    file.write(string)

    file.close()

def main():
    for i in range(1,11):
        testGraph = test_network_generator()
        testFileCreation(testGraph, i)
        maxGen = max_flow_generator(testGraph)
        maxFileCreation(maxGen, i)

        os.environ['PATH'] += ":"+"/usr/local/bin"
        filenameIn = "../input_graphs/graph{}.dot".format(i)
        filenameOut = "../input_graphs/graph{}.png".format(i)
        print(os.system("dot -Tpng " +filenameIn+ " -o" +filenameOut))

        filenameIn = "../output_graphs/graph{}.dot".format(i)
        filenameOut = "../output_graphs/graph{}.png".format(i)
        print(os.system("dot -Tpng " +filenameIn+ " -o" +filenameOut))

main()
