import pytest
from scrape_boardgamegeek import get_bgg_page, print_top50_boardgames_from_boardgamegeek

expected_lines = """[game(name='Gloomhaven', bgg_rating=8.564, year=2017),
 game(name='Pandemic Legacy: Season 1', bgg_rating=8.468, year=2015),
 game(name='Brass: Birmingham', bgg_rating=8.322, year=2018),
 game(name='Terraforming Mars', bgg_rating=8.283, year=2016),
 game(name='Twilight Imperium (Fourth Edition)', bgg_rating=8.224, year=2017),
 game(name='Through the Ages: A New Story of Civilization', bgg_rating=8.206, year=2015),
 game(name='Star Wars: Rebellion', bgg_rating=8.162, year=2016),
 game(name='Gaia Project', bgg_rating=8.161, year=2017),
 game(name='Twilight Struggle', bgg_rating=8.144, year=2005),
 game(name='Great Western Trail', bgg_rating=8.112, year=2016),
 game(name='Scythe', bgg_rating=8.088, year=2016),
 game(name='War of the Ring: Second Edition', bgg_rating=8.084, year=2012),
 game(name='Spirit Island', bgg_rating=8.064, year=2017),
 game(name='The Castles of Burgundy', bgg_rating=8.013, year=2011),
 game(name='Terra Mystica', bgg_rating=8.001, year=2012),
 game(name='7 Wonders Duel', bgg_rating=7.975, year=2015),
 game(name='Concordia', bgg_rating=7.961, year=2013),
 game(name='Brass: Lancashire', bgg_rating=7.952, year=2007),
 game(name='Arkham Horror: The Card Game', bgg_rating=7.93, year=2016),
 game(name='Wingspan', bgg_rating=7.925, year=2019),
 game(name='Viticulture Essential Edition', bgg_rating=7.914, year=2015),
 game(name='A Feast for Odin', bgg_rating=7.911, year=2016),
 game(name='Orléans', bgg_rating=7.887, year=2014),
 game(name='Mage Knight Board Game', bgg_rating=7.885, year=2011),
 game(name='Puerto Rico', bgg_rating=7.879, year=2002),
 game(name='The 7th Continent', bgg_rating=7.875, year=2017),
 game(name='Caverna: The Cave Farmers', bgg_rating=7.859, year=2013),
 game(name='Food Chain Magnate', bgg_rating=7.859, year=2015),
 game(name='Agricola', bgg_rating=7.845, year=2007),
 game(name='Nemesis', bgg_rating=7.842, year=2018),
 game(name='Root', bgg_rating=7.835, year=2018),
 game(name='Mansions of Madness: Second Edition', bgg_rating=7.825, year=2016),
 game(name='Blood Rage', bgg_rating=7.821, year=2015),
 game(name='Pandemic Legacy: Season 2', bgg_rating=7.82, year=2017),
 game(name='Kingdom Death: Monster', bgg_rating=7.79, year=2015),
 game(name='Power Grid', bgg_rating=7.765, year=2004),
 game(name='Everdell', bgg_rating=7.764, year=2018),
 game(name="Tzolk'in: The Mayan Calendar", bgg_rating=7.759, year=2012),
 game(name='Mechs vs. Minions', bgg_rating=7.755, year=2016),
 game(name='Star Wars: Imperial Assault', bgg_rating=7.754, year=2014),
 game(name='Clans of Caledonia', bgg_rating=7.737, year=2017),
 game(name='Through the Ages: A Story of Civilization', bgg_rating=7.735, year=2006),
 game(name='Le Havre', bgg_rating=7.722, year=2008),
 game(name='Eclipse', bgg_rating=7.72, year=2011),
 game(name='Azul', bgg_rating=7.717, year=2017),
 game(name='Gloomhaven: Jaws of the Lion', bgg_rating=7.712, year=2020),
 game(name='Anachrony', bgg_rating=7.697, year=2017),
 game(name='The Voyages of Marco Polo', bgg_rating=7.692, year=2015),
 game(name='Robinson Crusoe: Adventures on the Cursed Island', bgg_rating=7.685, year=2012),
 game(name='Maracaibo', bgg_rating=7.683, year=2019)]""".split('\n')


@pytest.fixture
def preload_bgg_site():
    with open('boardgamegeek.html') as file:
        bgg = file.read()
    return bgg


def test_valid_output(capfd, preload_bgg_site):
    print_top50_boardgames_from_boardgamegeek(preload_bgg_site)
    out, _ = capfd.readouterr()
    for line in expected_lines:
        assert line in out, f'"{line}" should be in output of top50 boardgames'
