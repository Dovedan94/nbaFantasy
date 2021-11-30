from pprint import pprint

import requests
from bs4 import BeautifulSoup


# GETS ALL NBA PLAYERS POINTS THIS SEASON
from enums import ALL_ROSTERS, ALL_PLAYERS_PTS_LOGS


def get_all_points_by_team(teams_abbreviations):
    all_data = []

    for abb in teams_abbreviations:

        helper_dict = {}

        link = f"https://www.basketball-reference.com/teams/{abb}/2022.html"
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


def get_single_fantasy_player_total_points(team_players_dict):
    roster_totals = []

    for teams_players in team_players_dict.values():

        for team_player in teams_players:
            link = (
                f"https://www.basketball-reference.com/teams/{team_player[0]}/2022.html"
            )
            print(link)
            page = requests.get(link).text
            soup = BeautifulSoup(page, "html.parser")

            totals_table = soup.find("table", id="totals")
            exact_player_pts = totals_table.find_all(
                "tr"
            )  # finds all rows in totals table

            for row in exact_player_pts[1:-1]:  # ignore tables header and footer rows
                if row.find("a").text == f"{team_player[1]}":
                    print(f"{team_player[1]}", row.find_all("td")[-1].text)
                    roster_totals.append((team_player[1], row.find_all("td")[-1].text))

    return roster_totals


def get_all_fantasy_player_total_points(all_rosters):
    all_data = []
    for player in all_rosters:
        all_data.append(get_single_fantasy_player_total_points(player))
        print(player)
    return all_data


# DOWNLOADS NBA PLAYERS GAME LOGS FOR A SINGLE FANTASY PLAYER
def get_game_logs_data(single_fantasy_player_list):
    all_data = []
    for players in list(single_fantasy_player_list.values())[0]:
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
def get_all_game_logs_data(all_fantasy_player_list):
    all_data = []

    for players in all_fantasy_player_list:
        all_data.append(get_game_logs_data(players))

    return all_data
