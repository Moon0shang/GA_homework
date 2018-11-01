"""
author: YuanQuan Xu
e-mail: jxgxxuyq@163.com

note: It's a homework of natrue calculation, which need to use GA to solve TSP problem!
    For this problem, use interge encode may have easier operation.
"""

import numpy as np


class GA_core(object):

    def __init__(self, cross_rate, muta_rate, group_num, city_num, **args):

        self.p_c = cross_rate
        self.p_m = muta_rate
        self.g_num = group_num
        self.city_num = city_num

    def reset(self):
        self.best = 99999999
        self.best_history = []
        self.best_group = None

    def initail(self):
        """初始化"""
        population = []

        for i in range(self.g_num):
            rand_pop = [j for j in range(self.city_num)]
            population.append(np.random.shuffle(rand_pop))

        return population

    def fitness(self, pop, dis):
        """计算适应度"""
        y = np.empty(self.g_num)

        for i in range(self.g_num):
            total_dis = dis[pop[i][0]][pop[i][-1]]

            for j in range(self.city_num-1):
                total_dis += dis[pop[i][j]][pop[i][j + 1]]

            y[i] = total_dis

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
        pop_new = [None] * self.g_num

        for i in range(self.g_num):
            s = np.where(p >= c[i])[0][0]
            pop_new[i] = pop[i]

        return pop_new

    def cross(self, pop):
        """交叉"""
        p = np.random.rand(self.g_num)
        mating = np.where(p > self.p_c)[0]
        np.random.shuffle(mating)
        city_code = [i for i in range(self.city_num)]
        l_v = len(mating)

        if l_v == 0:
            return pop

        elif l_v % 2 != 0:
            mating.pop()
            l_v = len(mating)

        for i in range(l_v // 2):
            pos = np.sort(np.random.choice(city_code, 2))
            new_pop1 = pop[mating[2 * i]][pos[0]:pos[1]]
            new_pop2 = pop[mating[2 * i + 1]][pos[0]: pos[1]]
            pop[mating[2 * i]
                ] = self.gen_new(pop[mating[2 * i]], pos, new_pop2)
            pop[mating[2 * i + 1]
                ] = self.gen_new(pop[mating[2 * i + 1]], pos, new_pop1)

        return pop

    def gen_new(self, mating, pos, seg_pop):
        """产生交叉后的新后代"""
        pop_temp = []

        for i in mating:

            if i not in seg_pop:
                pop_temp.append(i)

        mating[0:pos[0]] = pop_temp[0:pos[0]]
        mating[pos[0]: pos[1]] = seg_pop
        mating[pos[1]:] = pop_temp[pos[1]:]

        return mating

    def mutation(self, population):
        """变异"""
        city_code = [i for i in range(self.city_num)]
        for pop in population:
            p = np.random.rand()
            if p < self.p_m:
                pos = np.random.choice(city_code, 2)
                pop[pos[0]], pop[pos[1]] = pop[pos[1]], pop[pos[0]]

        return population
