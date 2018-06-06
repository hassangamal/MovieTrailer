import fresh_tomatoes
import media
import json
movies = []
# read movies from json file and store it in movies array
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['movies']:
        moive=media.Movie(p['title'], p['storyline'],p['poster_image_url'],p['trailer_youtube_url'],p['year'])
        movies.append(moive)
# to show all moives in browser
fresh_tomatoes.open_movies_page(movies)