import imagepusher, random

if __name__ == '__main__':

	host, port = '', 18002
	pusher = imagepusher.ImagePusher( (host, port) )

	width, height = 12, 10

	munch = [ [ [0,0,0] for x in xrange(width) ] for y in xrange(height) ]

	while True:
		for i in xrange(16):
			for j in xrange(i+1):
				for y in xrange(height):
					for x in xrange(width):
						if y == (x ^ j):
							munch[y][x][0] += 1
							munch[y][x][0] %= 256
							munch[y][x][1] += 5
							munch[y][x][1] %= 256
							munch[y][x][2] += 9
							munch[y][x][2] %= 256
		
			frame = [ [ [n/255., m/255., o/255.] for n,m,o in row ] for row in munch ]
			pusher.push_frame( frame )

