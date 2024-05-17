import pandas as pd
import json

data = pd.read_csv("netflix_titles.tsv", encoding="utf-8", delimiter="\t")

info = data[["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR"]]
info.columns = ["title", "directors", "cast", "genres", "decade"]

info[["directors", "cast", "genres"]] = info[["directors", "cast", "genres"]].fillna("")

def rozdeleni(value):
    return [item.strip() for item in value.split(", ")] if value else []

info["directors"] = info["directors"].apply(rozdeleni)
info["cast"] = info["cast"].apply(rozdeleni)
info["genres"] = info["genres"].apply(rozdeleni)

def rok_na_dekadu(year):
    return year // 10 * 10

info["decade"] = info["decade"].apply(rok_na_dekadu)

info_list = info.to_dict(orient="records")

with open("hw02_output.json", "w", encoding="utf-8") as file:
    json.dump(info_list, file, indent=4, ensure_ascii=False)
