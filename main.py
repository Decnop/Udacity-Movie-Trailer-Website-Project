import fresh_tomatoes


class Filme():
    """ This is the Filme class where the atributes and functions
        for the movies are defined.
        def __init__ method initializes a instance with the 3 parameters
        title (string), poster_image_url(string, trailer_youtube_url(string.

        fresh_tomatoes file is imported. Inside this module there is a method
        that creates the webpage.

        Line 32 is an example that creates creates the lord_of_the_rings
        instance with the parameters.

        At line 50 movies list is created,and all instances of Movie go inside

        The last code line calls the open_movies_page method, inside the
        fresh tomatoes file. Movies list is used as a parameter for the method.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

amnesia = Filme("Amnesia",
                "https://bit.ly/2ylPnj4",
                "https://www.youtube.com/watch?v=sHRiMXd5fos")

lord_of_the_rings = Filme("Lord of the Rings",
                          "https://bit.ly/2yNrYGv",
                          "https://www.youtube.com/watch?v=Pki6jbSbXIY")

independence_day = Filme("Independence Day",
                         "https://bit.ly/2CN8juQ",
                         "https://www.youtube.com/watch?v=cir-WCrVPSg")

black_panther = Filme("Black Panther",
                      "https://bit.ly/2nJLIWG",
                      "http://www.youtube.com/watch?v=EhQxxa1SKSM")

avengers = Filme("Avengers: Infinity War",
                 "https://bit.ly/2CPdBG7",
                 "http://www.youtube.com/watch?v=Aiv5sYzwGb8")

predator = Filme("The Predator",
                 "https://bit.ly/2P54gjk",
                 "https://www.youtube.com/watch?v=VPI9E-wNK8s")

movies = [amnesia, lord_of_the_rings, independence_day,
          black_panther, predator]

fresh_tomatoes.open_movies_page(movies)
