"""
author: YuanQuan Xu
e-mail: jxgxxuyq@163.com

note: It's a homework of natrue calculation, 
which need to use GA to solve math function optimization!
"""
import numpy as np

from fit_func import f_func


class GA_core(object):

    def __init__(self, arg_num, arg_range, accuracy, crossover_rate=0.6, mutation_rate=0.06):

        self.arg_num = arg_num
        self.ranges = arg_range
        self.p_c = crossover_rate  # 0.4~0.9,mating when smaller than p_c
        self.p_m = mutation_rate   # 0.0001~0.1,mutation when smaller than p_m
        self.accuracy = accuracy
        self.length = self.get_length()

    def reset(self):
        """重置基本参数"""
        self.best = 999999
        self.best_history = []
        self.best_group = None

    def get_length(self):
        """获取最大二进制长度"""
        bin_ranges = bin(int(self.ranges[1] / self.accuracy)).replace('0b', '')
        single_length = len(bin_ranges) + 1

        return single_length

    def encoding(self, population):
        """编码"""
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
        """解码"""
        l = len(list_pop)
        num_pop = np.empty([l, self.arg_num])

        for i in range(l):
            list_pop[i] = ''.join(list_pop[i])

        for i in range(l):
            for j in range(self.arg_num):
                num_pop[i][j] = int(
                    list_pop[i][j*self.length:(j+1)*self.length], base=2) * self.accuracy

        return num_pop

    def initial(self, group_num, a):
        """初始化种群"""
        if a == 0:
            population = np.random.randint(
                self.ranges[0], self.ranges[1], [group_num, self.arg_num])
        else:
            population = np.random.uniform(
                self.ranges[0], self.ranges[1], [group_num, self.arg_num])
            # 保留小数位数
            population = np.round(population, a)

        return population

    def fitness(self, population):
        """计算种群适应度"""
        group_num = len(population)
        y = np.empty(group_num)

        for i in range(group_num):
            y[i] = f_func(population[i])

        best = np.min(y)
        # func 8
        # best = np.max(y)
        b = np.where(y == best)[0][0]
        best_pop = population[b]

        if best < self.best:
            self.best = best
            self.best_group = best_pop

        self.best_history.append(best)

        return y

    def select(self, fit, population, neg_min):
        """对种群进行选择"""
        l1 = population.shape[0]
        pop_new = np.empty([l1, self.arg_num])
        # 只保留前50% 的个体
        nn = 2
        l = l1//nn
        pop_new1 = np.empty([l, self.arg_num])
        '''
        func 8
        fit[fit < 0] = 0
        idx = np.argsort(fit)[-l:]
        '''
        # 最优值为正负时的不同操作
        if neg_min:
            fit[fit > 0] = 0
            # argsort 将fit值由小到大的顺序排列并输出原索引
            idx = np.argsort(fit)[:l]
        else:
            # 避免出现0无法取倒数的情况
            fit[fit == 0] = np.power(0.1, 40)
            fit = np.reciprocal(fit)
            idx = np.argsort(fit)[-l:]

        fit_rank = fit[idx]
        pop_rank = population[idx]
        total = np.sum(fit_rank)
        p0 = fit_rank / total
        p = np.cumsum(p0)
        # 防止最后出现相加略小于1的情况
        p[-1] = 1
        c = np.random.rand(l)

        for i in range(l):
            s = np.where(p >= c[i])[0][0]
            pop_new1[i] = pop_rank[s]

        for i in range(nn):
            pop_new[l*i:l*(i+1)] = pop_new1

        return pop_new

    def crossover(self, pop_new):
        """交叉操作"""
        # pop_ori = pop_new
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

        for i in range(l_v//2):
            pos = np.random.randint(1, self.length)
            for j in range(self.arg_num):
                idx1 = pos + self.length*j
                idx2 = self.length*(j+1)-1
                t = pop_new[mating[i*2]][idx1:idx2]
                pop_new[mating[i*2]][idx1:idx2] = pop_new[mating[i*2+1]][idx1:idx2]
                pop_new[mating[i*2+1]][idx1:idx2] = t

        return pop_new

    def mutation(self, cr_pop):
        """变异操作"""
        l = len(cr_pop)

        for i in range(l):
            for k in range(self.length-1):
                k = k + 1
                for j in range(self.arg_num):
                    p = np.random.rand()

                    if p < self.p_m:
                        # mutation, transfer 1 -> 0; 0 -> 1
                        cr_pop[i][k+j*self.length] = str(
                            np.abs(int(cr_pop[i][k+j*self.length])-1))

        return cr_pop
