from pprint import pprint
from typing import Dict, List

import requests
from bs4 import BeautifulSoup



# Function scrapes NBA teams pages and gets all players total points in
# specified season
def get_all_points_by_team_and_season(
    team_abbreviation: List[str], season: str
) -> List[Dict]:
    all_data = []

    for abb in team_abbreviation:

        helper_dict = {}

        link = f"https://www.basketball-reference.com/teams/{abb}/{season}.html"
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "html.parser")

        totals_table = soup.find("table", id="totals")
        players_column = totals_table.find_all("td", class_="left")
        points_column = totals_table.find_all("tr")

        players = []
        for player in players_column[:-1]:
            players.append(player.get_text())

        points = []
        for point in points_column[1:-1]:
            points.append(point.find_all("td")[-1].get_text())

        helper_dict[abb] = list(zip(players, points))
        pprint(helper_dict)

        all_data.append(helper_dict)
    return all_data
