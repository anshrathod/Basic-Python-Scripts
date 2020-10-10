from collections import namedtuple
from typing import List
import pprint
import requests
from bs4 import BeautifulSoup

URL = 'https://boardgamegeek.com/browse/boardgame'
Game = namedtuple('game', 'name, bgg_rating, year')



def get_bgg_page():
    page = requests.get(URL)
    page.raise_for_status()
    return page.text

# with open('boardgamegeek.html', 'w') as file:
#     file.write(get_bgg_page())


def print_top50_boardgames_from_boardgamegeek(content_bgg):
    """Print list of 50 games from boardgamegeek"""

    soup = BeautifulSoup(content_bgg, 'html.parser')
    collection = soup.find('div', id='maincontent')
    games = collection.find_all('tr', id='row_')

    list_of_games = []
    for num, game in enumerate(games[:50]):
        name_year = soup.find(
            'div', id=f'results_objectname{num + 1}'
        ).text.strip().split('\n')

        rating = game.find('td', class_='collection_bggrating').text.strip()
        list_of_games.append(
            Game(
                name=name_year[0],
                year=int(name_year[1][1:-1]),
                bgg_rating=float(rating))
        )
    pprint.pprint(list_of_games)


if __name__ == '__main__':
    print_top50_boardgames_from_boardgamegeek(get_bgg_page())

