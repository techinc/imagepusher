import imagepusher, random, cmath, math

def color(x, y, phase):

	phase *= 2 * math.pi

	rad, phi = cmath.polar(complex(x-5.5, y-4.5))

	phi /= 2.

	r, g, b = (math.sin( phi*2+phase*4 )+1.)/2., (math.sin(phi*2+phase)+1.)/2., (math.cos(-rad*1.5+phase*8.)*math.sin(phase/3.)+1.)/2.

	return r**4,g**4,b**4

if __name__ == '__main__':

	host, port = '', 18007
	pusher = imagepusher.ImagePusher( (host, port) )

	w, h = 12, 10

	n_phases = 128

	while True:

		for p in xrange(n_phases*6):
			phase = float(p)/n_phases

			screen = [ [ color(x, y, phase) for x in xrange(w) ] for y in xrange(h) ]
			pusher.push_frame( screen )

