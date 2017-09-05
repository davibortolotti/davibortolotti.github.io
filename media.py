# defining class where movie data will be stored
class Movie():
    # constructor method:
    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        print("The movie " + self.title + " was defined")   # proof-check
