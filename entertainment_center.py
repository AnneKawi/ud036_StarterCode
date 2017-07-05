import media
import fresh_tomatoes

# Build the Movie Instances and collect them in a list
movies = []

# Mask of Zorro
zorro = media.Movie(
                    'The Mask of Zorro',
                    "A young thief, seeking revenge for the "
                    "death of his brother, "
                    "is trained by the once great, but aged Zorro, "
                    "who also pursues vengeance of his own.",
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BNjI3NzI2MjY2MF5BMl5BanBnXkFtZTYwMDM5ODU5._V1_.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=FzrhTLNorF0'
                    )
movies.append(zorro)

# Much Ado About Nothing
much_ado = media.Movie(
                    'Much Ado about nothing',
                    'Young lovers Hero and Claudio, soon to wed, '
                    'conspire to get verbal sparring partners and '
                    'confirmed singles Benedick and Beatrice to wed as well.',
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q3YTU4OTgtZTc0My00YmY1LWJmOTQtMmMwNGE2ZjBmNmIxXkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=wGlmhwa0zjw'
                    )
movies.append(much_ado)

# Taxi
taxi = media.Movie(
                    'Taxi',
                    "To work off his tarnished driving record, "
                    "a hip taxi driver must chauffeur a loser "
                    "police inspector on the trail of German bank robbers.",
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BMmViOGVjZWQtZmNmNS00MWU3LWFjNGEtMDc1MjNlY2ZlNjdiXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,701,1000_AL_.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=8nANiVnDJOo'
                    )
movies.append(taxi)

# Ladyhawke
ladyhawke = media.Movie(
                    'Ladyhawke',
                    "CURSED FOR ETERNITY..."
                    "No force in Heaven will release them. "
                    "No power on Earth can save them.",
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BYmYyNzBjNGUtOGYwZi00ZTVjLWE5YzYtZTcyMjFiMDExYmVkXkEyXkFqcGdeQXVyNjU0MTA3NzQ@._V1_SY1000_CR0,0,713,1000_AL_.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=iGs4o_5jyhw'
                    )
movies.append(ladyhawke)

# Black Beauty
black_beauty = media.Movie(
                    'Black Beauty',
                    'A story for all ages. A Friendship for all time. '
                    'Share the adventure.',
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwNTc3NzI4NF5BMl5BanBnXkFtZTcwOTk3MDcyMQ@@._V1_.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=-qCPMP4mNcQ'
                    )
movies.append(black_beauty)

# Secondhand Lions
secondhand = media.Movie('Secondhand Lions',
                     "A coming-of-age story about a shy, "
                     "young boy sent by his irresponsible mother to spend "
                     "the summer with his wealthy, eccentric uncles in Texas.",
                     'https://upload.wikimedia.org/wikipedia/en/6/6a/SecondhandLions.jpg',  # NOQA
                     'https://www.youtube.com/watch?v=Ebkrm7u44UI')

movies.append(secondhand)


# Hand the Movie-List to the Fresh Tomatos-Open_movies_page-funtion
# (aka build and open the Webpage)
fresh_tomatoes.open_movies_page(movies)
