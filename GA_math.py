import random
import numpy as np


class GA_core(object):

    def __init__(self, arg_range, crossover_rate, mutation_rate, accuracy, **args):

        self.ranges = arg_range
        self.p_c = crossover_rate  # 0.4~0.9,mating when smaller than p_c
        self.p_m = mutation_rate   # 0.0001~0.1,mutation when smaller than p_m
        self.accuracy = accuracy
        self.best = None
        # self.population = []
        self.generation = 1
        self.cross_count = 0
        self.mutation_count = 0

    def get_length(self, arg_num):

        bin_ranges = bin(self.ranges[1]).replace('0b', '')
        single_length = len(bin_ranges) + 1
        total_length = single_length * arg_num

        return single_length, total_length

    def encoding(self, number, single_length):

        number = number / self.accuracy
        bin_num = bin(number).replace('0b', '')
        # 归一化二进制长度，负数第一位为-，正数为0
        if bin_num[0] == '-':
            sub = single_length - len(bin_num)
            if sub > 0:
                s = '0' * sub
                s_list = ['-', s, bin_num[1:]]
                bin_num = ''.join(s_list)
        else:
            sub = single_length - len(bin_num)
            s = '0' * sub
            s_list = [s, bin_num]
            s_list = ''.join(s_list)

        return bin_num

    def decoding(self, bin_num):
        """
        ordinary algorithm
        l = 0
        s = 0
        for i in range(l):
            s += b[i] * (2 ** i)

        # decoding formula

        x = range_l + (range_r - range_l) / (2 ** l - 1) * s
        """

        number = int(bin_num, base=2) * self.accuracy

        return number

    def initial(self, group_num, arg_num):
        """
        group initialize, by generate random numbers
        should catious that the initial should obey the valid define
        if we have a good group, then we can improve the algorithm
        """
        # initial group
        group = np.random.uniform(
            self.range[0], self.range[1], [group_num, arg_num])

        # transfer number to binary list representation
        for i in range(group_num):
            for j in range(arg_num):

                population[i][j] = self.encoding(group[i][j])

        return population


"""
    def fitness_function(self, f, arg_num, x):
        """
        fitness function are using to evaluate the adaption of each chromosome
        it was always confirmed by the destination
        the better the adoption, the better the chromosome
        """
        # decoding
        for i in range(arg_num):
            x[i] = self.decoding(x[i])

        if f == 1:
            y = x[0] ** 2 + x[1] ** 2
        elif f == 2:
            y = 100 * ((x[1] - x[0] ** 2) ** 2) + (x[0] - 1) ** 2
        elif f == 3:
            y = (1+(x[0]+x[1]+1)**2+(19-14*x[0]+(3*(x[1]**2)-14*x[0]+6*x[0]*x[1]+3*(x[0**2]))) *
                 (30+(2*x[0]-3*(x[1]**2)**2)*(18-32*x[0]+12*(x[0]**2)+48*x[1]-36*x[0]*x[1]+27*x[1])))
        elif f == 4:
            y = (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2
        elif f == 5:
            y = 4 * (x[0] ** 2) - 2.1 * (x[0] ** 4) + (1 / 3) * (x[0]
                                                                 ** 6) + x[0] * x[1] - 4 * (x[1] ** 2) + 4 * (x[1] ** 4)
        elif f == 6:
            y = x[0] ** 2 + x[1] ** 2 - 0.3 * \
                np.cos(3 * np.pi * x[0]) + 0.3 * np.cos(4 * np.pi * x[1]) + 0.3
        elif f == 7:
            print('no functions!')
        elif f == 8:
            y = 1+x*np.sin(4*np.pi*x[0])-x[1]*np.sin(4*np.pi*x[1]+np.pi)+(np.sin(6*np.sqrt(np.power(
                x[0], 2)+np.power(x[1], 2))))/(6*np.sqrt(np.power(x[0], 2)+np.power(x[1], 2))+np.power(10, -15))
        elif f == 9:
            y = np.sum(np.power(x, 2))
        elif f == 10:
            y = np.sum(np.power(np.ceil(x + 0.5), 2))
        elif f == 11:
            y = np.sum(np.power(np.sum(x), 2))
        elif f == 12:
            y = np.sum(np.abs(x)) + np.nanprod(x)
        elif f == 13:
            print('no functions!')
        elif f == 14:
            np.sum(np.power(x, 2) / 4000) - np.nanprod(np.cos(x) / i) + 1
        elif f == 15:
            y = -20 * np.exp(-0.2 * np.sqrt(np.sum(x) / len(x))) - \
                np.exp(np.sum(np.cos(2 * np.pi * x))) + 20 + np.e
        elif f == 16:
            s = 0
            for i in range(len(x)-1):
                s += np.power((x[i+1]-x[i]), 2)
            y = 100*(s+np.sum(np.power(x-1, 2)))
 """
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
