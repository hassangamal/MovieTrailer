import webbrowser


class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube, year):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year
    """to play moive in webbrowser"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
