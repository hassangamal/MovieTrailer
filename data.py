import json
# to store all movies in json file
data = {}
data['movies'] = []
data['movies'].append({
    'title': 'Contact',
    'storyline': 'We make contact with aliens',
    'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=d9C2cF3KvP8',
    'year': '1997'
})
data['movies'].append({
    'title': 'Toy Story',
    'storyline': 'A story of a boy and his toys that come to life.',
    'poster_image_url': 'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=vwyZH85NQC4',
    'year': '1921'
})
data['movies'].append({
    'title': 'Moses',
    'storyline': 'The story of how God delivered Israel from 400 years slavery.',
    'poster_image_url': 'http://upload.wikimedia.org/wikipedia/en/d/d1/10Command56.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=OqCTq3EeDcY',
    'year': '2001'
})
data['movies'].append({
    'title': 'Above the Rim',
    'storyline': 'A promising New York City high school basketball star and his relationships with two people.',
    'poster_image_url': 'http://upload.wikimedia.org/wikipedia/en/b/b6/Above_the_rim_poster.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=sEsCXWD7-Cc',
    'year': '1987'
})
data['movies'].append({
    'title': 'The Matrix',
    'storyline': 'The world is a simulation.',
    'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
    'trailer_youtube_url': 'https://www.youtube.com/watch?v=vKQi3bBA1y8',
    'year': '1999'
})


# to write movies in json file
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)