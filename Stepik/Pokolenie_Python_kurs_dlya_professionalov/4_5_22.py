
from zipfile import ZipFile
import json


def is_correct_json(string: str) -> bool:
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


if __name__ == '__main__':
    players = []
    with ZipFile('data.zip') as zip_file:
        datas = zip_file.infolist()
        for data in datas:
            with zip_file.open(data.filename) as file:
                try:
                    text = file.read().decode(encoding='utf-8')
                    if is_correct_json(text):
                        player = json.loads(text)
                        players.append(player)
                except UnicodeDecodeError:
                    continue
    arsenal_players = sorted([player for player in players if player['team'] == 'Arsenal'], key=lambda x: (x['first_name'], x['last_name']))
    for player in arsenal_players:
        print(player['first_name'], player['last_name'])
