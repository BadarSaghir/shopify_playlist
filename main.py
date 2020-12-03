import datetime
import requests
from bs4 import BeautifulSoup


# 59h9kpbPLrbWRk7
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def make_soup():
    date = input("Where you want to travel in time? Enter Date input this format YYYY-MM-DD\n")
    if validate(date):
        response = requests.get('https://www.billboard.com/charts/hot-100/' + date)
        soup = BeautifulSoup(response.text, 'html.parser')
        rank = [rank.get_text() for rank in soup.findAll(class_="chart-element__rank__number")]
        song_name = [rank.get_text() for rank in soup.findAll(class_="chart-element__information__song")]
        artists = [artist.get_text() for artist in soup.find_all(class_="chart-element__information__artist")]
        popular_songs = []

        with open("movies.txt", 'w') as file:
            for (r, s, artist) in zip(rank, song_name, artists):
                popular_songs.append(r + " " + s + " by " + "artist")
                file.writelines(r + " " + s  + " by "+artist+"\n")

        print(popular_songs[0] + " ")

    else:
        print('Sorry Incorrect Date time format. Kindly provide the valid Time')
        make_soup()


make_soup()
