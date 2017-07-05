import webbrowser

# A superclass about Videos
class Video():
    '''a class for vieos. Currently only with attribute title (str).'''
    
    def __init__(self, title):
        self.title = title
        
    def show_info(self): # print the title 
        print (self.title)

# The Movie-Class (inheriting Video) with the title, storyline, URLs to the poster and the youtube trailer      
class Movie(Video):
    '''a class for movies.
    
       inherits Video, from which inherits the attribute title
       
       additionally keeps the attributes: 
            storyline (str): the storyline of the title
            poster_image_url (str): url pointing to a picture poster of the movie
            trailer_youtube_url (str): url pointing to the trailer of the video on youtube 
        
        movie_title, movie_storyline, poster_image_url and trailer_youtube_url need to be passed in on initialisation of any class instance
            
        The function show_trailer opens the trailer in a browser.
        The function show_info prints title and storyline.
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self): # open a Browser and show the trailer
        webbrowser.open(self.trailer_youtube_url)

    def show_info(self): # print the Title and the Storyline
        print (self.title)
        print (self.stoyline)
