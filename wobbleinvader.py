import imagepusher, random, cmath, math

def color(x, y, phase, opacity):

	phase *= 2 * math.pi

	rad, phi = cmath.polar(complex(x-5.5, y-4.5))

	phi /= 2.

	r, g = (math.sin( phi*2+phase*4 )+1.)/2., (math.sin(phi*2+phase)+1.)/2.

	b = (2. - r - g)/2.
	if b > 1.:
		b = 1.

	return r**4 * opacity, g**4 * opacity, b**4 * opacity

if __name__ == '__main__':

	X = True
	_ = False

	sprite= (
	[
		[_,_,_,_,_,_,_,_,_,_,_,_,],
		[_,_,_,X,_,_,_,_,_,X,_,_,],
		[_,_,_,_,X,_,_,_,X,_,_,_,],
		[_,_,_,X,X,X,X,X,X,X,_,_,],
		[_,_,X,X,_,X,X,X,_,X,X,_,],
		[_,X,X,X,X,X,X,X,X,X,X,X,],
		[_,X,_,X,X,X,X,X,X,X,_,X,],
		[_,X,_,X,_,_,_,_,_,X,_,X,],
		[_,_,_,_,X,X,_,X,X,_,_,_,],
		[_,_,_,_,_,_,_,_,_,_,_,_,],
	],
	[
		[_,_,_,_,_,_,_,_,_,_,_,_,],
		[_,_,_,X,_,_,_,_,_,X,_,_,],
		[_,X,_,_,X,_,_,_,X,_,_,X,],
		[_,X,_,X,X,X,X,X,X,X,_,X,],
		[_,X,X,X,_,X,X,X,_,X,X,X,],
		[_,X,X,X,X,X,X,X,X,X,X,X,],
		[_,_,X,X,X,X,X,X,X,X,X,_,],
		[_,_,_,X,_,_,_,_,_,X,_,_,],
		[_,_,X,_,_,_,_,_,_,_,X,_,],
		[_,_,_,_,_,_,_,_,_,_,_,_,],
	])

	host, port = '', 18011
	pusher = imagepusher.ImagePusher( (host, port) )

	w, h = 12, 10

	n_phases = 128

	while True:

		c = 0

		for p in xrange(n_phases*6):
			phase = float(p)/n_phases

			screen = [ [ color(x, y, phase, sprite[int(c/5)][y][x]) for x in xrange(w) ] for y in xrange(h) ]
			pusher.push_frame( screen )

			c = (c+1)%10

