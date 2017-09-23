import webbrowser

class Movie():
    """The movie class allows to create movie instances to store information"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """The constructor of the movie class uses storyline,
        poster image and youtube trailer url to instanciate an object"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This method opens the movie trailer in a new browser window"""
        webbrowser.open(self.trailer_youtube_url)
