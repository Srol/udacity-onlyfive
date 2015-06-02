# Bringing in the provided functions for creating the webpage
from only_five import *

# This initializes the class and assigns attributes. There are 4 by default.
# Don't change unless you also edit only_five.py to accept more info.
class Movie(object):
	def __init__(self, title, poster_image_url, trailer_youtube_url, 
	description):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.description = description

# Creating variables for the films, as well as assigning the relevant data. 
# Additional films can be added here.
highlander_1 = Movie("Highlander", "http://i.imgur.com/EULiNeP.jpg", 
"https://www.youtube.com/watch?v=omOZyLmNMJs", "I can't be 100 percent certain"
", but I think this is one of the films in the Highlander series.")
highlander_2 = Movie("Highlander II: The Quickening", 
"http://i.imgur.com/WbS0V5E.jpg", "https://www.youtube.com/watch?v=YsgJltP__UA"
, "The Quickeningest film I've ever seen. It was over before I even knew it.")
highlander_3 = Movie("Highlander III: The Sorcerer", 
"http://i.imgur.com/oolFckA.jpg", "https://www.youtube.com/watch?v=eW_HzYMNOng"
, 'This movie is commonly referred to by its better-known title, '
'"Sleepless in Seattle"')
highlander_4 = Movie("Highlander: Endgame", "http://i.imgur.com/u32XwEE.jpg", 
"https://www.youtube.com/watch?v=6Xfx0RKvA5s", "At long last, the respected "
"Highlander film franchise completes its journey with this, the final film in "
"the series.")
highlander_5 = Movie("Highlander: The Source", 
"http://i.imgur.com/FOjpOO5.jpg", "https://www.youtube.com/watch?v=RQJeTwNFSSc"
, "I'm pretty sure this isn't a real film. Do you remember it coming out? I "
"don't.")		
# Putting all of the films in a list to be sent to the only_five function. 
# Any additional films need to be added to this list.
fav_films = [highlander_1, highlander_2, highlander_3, highlander_4,
 highlander_5]

# This calls the only_five function to create the webpage.
# Do not change.
open_movies_page(fav_films)