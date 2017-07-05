import webbrowser

class Video():
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration
	
	def show_info(self):
		print (self.title)
		print (self.duration)

class Movie(Video):
	def __init__(self, movie_title, duration, movie_storyline, poster_image, trailer_youtube):
		Video.__init__(self, movie_title, duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

	def show_info(self):
		print (self.title)
		print (self.duration)
		print (self.stoyline)
