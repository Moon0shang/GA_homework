import numpy as np
import matplotlib.pyplot as plt

from GA_TSP import GA_core
from get_dis import *


def run(pop, dis):
    """开始进化"""
    for i in range(5000):
        fit = tsp.fitness(pop, True)
        pop_new = tsp.select(fit, pop)
        cr_pop = tsp.cross(pop_new)
        pop = tsp.mutation(cr_pop)

        if i % 200 == 0:
            print("have run %s times" % i)


def show_trend():
    """趋势图"""
    fig = plt.figure()
    plt.plot(tsp.best_history)
    # plt.plot(ze, c='r')
    y = np.min(tsp.best_history)
    x = np.where(tsp.best_history == y)[0][0]
    plt.scatter(x, y, c='r')
    plt.text(len(tsp.best_history)/2, (y+np.max(tsp.best_history))/2,      # np.max(tsp.best_history)/2
             "min distance:%s" % y)
    plt.xlabel('generation')
    plt.ylabel('distance')
    plt.savefig('./trend.png')
    plt.show()
    plt.close()


def visualize(loc):
    """可视化"""
    fig = plt.figure()
    order = np.empty([loc.shape[0] + 1, 2])

    for i in range(len(tsp.best_group)):
        order[i] = loc[i]

    order[-1] = order[0]
    x = order[:, 0]
    y = order[:, 1]
    plt.plot(x, y)
    plt.scatter(x, y, c='r')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.text(order[0][0], order[0][1], 'start')
    plt.text(order[-2][0], order[-2][1], 'end')
    plt.savefig('./route.png')
    plt.show()
    plt.close()


if __name__ == '__main__':

    # [locations, distances] = read_info()
    locations = read_info()
    distances = cal_dis(locations)
    city_num = locations.shape[0]
    tsp = GA_core(cross_rate=0.9, muta_rate=0.2,
                  group_num=100, city_num=city_num,
                  dis=distances)
    tsp.reset()
    populations = tsp.initail()
    run(populations, distances)
    print(tsp.best)
    show_trend()
    visualize(locations)
