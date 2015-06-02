# Bringing in the provided functions for creating the webpage
from only_five import *

# This initializes the class and assigns attributes. There are 4 included by default.
# Don't change unless you also edit only_five.py to accept more info.
class Movie(object):
	def __init__(self, title, poster_image_url, trailer_youtube_url, description):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.description = description

# Creating variables for each of the films, as well as assigning the relevant data. 
# Additional films can be added here.
Highlander1 = Movie("Highlander", "http://www.cinemasterpieces.com/92010/billm2.jpg", "https://www.youtube.com/watch?v=omOZyLmNMJs", "I can't be 100 percent certain, but I think this is one of the films in the Highlander series.")
Highlander2 = Movie("Highlander II: The Quickening", "http://static.rogerebert.com/uploads/movie/movie_poster/highlander-2-the-quickening-1991/large_7W43CXQh6jF9NhnBnlA4BoaFp8W.jpg", "https://www.youtube.com/watch?v=YsgJltP__UA", "The Quickeningest film I've ever seen. It was over before I even knew it.")
Highlander3 = Movie("Highlander III: The Sorcerer", "http://img4.wikia.nocookie.net/__cb20140617222223/to-hollywood-and-beyond/images/d/d4/Highlander_III_The_Sorcerer.jpeg", "https://www.youtube.com/watch?v=eW_HzYMNOng", 'This movie is commonly referred to by its better-known title, "Sleepless in Seattle"')
Highlander4 = Movie("Highlander: Endgame", "http://iv1.lisimg.com/image/683335/600full-highlander%3A-endgame-poster.jpg", "https://www.youtube.com/watch?v=6Xfx0RKvA5s", "At long last, the respected Highlander film franchise completes its journey with this, the final film in the series.")
Highlander5 = Movie("Highlander: The Source", "http://images.moviepostershop.com/highlander-the-source-movie-poster-2007-1020406727.jpg", "https://www.youtube.com/watch?v=RQJeTwNFSSc", "I'm pretty sure this isn't a real film. Do you remember it coming out? I don't.")		
# Putting all of the films in a list that can be sent to the only_five function. 
# Any additional films need to be added to this list.
FavFilms = [Highlander1, Highlander2, Highlander3, Highlander4, Highlander5]

# This calls the only_five function to create the webpage.
# Do not change.
open_movies_page(FavFilms)