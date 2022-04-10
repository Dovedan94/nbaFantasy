from pprint import pprint
from time import strftime, localtime
from typing import Dict, List

from google.oauth2 import service_account
from googleapiclient.discovery import build

from main import get_game_logs_data

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "google_api_key.json"

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

SPREADSHEET_ID = "1pQtzP5BM6P0Xib83FM7s32qCHdh2ZaQB6k_tk13pEJ4"
RANGE_NAME = "!B4:K150"
service = build("sheets", "v4", credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


# Function creates sheets for all fantasy players
def create_sheets_for_all_fantasy_players(all_rosters: List[Dict]):
    for roster in all_rosters:
        fantasy_player_name = list(roster.keys())
        body = {
            "requests": [
                {
                    "addSheet": {
                        "properties": {
                            "title": f"{fantasy_player_name[0]}",
                        }
                    }
                }
            ]
        }

        service.spreadsheets().batchUpdate(
            spreadsheetId=SPREADSHEET_ID, body=body
        ).execute()


# Function writes total points for a specified fantasy player roster
def write_a_single_pts_logs(fantasy_player_roster: Dict):
    roster = get_game_logs_data(fantasy_player_roster)

    sheet_name = list(fantasy_player_roster.keys())[0]
    new_range = sheet_name + RANGE_NAME
    value_input_option = "USER_ENTERED"

    value_range_body = {
        "majorDimension": "COLUMNS",
        "values": roster,
    }

    request = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=new_range,
            valueInputOption=value_input_option,
            body=value_range_body,
        )
    )
    response = request.execute()
    pprint(response)


# Function takes all rosters dict and writes points in the appropriate sheets
def write_all_pts_logs(all_rosters: Dict):
    for player in all_rosters:
        write_a_single_pts_logs(player)


# Function gets current table standings e.g Sheet1!A1:H15
def get_tabela_data(table_location: str) -> List[List]:
    sheet_range = table_location
    request = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, majorDimension="ROWS", range=sheet_range)
    )
    response = request.execute()

    all_data = response.get("values", [])

    return all_data


# Function writes 'updated at' time, in specified cell e.g. Sheet1!A1
def updated_at(cell_location: str):
    current_time = [strftime("%d-%m-%Y %H:%M:%S", localtime())]
    value_range_body = {
        "majorDimension": "COLUMNS",
        "values": [current_time],
    }
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=cell_location,
        valueInputOption="RAW",
        body=value_range_body,
    ).execute()
