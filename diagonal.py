import imagepusher

if __name__ == '__main__':

	host, port = '', 18010

	width, height = 12, 10

	pusher = imagepusher.ImagePusher( (host, port) )

	while True:
		for i in range(120):
			frame = [ [ [(i+x)%120/20., (y-i)%120/60., (y-x+i)%120/12.] for x in xrange(width) ]
			                                                            for y in xrange(height) ]
			pusher.push_frame( frame )

