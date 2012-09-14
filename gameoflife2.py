import imagepusher, random, time

def get_random_bitmap(w, h):
	return [ [ random.randint(0,1) for x in xrange(w) ] for y in xrange(h) ]

def game_of_life(prev):
	w, h = len(prev[0]), len(prev)
	new = [ [ 0 for x in xrange(w) ] for y in xrange(h) ]
	for y in xrange(h):
		for x in xrange(w):
			n = 0
			for dx, dy in ( (-1, -1), (-1, 0), (-1, 1),
			                ( 0, -1),          ( 0, 1),
			                ( 1, -1), ( 1, 0), ( 1, 1) ):
				if prev[(y+dy)%h][(x+dx)%w]:
					n += 1
			if n == 3:
				new[y][x] = 1
			elif n == 2 and prev[y][x]:
				new[y][x] = 1

	return new

class FadeGameOfLife:

	def __init__(self, w, h, phase):
		self.cells_next = get_random_bitmap(w, h)
		self.phase = phase-1
		self.max_phase = phase
		self.w, self.h = w, h
		self.timeout = 64

	def next(self):
		w, h = self.w, self.h
		self.phase += 1
		if self.phase == self.max_phase:
			self.phase = 0
			self.cells_prev, self.cells_next = self.cells_next, game_of_life(self.cells_next)
			self.timeout -= 1
			if self.cells_prev == self.cells_next or self.timeout == 0:
				self.cells_next = get_random_bitmap(w, h)
				self.timeout = 64

		counterphase = (self.max_phase-self.phase)
		return [ [ float( self.cells_prev[y][x]*counterphase + 
		                  self.cells_next[y][x]*self.phase ) / self.max_phase for x in xrange(w) ]
		                                                                      for y in xrange(h) ]

if __name__ == '__main__':

	host, port = '', 18005
	pusher = imagepusher.ImagePusher( (host, port) )

	width, height = 12, 10
	phase = 20

	red_game = FadeGameOfLife(width, height, 2)
	green_game = FadeGameOfLife(width, height, 2)
	blue_game = FadeGameOfLife(width, height, 2)

	while True:

		red = red_game.next()
		green = green_game.next()
		blue = blue_game.next()

		frame = [ [ [red[y][x], green[y][x], blue[y][x]] for x in xrange(width) ]
		                                                 for y in xrange(height) ]
		pusher.push_frame( frame )

