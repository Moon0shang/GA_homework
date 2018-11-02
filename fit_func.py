import numpy as np


def f_func(pop):

    # 1 range (-5.12,5.12)  min = 0 at (0,0)
    # y = np.power(pop[0], 2) + np.power(pop[1], 2)
    # 2 range (-2.048,2.048) min = 0 at (1,1)
    # y = 100 * np.power(pop[1]-np.power(pop[0], 2), 2) + np.power(pop[0]-1, 2)
    # 3 range (-2,2) min = 3 at (0,-1)
    '''
    y = (1 + np.power(pop[0]+pop[1]+1, 2)*(19-14*pop[0]+3 * np.power(pop[0], 2)-14*pop[1]+6*pop[0]*pop[1]+3*np.power(pop[1], 2)))*(
        30+(np.power(2*pop[0]-3*pop[1], 2))*(18 - 32*pop[0]+12*np.power(pop[0], 2)+48*pop[1]-36*pop[0]*pop[1]+27*np.power(pop[1], 2)))
    '''
    # 4 range (-6,6) min = 0 at (3,2)...*4
    '''
    y = np.power(np.power(pop[0], 2)+pop[1]-11, 2) + \
        np.power(pop[0]+np.power(pop[1], 2)-7, 2)
    '''
    # 5 range (-5,5) min = -1.031628 at (+-0.0898,-+0.7126)*2
    '''
    y = 4*np.power(pop[0], 2)-2.1*np.power(pop[0], 4)+(1/3)*np.power(pop[0],
                                                                     6)+pop[0]*pop[1]-4*np.power(pop[1], 2) + 4*np.power(pop[1], 4)
    '''
    # 6 range (-1,1) min = -0.24 at (0,+-0.23)*2
    '''
    y = np.power(pop[0], 2) + np.power(pop[1], 2) - 0.3 * np.cos(3 *
                                                                 np.pi * pop[0]) + 0.3 * np.cos(4 * np.pi * pop[1]) + 0.3
    '''
    # 7 range (-10,10) min = -186.73 at ...*18
    '''
    s1 = 0
    s2 = 0

    for i in range(5):
        i = i+1
        s1 += i * np.cos((i+1)*pop[0]+i)
        s2 += i * np.cos((i+1)*pop[1]+i)

    y = s1*s2
    '''
    # 8 range (-1,1) min = -2.118 at (+-0.64，+-0.64)
    '''
    y = 1 + pop[0] * np.sin(4 * np.pi * pop[0]) - pop[1] * np.sin(4 * np.pi * pop[1] + np.pi) + (np.sin(6 * np.sqrt(
        np.power(pop[0], 2) + np.power(pop[1], 2)))) / (6 * np.sqrt(np.power(pop[0], 2) + np.power(pop[1], 2)) + np.power(0.1, 15))
    '''
    # 9 range (-100,100) min = 0 at (0,...,0)
    # y = np.sum(np.power(pop, 2))
    # 10 range (-100,100) min = 0 at (0,...,0)
    # y = np.sum(np.power(np.floor(pop + 0.5), 2))
    # 11 range (-100,100) min = 0 at (0,...,0)
    # y = np.sum([np.power(np.sum(pop[:i]), 2) for i in range(pop.shape[0])])
    '''
    s1 = 0
    s2 = 0

    for i in range(pop.shape[0]):
        for j in range(i):
            s1 += pop[j]
        s2 += np.power(s1, 2)

    y = s2
    '''
    # 12 range (-10,10) min = 0 at (0,...,0)
    # y = np.sum(np.abs(pop)) + np.nanprod(np.abs(pop))
    # 13 A = 10 range (-5.12,5.12) min = 0 at (0,...,0)
    y = np.sum(10 + np.power(pop, 2) - 10 * np.cos(2 * np.pi * pop))
    # 14 range (-600,600) min = 0 at (0,...,0)
    '''
    s1 = np.sum(np.power(pop, 2)/4000)
    s2 = 1
    for i in range(pop.shape[0]):
        j = i+1
        s2 *= np.cos(pop[i]/np.sqrt(j))
    y = s1-s2+1
    '''
    # y = np.sum(np.power(pop, 2) / 4000) - np.nanprod(np.cos(pop) / i) + 1
    # 15 range (-32,32) min = 0 at (0,...,0)
    # y = -20*np.exp(-0.2*np.sqrt(np.sum(np.power(pop, 2))/pop.shape[0])) - np.exp(
    #   np.sum(np.cos(2 * np.pi * pop))/pop.shape[0]) + 20 + np.e
    # pop = round(pop, 2)
    '''
    s1 = 0
    s2 = 0
    len_p = pop.shape[0]
    for i in range(pop.shape[0]):
        s1 += pop[i]
        s2 += np.cos(2*np.pi*pop[i])
    y = -20*np.exp(-0.2*np.sqrt(s1/len_p))-np.exp(s2/len_p)+20+np.e
    '''
    '''
    s11 = np.sum(pop)
    s12 = pop.shape[0]
    s13 = np.sqrt(s11/s12)
    s1 = -20 * np.exp(-0.2 * s13)
    s2 = np.exp(np.sum(np.cos(2 * np.pi * pop))/pop.shape[0]) + 20 + np.e
    y = s1-s2
    '''
    # print('wait')
    # 16 range (-10,10) min = 0 at (0,...,0)
    '''
    s = 0

    for i in range(pop.shape[0]-1):
        s += 100*np.power((pop[i+1]-pop[i]), 2)+np.power(pop[i]-1, 2)

    y = s
    '''
    return y


# y = f_func([-0.64, -0.64])
# print(y)
