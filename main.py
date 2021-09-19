#!/usr/bin/env python3
from visualize import *

def do_main():
	vis = Visualizer(10,10)
	for i in range(10):
		for j in range(10):
			vis.explore(i,j)

if __name__  == '__main__':
	do_main()
