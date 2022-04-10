from typing import List, Dict

import requests
from bs4 import BeautifulSoup


# DOWNLOADS NBA PLAYERS GAME LOGS FOR A SINGLE FANTASY PLAYER
def get_game_logs_data(fantasy_player: Dict) -> List:
    all_data = []
    for players in list(fantasy_player.values())[0]:
        nba_player_points = [f"{players[0]}"]
        game_log_link = f"https://www.basketball-reference.com/players/{players[1][0]}/{players[1]}/gamelog/2022"
        print(game_log_link)
        page = requests.get(game_log_link)
        soup = BeautifulSoup(page.content, "html.parser")
        # FINDS ALL ROWS IN THE TABLE
        regular_season_points_table = soup.find("table", id="pgl_basic").find_all("tr")

        for column in regular_season_points_table[1::]:
            if column.find("td") is not None:
                if column.find_all("td")[0].text != "":
                    nba_player_points.append(column.find_all("td")[26].text)
                else:
                    nba_player_points.append("0")

        all_data.append(nba_player_points)

    return all_data


# DOWNLOADS NBA PLAYERS GAME LOGS FOR ALL FANTASY PLAYERS
def get_all_game_logs_data(all_rosters: list) -> List:
    all_data = []

    for roster in all_rosters:
        all_data.append(get_game_logs_data(roster))

    return all_data
