import csv
from movieuniverse.models import TVShow
from .import_csv import process_number

with open('files/movies.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = TVShow.objects.get_or_create(
                title = row[1],
                year = row[2],
                age = row[3],
                IMDb_rating = process_number(row[4]),
                Rotten_Tomatoes_rating = int(process_number(row[5])),
                netflix = int(row[6]),
                hulu = int(row[7]),
                prime = int(row[8]),
                disney = int(row[9]),
            )