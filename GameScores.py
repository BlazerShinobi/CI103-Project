from flask import Flask, render_template
import requests
import numpy as np
import pandas as pd
from tabulate import tabulate
from datetime import datetime, timezone
from dateutil import parser
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.live.nba.endpoints import scoreboard

app = Flask(__name__)

@app.route("/scoreBoard")
def scoreBoard():
    f = "{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}"
    final = ""

    board = scoreboard.ScoreBoard()
    print("ScoreBoardDate: " + board.score_board_date)
    games = board.games.get_dict()
    gamesList = []
    for game in games:
        gameTimeLTZ = parser.parse(game["gameTimeUTC"]).replace(tzinfo=timezone.utc).astimezone(tz=None)
        gamesList.append((f.format(gameId=game['gameId'], awayTeam=game['awayTeam']['teamName'], homeTeam=game['homeTeam']['teamName'], gameTimeLTZ=gameTimeLTZ)))
    for item in gamesList:
        out = str(item)
        final = out + "\n" + final 
    return str(final)

@app.route("/Hawks")
def Hawks():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612737')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Celtics")
def Celtics():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612738')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Cavaliers")
def Cavaliers():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612739')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Pelicans")
def Pelicans():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612740')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Bulls")
def Bulls():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612741')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Mavericks")
def Mavericks():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612742')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Nuggets")
def Nuggets():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612743')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Warriors")
def Warriors():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612744')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Rockets")
def Rockets():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612745')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Clippers")
def Clippers():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612746')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Lakers")
def Lakers():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612747')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Heat")
def Heat():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612748')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Bucks")
def Bucks():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612749')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Timberwolves")
def Timberwolves():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612750')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Nets")
def Nets():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612751')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Knicks")
def Knicks():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612752')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Magic")
def Magic():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612753')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Pacers")
def Pacers():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612754')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)


@app.route("/76ers")
def SeventySixers():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612755')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Suns")
def Suns():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612756')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Blazers")
def Blazers():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612757')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Kings")
def Kings():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612758')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Spurs")
def Spurs():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612759')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Thunder")
def Thunder():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612760')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Raptors")
def Raptors():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612761')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Jazz")
def Jazz():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612762')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Grizzlies")
def Grizzlies():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612763')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Wizards")
def Wizards():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612764')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Pistons")
def Pistons():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612765')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

@app.route("/Hornets")
def Hornets():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable='1610612766')
    games = gamefinder.get_data_frames()[0]
    games_2122 = games[games.SEASON_ID.str[-4:] == '2021']
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(games_2122)
    dtTable = dtDf.to_html(classes="table table-striped")
    return str(dtTable)

    
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=7000)