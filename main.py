import requests
from bs4 import BeautifulSoup

from enums import LINK

page = requests.get(LINK)
soup = BeautifulSoup(page.content, "html.parser")

totals_table = soup.find("table", id="totals")

players_column = totals_table.find_all("td", class_="left")
points_column = totals_table.find_all("tr")

points = []
for point in points_column[1:-1]:
    points.append(point.find_all("td")[-1].get_text())

players = []
for player in players_column[:-1]:
    players.append(player.get_text())
