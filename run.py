import os
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
from GA_math import GA_core


def run(Ga, population, accuracy, name):

    neg_min = False

    for i in range(2000):
        y = Ga.fitness(population)
        # 判断最优值正负
        if np.min(y) < 0:
            neg_min = True

        new_pop = Ga.select(100, y, population, neg_min)
        bin_pop = Ga.encoding(new_pop)
        cr_pop = Ga.crossover(bin_pop)
        mu_pop = Ga.mutation(cr_pop)
        population = Ga.decoding(mu_pop)

        if (i+1) % 200 == 0:
            print("process %s have run %s times" % (name, i+1))
        # print('generation:'+'%s' % (i+1))


def visualize(Ga, i):

    # 趋势图
    fig = plt.figure()
    plt.plot(Ga.best_history)
    # plt.plot(ze, c='r')
    y = np.min(Ga.best_history)
    x = np.where(Ga.best_history == y)[0][0]
    plt.scatter(x, y, c='r')
    plt.text(len(Ga.best_history)/2, (y+np.max(Ga.best_history))/2,      # np.max(Ga.best_history)/2
             "best value:%s" % np.round(y, 6))
    plt.xlabel('generation')
    plt.ylabel('f(x,y)')
    plt.savefig('./math/13/%s.png' % i)
    # print('save')
    plt.close()


def mul_process(name):

    print('start process %s' % name)

    accuracy = 0.01
    Ga = GA_core(30, [-5.12, 5.12], accuracy,
                 crossover_rate=0.5, mutation_rate=0.0042)

    for i in range(3):

        Ga.reset()

        population = Ga.initial(100, 3)

        run(Ga, population, accuracy, name)
        #print('run%s' % name)
        # np.savetxt('C:/Users/X/Desktop/GA_math/2/%s.txt' % i, Ga.best_group_his)
        file_name = name + str(i)

        visualize(Ga, file_name)
        print('output pic%s' % file_name)


if __name__ == '__main__':

    try:
        os.mkdir('./math')
    except:
        print('file math alredy exist!')
    p1 = mp.Process(target=mul_process, args=('1-',))
    p2 = mp.Process(target=mul_process, args=('2-',))
    p3 = mp.Process(target=mul_process, args=('3-',))
    """     
    p4 = mp.Process(target=mul_process, args=('4-',))
    p5 = mp.Process(target=mul_process, args=('5-',))
    p6 = mp.Process(target=mul_process, args=('6-',))
    p7 = mp.Process(target=mul_process, args=('7-',))
    p8 = mp.Process(target=mul_process, args=('8-',))
    p9 = mp.Process(target=mul_process, args=('9-',))
    p0 = mp.Process(target=mul_process, args=('0-',)) """
    p1.start()
    p2.start()
    p3.start()
    """     
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p0.start() """
    p3.join()
