from pprint import pprint

from google.oauth2 import service_account
from googleapiclient.discovery import build


from enums import ALL_ROSTERS
from main import get_single_fantasy_player_total_points, get_game_logs_data

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "google_api_key.json"

# promeni za dict posle
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

SPREADSHEET_ID = "1pQtzP5BM6P0Xib83FM7s32qCHdh2ZaQB6k_tk13pEJ4"
RANGE_NAME = "!B4:K150"
service = build("sheets", "v4", credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


# CREATE SHEETS FOR ALL FANTASY PLAYERS
def create_sheets_for_all_fantasy_players():
    for fantasy_player in ALL_ROSTERS:
        fantasy_player_name = list(fantasy_player.keys())
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


def write_total_points_to_a_specific_sheet(player_roster):
    roster = get_single_fantasy_player_total_points(player_roster)
    sheet_name = list(player_roster.keys())[0]
    new_range = sheet_name + RANGE_NAME
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=new_range,
        valueInputOption="USER_ENTERED",
        body={"values": roster},
    ).execute()


def write_total_points_to_all_sheets():
    for player_roster in ALL_ROSTERS:
        write_total_points_to_a_specific_sheet(player_roster)


def write_a_single_pts_logs(player_pts_logs):
    roster = get_game_logs_data(player_pts_logs)

    sheet_name = list(player_pts_logs.keys())[0]
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


def write_all_pts_logs(all_players_pts_logs):
    for player in all_players_pts_logs:
        print(player)
        write_a_single_pts_logs(player)


def get_tabela_data():

    sheet_range = "TABELA!E2:H17"
    request = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, majorDimension="ROWS", range=sheet_range)
    )
    response = request.execute()

    all_data = response.get("values", [])

    return all_data

