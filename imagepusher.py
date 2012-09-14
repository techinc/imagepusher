import BaseHTTPServer, json

class FrameRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

	def do_POST(self):
		try:
			if self.path == '/timeCycle':
				self.send_response(200)
				self.send_header('Content-type', 'text/plain')
				self.end_headers()
				self.wfile.write(self.server.current_frame)
				self.server.pushed = True
			if self.path in ( '/init', '/stop' ):
				self.send_response(200)
				self.send_header('Content-type', 'text/plain')
				self.end_headers()
				self.wfile.write('')
				self.server.running = (self.path == '/init')
		except IOError:			
			self.send_error(404, 'File Not Found')

	def do_GET(self):
		self.do_POST()

	def log_message(self, *args):
		pass

class ImagePusher:

	def __init__(self, address):
		self.httpd = BaseHTTPServer.HTTPServer(address, FrameRequestHandler)
		self.httpd.current_frame = None
		self.httpd.pushed = False
		self.httpd.running = False

	def push_frame(self, frame):
		w, h = len(frame[0]), len(frame)
		content = [ [ frame[y][w-x-1] for y in xrange(h) ] for x in xrange(w) ]
		self.httpd.pushed = False
		self.httpd.current_frame = json.dumps( {'type':'bitmap', 'content': content} )
		#while not self.httpd.running or not self.httpd.pushed:
		while not self.httpd.pushed:
			self.httpd.handle_request()
		self.httpd.pushed = True

if __name__ == '__main__':

	host, port = '', 18000

	width, height = 12, 10

	pusher = ImagePusher( (host, port) )

	while True:
		for i in range(120):
			frame = [ [ [(i+x)%120/20., (y-i)%120/60., (y-x+i)%120/12.] for x in xrange(width) ]
			                                                            for y in xrange(height) ]
			pusher.push_frame( frame )

