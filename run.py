import numpy as np
import matplotlib.pyplot as plt
from GA_math import GA_core


def run(population, accuracy):

    neg_min = False

    for i in range(5000):
        y = Ga.fitness(population)
        # 判断最优值正负
        if np.min(y) < 0:
            neg_min = True

        new_pop = Ga.select(y, population, neg_min)
        bin_pop = Ga.encoding(new_pop)
        cr_pop = Ga.crossover(bin_pop)
        mu_pop = Ga.mutation(cr_pop)
        population = Ga.decoding(mu_pop)

        # print('generation:'+'%s' % (i+1))


def visualize(i):

    # 趋势图
    fig = plt.figure()
    plt.plot(Ga.baddest_history)
    # plt.plot(ze, c='r')
    y = np.min(Ga.best_history)
    x = np.where(Ga.best_history == y)[0][0]
    plt.scatter(x, y, c='r')
    plt.text(len(Ga.best_history)/2, (y+np.max(Ga.best_history))/2,      # np.max(Ga.best_history)/2
             "best value:%s" % np.round(y, 6))
    plt.xlabel('generation')
    plt.ylabel('f(x,y)')
    plt.savefig('C:/Users/X/Desktop/GA_math/13/%s.png' % i)
    plt.close()


if __name__ == '__main__':

    accuracy = 0.1
    Ga = GA_core(30, [-5.12, 5.12], accuracy,
                 crossover_rate=0.5, mutation_rate=0.0045)

    for i in range(30):
        Ga.reset()
        population = Ga.initial(100, 2)
        run(population, accuracy)
        # np.savetxt('C:/Users/X/Desktop/GA_math/2/%s.txt' % i, Ga.best_group_his)
        visualize(i)
        print('output pic%s' % i)
