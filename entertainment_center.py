import media
import fresh_tomatoes
# -*- coding: utf-8 -*-

movies = []
#Toy Story
toy_story = media.Movie('Toy Story', 60,
						'A story of a boy and his toys that come to life', 
						'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 
						'https://www.youtube.com/watch?v=vwyZH85NQC4')
						
movies.append(toy_story)
#Avatar
avatar = media.Movie('Avatar', 60,
					 'A marine on an alien planet', 
					 'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg', 
					 'https://www.youtube.com/watch?v=5PSNL1qE6VY')

movies.append(avatar)

#Pride & Prejudice (1995)
pride_and_prejudice = media.Movie('Pride & Prejudice', 360,
					 "Jane Austen's classic novel about the prejudice that occurred between the 19th century classes and the pride which would keep lovers apart.", 
					 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU1MDY4OTU5OF5BMl5BanBnXkFtZTcwOTg5NzAyMw@@._V1_.jpg', 
					 'https://www.youtube.com/watch?v=P5MmcT_vcBU')

movies.append(pride_and_prejudice)

#Ladyhawke
ladyhawke = media.Movie('Ladyhawke', 60,
					 "CURSED FOR ETERNITY...No force in Heaven will release them. No power on Earth can save them.", 
					 'https://images-na.ssl-images-amazon.com/images/M/MV5BYmYyNzBjNGUtOGYwZi00ZTVjLWE5YzYtZTcyMjFiMDExYmVkXkEyXkFqcGdeQXVyNjU0MTA3NzQ@._V1_SY1000_CR0,0,713,1000_AL_.jpg', 
					 'https://www.youtube.com/watch?v=iGs4o_5jyhw')

movies.append(ladyhawke)

#Drei Haselnuesse
drei_haselnuesse = media.Movie('Drei Haselnuesse fuer Aschenputtel', 60,
					 "Life changes dramatically for a Czech housemaid when the house driver gives her three magical hazel nuts.", 
					 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzMzg2Njc3NV5BMl5BanBnXkFtZTcwOTA1MTEzMQ@@._V1_.jpg', 
					 'https://www.youtube.com/watch?v=bptf3Zlqlgo')

movies.append(drei_haselnuesse)

#Secondhand Lions
secondhand = media.Movie('Secondhand Lions', 60,
					 "A coming-of-age story about a shy, young boy sent by his irresponsible mother to spend the summer with his wealthy, eccentric uncles in Texas.", 
					 'https://upload.wikimedia.org/wikipedia/en/6/6a/SecondhandLions.jpg', 
					 'https://www.youtube.com/watch?v=Ebkrm7u44UI')

movies.append(secondhand)

#fresh_tomatoes.open_movies_page(movies)
print (secondhand.show_info())
#print (media.Movie.__bases__)
