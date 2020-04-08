from random import randint


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__repres = self.__generateRandomPermutation(self.__problParam['noNodes'] - 1)
        self.__fitness = 0.0

    def __generateRandomPermutation(self, list):
        permutation = [i + 1 for i in range(list)]
        ind1 = randint(0, list - 1)
        ind2 = randint(0, list - 1)
        permutation[ind1], permutation[ind2] = permutation[ind2], permutation[ind1]
        return permutation

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        pos1 = randint(-1, self.__problParam['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        pos1 = randint(0, self.__problParam['noNodes'] - 2)
        pos2 = randint(0, self.__problParam['noNodes'] - 2)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        element = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, element )

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness