import csv

all_movies = []

with open('shared_articles.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked = []
not_liked = []
did_not_watch = []