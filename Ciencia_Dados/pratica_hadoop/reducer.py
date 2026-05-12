import sys


movie_names = {}
try:
    with open('ml-100k/u.item', 'r', encoding='latin-1') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) > 1:
                movie_names[parts[0]] = parts[1]
except Exception as e:
    pass

current_movie = None
ratings = []


for line in sys.stdin:
    line = line.strip()
    try:
        movie_id, rating = line.split('\t', 1)
        rating = float(rating)
    except ValueError:
        continue

    
    if current_movie == movie_id:
        ratings.append(rating)
    else:
        if current_movie:
            raw_title = movie_names.get(current_movie, "Desconhecido")
            
            title = raw_title.encode('ascii', 'ignore').decode('ascii')
            
            avg_rating = sum(ratings) / len(ratings)
            max_rating = max(ratings)
            total_votes = len(ratings)
            print("{}\tMedia: {:.2f} | Nota Max: {} | Votos: {}".format(title, avg_rating, max_rating, total_votes))
        
        current_movie = movie_id
        ratings = [rating]


if current_movie:
    raw_title = movie_names.get(current_movie, "Desconhecido")
    title = raw_title.encode('ascii', 'ignore').decode('ascii')
    avg_rating = sum(ratings) / len(ratings)
    max_rating = max(ratings)
    total_votes = len(ratings)
    print("{}\tMedia: {:.2f} | Nota Max: {} | Votos: {}".format(title, avg_rating, max_rating, total_votes))
