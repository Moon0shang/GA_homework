"""
author: YuanQuan Xu
e-mail: jxgxxuyq@163.com

note: It's a homework of natrue calculation, which need to use GA to solve TSP problem!
    For this problem, use interge encode may have easier operation.
"""

import numpy as np
from fit_tsp import fit_func


class GA_core(object):

    def __init__(self, cross_rate, muta_rate, group_num, **args):

        self.p_c = cross_rate
        self.p_m = muta_rate
        self.g_num = group_num
        self.best = 99999999
        self.best_history = []

    def initail(self, city_num):
        """初始化"""
        population = []

        for i in range(self.g_num):
            rand_pop = [j for j in range(city_num)]
            population.append(np.random.shuffle(rand_pop))

        return population

    def fitness(self, pop):
        """计算适应度"""
        y = np.empty(self.g_num)
        for i in range(self.g_num):
            y[i] = fit_func(pop[i])

        best = np.min(y)
        b = np.where(y == best)[0][0]
        best_group = pop[b]

        if best < self.best:
            self.best = best
            self.best_group = best_group

        self.best_history.append(best)

        return y

    def select(self, fit, pop):
        """自然选择"""
        total = np.sum(fit)
        p0 = fit/total
        p = np.cumsum(p0)
        p[-1] = 1
        c = np.random.rand(self.g_num)

        pop_new = [None]*self.g_num
        for i in range(self.g_num):
            s = np.where(p >= c[i])[0][0]
            pop_new[i] = pop[i]

        return pop_new

    def cross(self):
        """交叉"""
        pass

    def mutation(self):
        """变异"""
        pass
