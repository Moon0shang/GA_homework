import numpy as np


def read_info():
    """读取tsp坐标数据"""
    with open('./ch150.tsp', 'r') as f:
        raw = f.read().split('NODE_COORD_SECTION')

    loc_list = raw[1].split('EOF')[0].replace('\n', '').split(' ')
    loc_valid = list(filter(lambda n: n != '', loc_list))
    loc_raw = list(filter(lambda n: len(n) > 2, loc_valid))
    locations = np.array(loc_raw, dtype=np.float32)
    locations = locations.reshape(len(locations) // 2, 2)

    """     dis = raw[0].split('EDGE_WEIGHT_SECTION')[1]
    dis_list = dis.replace('\n', '').split(' ')
    dis_valid = list(filter(lambda n: n != '', dis_list))
    distances = np.array(dis_valid, dtype=np.float32)
    l = locations.shape[0]
    distances = distances.reshape([l, l]) """

    return locations  # , distances


def cal_dis(loc):
    """计算各城市之间的距离"""
    l = loc.shape[0]
    dis = np.empty([l, l])
    for i in range(l):
        for j in range(l):
            dis[i][j] = np.sqrt(
                np.power(loc[i][0]-loc[j][0], 2) + np.power(loc[i][1]-loc[j][1], 2))

    return dis


def fitness(pop, dis):
    """获取长度"""
    total_dis = dis[pop[0]][pop[-1]]

    for i in range(len(pop)-1):
        total_dis += dis[pop[i]][pop[i + 1]]

    return total_dis
