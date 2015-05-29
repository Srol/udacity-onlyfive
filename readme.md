***** There Can Be Only Five movie trailers
by Patrick Hogan (srol.hogan@gmail.com)

Contents:
I. Intro
II. Contents
III. How to run.
IV. Adding additional films.
V. Adding additional information.
VI. Credits

I. Intro

This script is used to create a website to display a list of movies, provide their titles, movie poster and YouTube trailer and a short bit of description by a critic. When run, the script generates an HTML file that can then be uploaded to a web server for display. 

II. Contents

media.py
only_five.py
readme.txt

When run properly, media.py will generate only_five.html 

III. How to run.

1. If you don't have it already, install Python 2.7.10 on your computer. It can be found at python.org.
2. Put all the provided files are in a directory together.
3. Open a terminal or command line window in that directory.
4. Type python media.py and hit enter.
5. only_five.html should now be in the directory as well. Simply upload this file to your web server of choice.
6. Celebrate.

IV. Adding additional films.

Additional films can be added simply by creating a variable, then appending them to the list in media.py. 
	1. Add a new line between lines 15 and 19 of media.py with the following format, being sure to include the quotation marks.
		YourVariable = Movie("Your Movie's Title", "URL of poster image", "URL of Youtube Trailer", "Short text description")
	2. Add the variable to the list on line 22 (which will be line 23 if you added a new line in step 1). 
	FavFilms = [Highlander1, Highlander2, Highlander3, Highlander4, Highlander5, YourVariable]
	3. Run the steps in How to Run again and the new only_five.html should include your additional films.

V. Adding additional information.

Adding additional information is more difficult, as the only_five.py file is only expecting certain attributes. I only recommend this for more advanced users. The following steps would need to happen in order to do this.
	1. For each piece of additional information, a new attribute needs to be added to the Movie object on line 6 of media.py. 
	2. All of the movie variables on lines 15 through 19 (or more if you followed the steps in Adding additional films) needed to be edited to include the additional information. 
	3. The function open_movies_page in only_five.py needs to be edited to accept the new information.
	4. The HTML and CSS in only_five.html needs to be edited so the information can be displayed on the page. 
	
VI. Credits

The only_five.py file was provided by Udacity as part of the Full Stack Web Developer nanodegree, originally under the file name fresh_tomatoes.py. It was minimally edited to more appropriately fit the theme. All other code was written by me, Patrick Hogan.