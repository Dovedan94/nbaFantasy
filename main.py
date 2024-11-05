from time import sleep

from enums import MAINSHEET

from basketball_reference import Player, get_all_nba_injuries
from google_sheets import GoogleSheets


def get_data(participant_rosters: list[list]) -> list:
    """
    Function takes a list of lists (list of basketball reference links), obtained from participant rosters from Google
    Sheets.
    :param participant_rosters:
    :return: List of NBA players points.
    """

    all_data = []
    for roster in participant_rosters:
        data = [roster[0]]
        for nba_player in roster[1:]:
            player = Player(nba_player, "2025")
            sleep(3)
            data.append(player.get_all_player_data())
        all_data.append(data)

    return all_data


def run_all(spreadsheet_link: str, year: str):
    g_sheets = GoogleSheets(spreadsheet_link)
    for data in get_data(g_sheets.read_sheet("START!A2:K12")):
        g_sheets.update_single_sheet(data)
    g_sheets.write_injury_report(get_all_nba_injuries(year))
    g_sheets.updated_at()
    return


run_all(MAINSHEET, "2025")
