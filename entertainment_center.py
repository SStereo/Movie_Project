import fresh_tomatoes
import media

# Create 6 different movie objects 
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZXre34PxgTc")

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interstellar = media.Movie("Interstellar","A father rescures humanity during a space mission",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=FByEFOAQeU0")

matrix = media.Movie("Matrix", "Neo saves the world",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

gladiator = media.Movie("Gladiator","A soldier fights to free rome",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Gladiator_ver1.jpg/220px-Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")

sunshine = media.Movie("Sunshine","A space crew saves our sun",
                       "https://upload.wikimedia.org/wikipedia/en/thumb/6/68/Sunshine_poster.jpg/220px-Sunshine_poster.jpg",
                       "https://www.youtube.com/watch?v=veC25b8Vd2E")

# The movie object references are stored in a list
movies = [toy_story, avatar, interstellar, matrix, gladiator, sunshine]

# The list of movie object is passed to the fresh tomatoe module
# to generate an HTML file with the content of the movie objects
fresh_tomatoes.open_movies_page(movies)
