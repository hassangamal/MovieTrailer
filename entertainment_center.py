import fresh_tomatoes
import media
import json
movies = []
# read movies from json file and store it in movies array
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['movies']:
        title = p['title']
        storyline = p['storyline']
        image_url = p['poster_image_url']
        youtube_url = p['trailer_youtube_url']
        year = p['year']
        movie = media.Movie(title, storyline, image_url, youtube_url, year)
        movies.append(movie)
# to show all moives in browser
fresh_tomatoes.open_movies_page(movies)
