from indicator import Indicator
import numpy as np
import time


def train(data):
	time.sleep(0.1265)
	return 1, 2


if __name__ == '__main__':

	stub = np.arange(15000)

	bar = Indicator(train, stub, None, (lambda : print('d')))
	bar.start(100, 128)