import urllib.request
from time import sleep

from bs4 import BeautifulSoup, Comment

from enums import TEAM_ABBS


class Player:

    def __init__(self, link: str, year: str) -> None:
        self.link = link
        self.year = year
        self.html = urllib.request.urlopen(self._create_game_logs_link())
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.all_player_data = []

    def _create_game_logs_link(self) -> str:
        return self.link.removesuffix(".html") + f"/gamelog/{self.year}"

    def get_team(self) -> str:
        games_div = self.soup.find(id="div_pgl_basic").findAll(
            "td", {"data-stat": "team_id"}
        )
        return games_div[-1].getText()

    def get_image(self) -> str:
        meta_div = self.soup.find("div", id="meta")
        if meta_div and meta_div.find("div", class_="nothumb"):
            return "NO PHOTO AVAILABLE"
        else:
            return self.soup.find(attrs={"itemscope": "image"}).get("src").strip()

    def get_name(self) -> str:
        return (
            self.soup.find("h1")
            .getText()
            .strip()
            .removesuffix(f"{int(self.year) - 1}-{self.year[-2:]} Game Log")
            .strip()
        )

    def get_points(self) -> list:
        points = []
        table_div = self.soup.find(id="div_pgl_basic")

        for row in table_div.find_all("tr")[1:]:
            columns = row.find_all("td")
            if not columns:
                continue
            elif len(columns) == 29:
                points.append((columns[26]).getText())
            else:
                points.append(columns[7].getText())

        return points

    def get_all_player_data(self) -> list:
        self.all_player_data.append(self.get_team())
        self.all_player_data.append(self.get_name())
        self.all_player_data.append(self.get_image())
        for point in self.get_points():
            self.all_player_data.append(point)

        return self.all_player_data


class Team:

    def __init__(self, team_abb: str, year: str) -> None:
        self.team = team_abb
        self.year = year
        self.link = f"https://www.basketball-reference.com/teams/{team_abb}/{year}.html"
        self.html = urllib.request.urlopen(self.link)
        self.soup = BeautifulSoup(self.html, "html.parser")

    def get_roster(self) -> list:
        roster_table = (
            self.soup.find("table", {"id": "roster"})
            .find("tbody")
            .find_all("td", {"data-stat": "player"})
        )
        roster = []
        for player in roster_table:
            roster.append(player.get_text().removesuffix("(TW)").strip())
        roster = sorted(roster)
        roster.insert(0, self.team)

        return roster

    def get_injury_report(self) -> list:
        injuries_data = [self.team]
        no_injuries = self.soup.find_all("p")

        for p in no_injuries:
            if p.get_text() == "No current injuries to report.":
                injuries_data.append(["No current injuries to report."])
                return injuries_data

        injuries = self.soup.find(id="all_injuries")
        comments = [
            injury.extract()
            for injury in injuries(text=lambda text: isinstance(text, Comment))
        ]

        for comment in comments:
            comment_soup = BeautifulSoup(comment, "html.parser")
            rows = comment_soup.select("tbody tr")
            for row in rows:
                injury_data = []
                player = row.find("th", {"data-stat": "player"}).get_text(strip=True)
                date_update = row.find("td", {"data-stat": "date_update"}).get_text(
                    strip=True
                )
                note = row.find("td", {"data-stat": "note"}).get_text(strip=True)
                injury_data.append(player.strip())
                injury_data.append(date_update.strip())
                injury_data.append(note.strip())
                injuries_data.append(injury_data)

        return injuries_data


def get_all_nba_rosters(year: str, team_abbs: list = TEAM_ABBS) -> list:
    all_rosters = []
    for roster in team_abbs:
        team = Team(roster, year)
        all_rosters.append(team.get_roster())
        sleep(3.3)

    return all_rosters


def get_all_nba_injuries(year, team_abbs: list = TEAM_ABBS):
    all_injuries = []
    for roster in team_abbs:
        team = Team(roster, year)
        all_injuries.append(team.get_injury_report())
        sleep(3.3)

    return all_injuries
