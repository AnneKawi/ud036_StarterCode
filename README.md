# Movie Trailer Website

This repository contains code for a simple website displaying the posters and playing the trailers of some of my favourite movies.

# Source
the main outside source-code is the fresh_tomatoes.py-file from ud036_StarterCode

# Usage
to see the website, download the repo and run entertainment_center.py

# Files description:
1. fresh_tomatoes.py: 
	when passed a movie list to the function open_movies_page(), 
	it builds the necessary html-file, opens a browser and displays the website

2. media.py:
	holds the definitions of the Video-class with the subclass Movie
	every Movie-instance needs to be passed the movie title, movie storyline, the url of a movie poster and the url of a trailer of the movie on youtube upon initialisation

3. entertainment_center.py:
	contains the list with some of my favourite movies, builds the Movie Instances with the appropriate information 
	and calls the open_movies_page()-function from fresh_tomatoes.py
	- feel free to add movies (always appending the Movie()-instances to the global movies-variable)
