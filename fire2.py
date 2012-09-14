import imagepusher, random

class Fire:

	def __init__(self, w, h):
		self.old = [ [ 0.0 ] * w for y in xrange(h) ]
		self.new = [ [ 0.0 ] * w for y in xrange(h) ]
		self.w, self.h = w, h 

	def next(self):
		w, h = self.w, self.h

		self.old, self.new = self.new, self.old
		
		for y in xrange(h):
			for x in xrange(w):
				s = 0.
				for dx in (-1, 0, 1):
					if y == h-1:
						s += random.choice( (0.0,1.0) )
					elif 0 <= x+dx < w:
						s += self.old[y+1][x+dx]
				self.new[y][x] = s/3.8
		
		return self.new

def color(x):
	r,g,b = (x**1.2*3, x**2*4., x**4)
	if r > 1.:
		r = 1.
	if g > 1.:
		g = 1.
	if b > 1.:
		b = 1.
	return r,g,b

if __name__ == '__main__':

	host, port = '', 18006
	pusher = imagepusher.ImagePusher( (host, port) )

	width, height = 12, 10

	fire = Fire(width*2, height*2)

	while True:
		img = fire.next()
		screen = [ [ color( (img[y*2][x*2]+img[y*2][x*2+1]+img[y*2+1][x*2]+img[y*2+1][x*2+1])/4. ) for x in xrange(width) ] for y in xrange(height) ]
		pusher.push_frame( screen )

