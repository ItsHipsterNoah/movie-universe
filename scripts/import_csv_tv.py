import csv
from movieuniverse.models import TVShow


with open('files/movies.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = TVShow.objects.get_or_create(
                title = row[1],
                year = row[2],
                age = row[3],
                IMDb_rating = row[4],
                Rotten_Tomatoes_rating = row[5],
                netflix = row[6],
                hulu = row[7],
                prime = row[8],
                disney = row[9],
            )