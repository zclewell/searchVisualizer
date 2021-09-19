#!/usr/bin/env python3
import pygame

WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)  
GREY  = (100,100,100)

class Visualizer:
	def __init__(self, r, c, pixel_size=50, edge_width=1, tail_length=5):
		self.r = r
		self.c = c
		self.pixel_size = pixel_size
		self.edge_width = edge_width
		self.tail_length = tail_length
		self.tail = []
		pygame.init()
		self.display = pygame.display.set_mode((self.r * self.pixel_size, self.c * self.pixel_size))

		self.display.fill(WHITE)
		for i in range(r):
			for j in range(c):
				pygame.draw.rect(self.display, BLACK, (i * self.pixel_size, j * self.pixel_size, self.pixel_size, self.pixel_size), width=self.edge_width)
		pygame.display.update()
	def _update_pos(self, i, j, color, update=True):
		pygame.draw.rect(self.display, color, ((i * self.pixel_size) + self.edge_width, (j * self.pixel_size) + self.edge_width, self.pixel_size - (self.edge_width * 2), self.pixel_size - (self.edge_width * 2)))
		if update:
			pygame.display.flip()

	def explore(self, i, j):
		if len(self.tail) > self.tail_length:
			self.tail = self.tail[-self.tail_length:]

		if len(self.tail) > 0:
			(ii, jj) = self.tail[0]
			self._update_pos(ii, jj, GREY)	
			for idx, (ii, jj) in enumerate(self.tail[1::1]):
				self._update_pos(ii, jj, (GREY[0] + int((RED[0] - GREY[0]) * (idx / self.tail_length)), 0, 0))

		self._update_pos(i,j,RED)
		self.tail.append((i,j))

