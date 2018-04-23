import webbrowser


class Movie():
    """ Class for Movie with trailer preview function """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Constructor to intantiate movie parameters """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in a web browser """
        webbrowser.open(self.trailer_youtube_url)

