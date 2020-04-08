from cmath import sqrt
from GenerationAlgorithms import GenerationAlgorithms

def readFromFile(fileName):
    probParam={}

    probParam['matrix'] = []
    f = open(fileName, "r")
    probParam['noNodes'] = int(f.readline())
    for line in f:
        array = []
        currentline = line.split(",")
        for elem in currentline:
            array.append(float(elem))
        probParam['matrix'].append(array)
    f.close()
    return probParam

def CalculateFitness(path, probParam):
    matirx = probParam['matrix']
    fit = 0.0
    i = 0
    for j in range(len(path)):
        fit += matirx[i][path[j]]
        i = path[j]
    fit += matirx[i][0]
    return fit

def main():
    filename="in.txt"
    probParam=readFromFile(filename)
    probParam['function'] = CalculateFitness
    generationParam={'popSize': 400, 'noGen': 100}
    ga = GenerationAlgorithms(generationParam, probParam)
    ga.initialisation()
    ga.evaluation()
    g = -1
    while (g < generationParam['noGen']):
        g += 1
        ga.oneGeneration()
        #ga.oneGenerationElitism() 
        #ga.oneGenerationSteadyState()
        print("Generatia curenta: " + str(g) + "; "+ "Best fitness: " + str( ga.bestChromosome().fitness))
        cost = int(ga.bestChromosome().fitness)
        path = ga.bestChromosome().repres
        strpath = ''
        #path.insert(0, 0)
        for i in range(len(path)):
            strpath += str(path[i] + 1)
            if i != len(path) - 1:
                strpath += ','
        print("Traseu: " + "1,"+ strpath+",1")
        print("Cost: " + str(cost))

main()