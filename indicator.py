#!/usr/bin/env python
# coding: utf-8


from datetime import timedelta
import math
import sys
import time


class Indicator:
	def __init__(self, func, data, clazz, post_func=None):
		self.func = func
		self.data = data
		self.clazz = clazz
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
				min_index = current_size
				max_index = min(current_size + batch_size, max_size)

				if clazz is not None:
					dis, gen = self.func(self.data[min_index, max_index], self.clazz[min_index, max_index])
				else:
					dis, gen = self.func(self.data[min_index, max_index])
		
				sum_dis += dis
				sum_gen += gen
		
				current_size += batch_size
				count += 1
	
				mean_dis = sum_dis / count
				mean_gen = sum_gen / count
				remain_size = max(max_size - current_size, 0)
				remain_time = timedelta(seconds=math.floor((time.time() - current_time) / current_size * remain_size))
				print('\repoch:{} dis:{} gen:{} size:{} time:{}         '.format(epoch + 1, mean_dis, mean_gen, remain_size, remain_time), end='', flush=True)

			print()
			
			if self.post_func is not None:
				self.post_func()



