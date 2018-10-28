import numpy as np
import matplotlib.pyplot as plt
from fit_func import f_func


class GA_core(object):

    def __init__(self, arg_num, arg_range, accuracy, crossover_rate=0.6, mutation_rate=0.01,  **args):

        self.arg_num = arg_num
        self.ranges = arg_range
        self.p_c = crossover_rate  # 0.4~0.9,mating when smaller than p_c
        self.p_m = mutation_rate   # 0.0001~0.1,mutation when smaller than p_m
        self.accuracy = accuracy
        self.length = self.get_length()
        self.best = 9999
        self.best_history = []
        self.best_group = []

    def get_length(self):

        bin_ranges = bin(int(self.ranges[1] / self.accuracy)).replace('0b', '')
        single_length = len(bin_ranges) + 1
        # total_length = single_length * self.arg_num

        return single_length

    def encoding(self, population):

        g_n = population.shape[0]
        a_n = population.shape[1]
        list_pop = []
        bin_pop1 = []
        for i in range(g_n):
            for j in range(a_n):
                population[i][j] = population[i][j] / self.accuracy
                bin_n = bin(int(population[i][j])).replace('0b', '')
                # 归一化二进制长度，负数第一位为-，正数为0

                sub = self.length - len(bin_n)
                if sub > 0:
                    if bin_n[0] == '-':
                        s = '0' * sub
                        s_list = ['-', s, bin_n[1:]]
                        bin_pop1.append(''.join(s_list))
                    else:

                        s = '0' * sub
                        s_list = [s, bin_n]
                        bin_pop1.append(''.join(s_list))
                else:
                    bin_pop1.append(bin_n)
            bin_pop = ''.join(bin_pop1)
            bin_pop1.clear()
            list_pop.append(list(bin_pop))

        return list_pop

    def decoding(self, list_pop):
        """
        ordinary algorithm
        l = 0
        s = 0
        for i in range(l):
            s += b[i] * (2 ** i)

        # decoding formula

        x = range_l + (range_r - range_l) / (2 ** l - 1) * s
        """
        l = len(list_pop)
        bin_pop = []
        for i in range(l):
            list_pop[i] = ''.join(list_pop[i])
        num_pop = np.empty([l, self.arg_num])
        for i in range(l):
            for j in range(self.arg_num):

                num_pop[i][j] = int(
                    list_pop[i][j*self.length:(j+1)*self.length], base=2) * self.accuracy

        return num_pop

    def initial(self, group_num):
        """
        group initialize, by generate random numbers
        should catious that the initial should obey the valid define
        if we have a good group, then we can improve the algorithm
        """
        # initial group
        population = np.random.uniform(
            self.ranges[0], self.ranges[1], [group_num, self.arg_num])
        population = np.round(population, 3)

        return population

    def fitness(self, population, epoch):

        group_num = len(population)

        y = np.empty(group_num)

        for i in range(group_num):
            y[i] = f_func(population[i])

        best = np.min(y)
        b = np.where(y == best)[0][0]

        if best < self.best:
            self.best = best
            best_population = population[b]
            self.best_group = best_population

        # a_p = self.best_group
        self.best_history.append(best)
        # print('best:', self.best)
        # print('y:', y)
        return y

    def select(self, fit, population):
        """
        choose better chromosome
        """
        total = 0
        fit1 = fit
        fit = np.reciprocal(fit)
        l = population.shape[0]
        pop_new = np.empty([l, self.arg_num])
        total = np.sum(fit)
        p0 = fit / total
        p = np.cumsum(p0)
        # 防止最后出现相加略小于1的情况
        p[-1] = 1

        c = np.random.rand(l)

        for i in range(l):

            s = np.where(p >= c[i])[0][0]
            pop_new[i] = population[s]

        return pop_new

    def crossover(self, pop_new):

        l = len(pop_new)
        p = np.random.rand(l)
        mating = np.where(p > self.p_c)[0]
        # 打乱数组
        np.random.shuffle(mating)
        l_v = len(mating)
        if l_v == 0:
            return pop_new

        elif l_v % 2 != 0:
            mating = mating[:-1]
            l_v = len(mating)

        for i in range(int(l_v/2)):
            pos = np.random.randint(self.length//2, self.length)
            for i in range(self.arg_num):
                idx1 = pos + self.length*self.arg_num
                idx2 = self.length*(self.arg_num+1)
                t = pop_new[mating[i*2]][idx1:idx2]
                pop_new[mating[i*2]][idx1:idx2] = pop_new[mating[i*2+1]][idx1:idx2]
                pop_new[mating[i*2+1]][idx1:idx2] = t

        return pop_new

    def mutation(self, cr_pop):

        l = len(cr_pop)

        for i in range(l):
            for k in range(2*self.length//3):
                k = k+self.length//3
                for j in range(self.arg_num):

                    p = np.random.rand()

                    if p < self.p_m:
                        # mutation, transfer 1 -> 0; 0 -> 1
                        # if cr_pop[i][k] != '-':
                        cr_pop[i][k+j*self.length] = str(
                            np.abs(int(cr_pop[i][k+j*self.length])-1))

        return cr_pop


if __name__ == '__main__':
    Ga = GA_core(2, [-5.12, 5.12], 0.0001)
    population = Ga.initial(500)

    for i in range(1000):
        y = Ga.fitness(population, i)
        new_pop = Ga.select(y, population)
        bin_pop = Ga.encoding(population)
        cr_pop = Ga.crossover(bin_pop)
        mu_pop = Ga.mutation(cr_pop)
        population = Ga.decoding(mu_pop)
        print('generation:'+'%s' % (i+1))

    print(Ga.best)
    print(Ga.best_group)
    fig = plt.figure()
    plt.plot(Ga.best_history)
    ze = [0 for i in range(1000)]
    plt.plot(ze, color='r')
    plt.show()
    # print(Ga.best_history)
