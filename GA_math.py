import random


class GA_core(object):

    def __init__(self, arg_range, crossover_rate, mutation_rate, **args):

        self.range = arg_range
        self.p_c = crossover_rate  # 0.4~0.9,mating when smaller than p_c
        self.p_m = mutation_rate   # 0.0001~0.1,mutation when smaller than p_m
        self.best = None
        self.population = []
        self.generation = 1
        self.cross_count = 0
        self.mutation_count = 0

    def encoding(self, range_l, range_r):

        pass

    def decoding(self, b, range_l, range_r):

        l = 0
        s = 0
        for i in range(l):
            s += b[i] * (2 ** i)
        # decoding formula
        x = range_l + (range_r - range_l) / (2 ** l - 1) * s

        return x

    def initial(self):
        """
        group initialize, by generate random numbers
        should catious that the initial should obey the valid define
        if we have a good group, then we can improve the algorithm
        """
        pass

    def fitness_function(self):
        """
        fitness function are using to evaluate the adaption of each chromosome
        it was always confirmed by the destination
        the better the adoption, the better the chromosome
        """
        pass

    def select(self, fit, l):

        total = 0
        p = []
        for i in range(len(self.population)):
            total += fit[i]
        for i in range(len(l)):
            p[i] = fit[i]/total
        '''rank mechanism: choose the best k ones'''
        return p

    def crossover(self, l):

        p = random.random()
        if p < self.p_c:
            # cross
            position = random.randint(range(l), 3).sort()
        else:
            # copy
            pass

    def mutation(self, l):

        p = random.random()
        if p < self.p_m:
            # mutation
            postion = random.randint(0, l)

    def update_group(self):
        """
        parent be replaced by new ones, all or partly
        """
        pass
