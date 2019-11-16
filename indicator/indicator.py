#!/usr/bin/env python
# coding: utf-8

import sys
import time
import numpy as np
from datetime import timedelta
import math


class Indicator:
    def __init__(self, func, data, post_func=None):
        self.func = func
        self.data = data
        self.post_func = post_func
    
    def start(self, epochs, batch_size):
        max_size = len(self.data)
        for epoch in range(epochs):
            
            current_time = time.time()
            current_size = 0
            sum_dis = 0
            sum_gen = 0
            count = 0
            
            while current_size < max_size:
                dis, gen = train(stub[current_size:min(current_size + batch_size, max_size)])
        
                sum_dis += dis
                sum_gen += gen
        
                current_size += batch_size
                count += 1
    
                mean_dis = sum_dis / count
                mean_gen = sum_gen / count
                remain_size = max(max_size - current_size, 0)
                remain_time = timedelta(seconds=math.floor((time.time() - current_time) / current_size * remain_size))
                sys.stdout.write('epoch:{}\tdis:{}\tgen:{}\tsize:{}\ttime:{}\t\r'.format(epoch + 1, mean_dis, mean_gen, remain_size, remain_time))
    
            sys.stdout.write('\n')
            
            if self.post_func is not None:
                self.post_func()


# stub = np.arange(50)

# def train(data):
#     time.sleep(0.1265)
#     return 1, 2


# bar = Indicator(train, stub, (lambda : print('d')))
# bar.start(100, 64)



