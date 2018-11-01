import numpy as np
import matplotlib.pyplot as plt

from GA_TSP import GA_core
from get_dis import read_info


def run(populations, distances):
    """开始进化"""
    for i in range(1000):
        fit = tsp.fitness(populations, distances)
        pop_new = tsp.select(fit, populations)
        cr_pop = tsp.cross(pop_new)
        populations = tsp.mutation(cr_pop)


def show_trend():
    """趋势图"""
    fig = plt.figure()
    plt.plot(tsp.best_history)
    # plt.plot(ze, c='r')
    y = np.min(tsp.best_history)
    x = np.where(tsp.best_history == y)[0][0]
    plt.scatter(x, y, c='r')
    plt.text(len(tsp.best_history)/2, (y+np.max(tsp.best_history))/2,      # np.max(tsp.best_history)/2
             "best value:%s" % np.round(y, 6))
    plt.xlabel('generation')
    plt.ylabel('distance')
    plt.savefig('./trend.png')
    plt.close()


def visualize(locations):
    """可视化"""
    fig = plt.figure()
    order = []
    for i in tsp.best_group:
        order.append(locations[i])

    x = order[:][0]
    y = order[:][1]
    plt.plot(x, y)
    plt.scatter(x, y, c='r')


if __name__ == '__main__':

    locations, distances = read_info()
    city_num = locations.shape[0]
    tsp = GA_core(cross_rate=0.6, muta_rate=0.01,
                  group_num=100, city_num=city_num)
    tsp.reset()
    populations = tsp.initail()
    run(populations, distances)
    print(tsp.best)
    show_trend()
    visualize(locations)
