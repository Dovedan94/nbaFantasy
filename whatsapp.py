import pywhatkit
from time import localtime, strftime
import pandas as pd
import dataframe_image as dfi

from enums import ALL_PLAYERS_PTS_LOGS
from google_sheets_api import (
    get_tabela_data,
    write_all_pts_logs,
)


def send_tabela_data_via_whatsapp():

    write_all_pts_logs(ALL_PLAYERS_PTS_LOGS)

    all_data = get_tabela_data()

    df_cols = ["POZICIJA", "", "POENI", "RAZLIKA"]
    df = pd.DataFrame(columns=df_cols, data=all_data)
    df.to_csv("novi.csv", sep=",", encoding="utf-8", index=False)
    df_new = pd.read_csv("novi.csv", index_col=1)

    dfi.export(df_new, "tabela.png")
    current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    pywhatkit.sendwhats_image(
        "+381631076732",
        "tabela.png",
        caption=f"tabela ažurirana: {current_time}",
        wait_time=25,
    )


send_tabela_data_via_whatsapp()
# write_all_pts_logs(ALL_PLAYERS_PTS_LOGS)
