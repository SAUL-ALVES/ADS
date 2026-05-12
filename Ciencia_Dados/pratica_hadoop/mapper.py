import sys


for line in sys.stdin:
    parts = line.strip().split('\t')
    if len(parts) >= 3:
        movie_id = parts[1]
        rating = parts[2]
        print("{}\t{}".format(movie_id, rating))
