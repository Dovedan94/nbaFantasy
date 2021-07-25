import requests
from bs4 import BeautifulSoup

from enums import LINK

page = requests.get(LINK)
print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")

totals_table = soup.find("table", id="totals")
players_column = totals_table.find_all("td", class_="left")

players = []
for i in players_column[:-1]:
    players.append(i.get_text())
