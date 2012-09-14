import imagepusher, Image

imgfile = './imgs/test2.png'
#imgfile = './imgs/techinc-ad1.png'
#imgfile = './imgs/techinc-ad2.png'

def normalise(colour):
	r,g,b = colour
	return [r/255.,g/255.,b/255.]

if __name__ == '__main__':

	host, port = '', 18003
	pusher = imagepusher.ImagePusher( (host, port) )

	width, height = 12, 10


	image = Image.open(imgfile)
	image = image.convert(mode='RGB')
	img_width, img_height = image.size
	image = image.crop( (0, 0, img_width, height) )
	data = image.getdata()

	while True:
		for i in xrange(img_width-width):
			frame = [ [ normalise(data[i+x+y*img_width]) for x in xrange(width) ]
			                                             for y in xrange(height) ]
			pusher.push_frame( frame )

