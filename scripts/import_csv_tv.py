import csv
from movieuniverse.models import TVShow

def process_number(integer):
    if integer == '':
        return 0.0
    elif '%' in integer:
        return float(integer.replace('%', ''))
    else:
        return float(integer)

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