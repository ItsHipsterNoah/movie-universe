import csv
import os
from movieuniverse.models import Movie

def process_number(integer) -> int:
    if integer == '':
        return 0.0
    elif '%' in integer:
        return float(integer.replace('%', ''))
    else:
        return integer

def trunc(string):
    if len(string) > 50:
        return string[:45] + "..."
    return string


with open('files/movies.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Movie.objects.get_or_create(
                title = trunc(row[2]),
                year = row[3],
                age = row[4],
                IMDb_rating = process_number(row[5]),
                Rotten_Tomatoes_rating = int(process_number(row[6])),
                netflix = int(row[7]),
                hulu = int(row[8]),
                prime = int(row[9]),
                disney = int(row[10]),
                directors = trunc(row[12].replace(',', ', ')),
                genres = trunc(row[13].replace(',', ', ')),
                country = row[14],
                language = trunc(row[15].replace(',', ', ')),
                runtime = int(process_number(row[16]))
            )
