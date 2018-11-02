import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

from GA_TSP import GA_core
from get_dis import *


def run(tsp, pop, dis, name):
    """开始进化"""
    for i in range(10000):
        fit = tsp.fitness(pop)
        pop_new = tsp.select(fit, pop)
        cr_pop = tsp.cross(pop_new)
        pop = tsp.mutation(cr_pop)

        if i > 3000:
            tsp.p_m = 0.3

        if (i+1) % 1000 == 0:
            print("process %s have run %s times" % (name, i+1))


def show_trend(tsp, i):
    """趋势图"""
    fig = plt.figure()
    plt.plot(tsp.best_history)
    # plt.plot(ze, c='r')
    y = np.min(tsp.best_history)
    x = np.where(tsp.best_history == y)[0][0]
    plt.scatter(x, y, c='r')
    plt.text(len(tsp.best_history)/2, (y+np.max(tsp.best_history))/2,      # np.max(tsp.best_history)/2
             "min distance:%s" % np.round(y, 1))
    plt.xlabel('generation')
    plt.ylabel('distance')
    plt.savefig('./tsp/trend%s.png' % i)
    # plt.show()
    plt.close()


def visualize(tsp, loc, j):
    """可视化"""
    fig = plt.figure()
    order = np.empty([loc.shape[0] + 1, 2])

    for i in range(len(tsp.best_group)):
        order[i] = loc[tsp.best_group[i]]

    order[-1] = order[0]
    x = order[:, 0]
    y = order[:, 1]
    plt.plot(x, y)
    plt.scatter(x, y, c='r')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.text(order[0][0], order[0][1], 'start')
    plt.text(order[-2][0], order[-2][1], 'end')
    plt.savefig('./tsp/route%s.png' % j)
    # plt.show()
    plt.close()


def mul_process(name):
    """使用多个进程加快速度"""
    locations = read_info()
    distances = cal_dis(locations)
    city_num = locations.shape[0]
    start = 0
    tsp = GA_core(cross_rate=0.6, muta_rate=0.01,
                  group_num=100, city_num=city_num,
                  dis=distances)
    for i in range(2):
        print('generation %s' % i)
        tsp.reset()
        populations = tsp.initail(start)
        run(tsp, populations, distances, name)
        print(tsp.best)
        file_name = name+str(i)
        show_trend(tsp, file_name)
        visualize(tsp, locations, file_name)


if __name__ == '__main__':

    p1 = mp.Process(target=mul_process, args=('1-',))
    p2 = mp.Process(target=mul_process, args=('2-',))
    p3 = mp.Process(target=mul_process, args=('3-',))
    p1.start()
    p2.start()
    p3.start()
    p3.join()


""" 
    for i in range(30):
        print('generation %s' % i)
        tsp.reset()
        populations = tsp.initail(start)
        run(populations, distances)
        print(tsp.best)
        show_trend(i)
        visualize(locations, i) """
