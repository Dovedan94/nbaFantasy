from time import strftime, localtime
from typing import Optional, Union

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheets:

    def __init__(self, spreadsheet_id: str) -> None:
        self.spreadsheet_id = spreadsheet_id
        self.creds = service_account.Credentials.from_service_account_file(
            "google_api_key.json",
            scopes=["https://www.googleapis.com/auth/spreadsheets"],
        )
        self.service = build("sheets", "v4", credentials=self.creds).spreadsheets()

    # RUN THIS METHOD ONLY ONCE AT SEASON START
    def create_new_sheets_for_all_participants(self) -> Optional[HttpError]:
        try:
            for participant in self.read_sheet():
                body = {
                    "requests": [
                        {
                            "addSheet": {
                                "properties": {
                                    "title": f"{participant[0]}",
                                }
                            }
                        }
                    ]
                }

                self.service.batchUpdate(
                    spreadsheetId=self.spreadsheet_id, body=body
                ).execute()

        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def read_sheet(
        self, range_name: str = "START!A2:K100"
    ) -> Union[list[list], HttpError]:
        try:
            result = (
                self.service.values()
                .get(spreadsheetId=self.spreadsheet_id, range=range_name)
                .execute()
            )
            values = result.get("values", [])

            return values

        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def update_single_sheet(self, fetched_data: list[list]):
        all_data = []
        for item in fetched_data[1:]:
            data = []
            image = f'=IMAGE("{item[2]}";3)'
            data.append(item[0])
            data.append(item[1])
            data.append(image)
            for _ in item[3:]:
                data.append(_)
            all_data.append(data)

        body = {
            "majorDimension": "COLUMNS",
            "values": all_data,
        }
        request = (
            self.service.values().update(
                spreadsheetId=self.spreadsheet_id,
                range=f"{fetched_data[0]}!B3:P94",
                valueInputOption="USER_ENTERED",
                body=body,
            )
        ).execute()

        return request

    def write_injury_report(self, injuries: list[list]):
        all_data = []
        for team in injuries:
            all_data.append([team[0]])
            for injury in team[1:]:
                all_data[-1].extend(injury)

        body = {
            "majorDimension": "ROWS",
            "values": all_data,
        }
        request = (
            self.service.values().update(
                spreadsheetId=self.spreadsheet_id,
                range=f"POVREDE!A2:BZ350",
                valueInputOption="USER_ENTERED",
                body=body,
            )
        ).execute()

        return request

    def updated_at(self, cell_location: str = "TABELA!A2"):
        current_time = [strftime("%d-%m-%Y %H:%M:%S", localtime())]
        value_range_body = {
            "majorDimension": "COLUMNS",
            "values": [current_time],
        }
        request = (
            self.service.values()
            .update(
                spreadsheetId=self.spreadsheet_id,
                range=cell_location,
                valueInputOption="USER_ENTERED",
                body=value_range_body,
            )
            .execute()
        )

        return request
