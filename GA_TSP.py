"""
author: YuanQuan Xu
e-mail: jxgxxuyq@163.com

note: It's a homework of natrue calculation, which need to use GA to solve TSP problem!
    For this problem, use interge encode may have easier operation.
"""

import numpy as np


class GA_core(object):

    def __init__(self, cross_rate, muta_rate, **args):

        self.p_c = cross_rate
        self.p_m = muta_rate

    def initail(self):
        """初始化"""
        pass

    def fitness(self):
        """计算适应度"""
        pass

    def select(self):
        """自然选择"""
        pass

    def cross(self):
        """交叉"""
        pass

    def mutation(self):
        """变异"""
        pass
