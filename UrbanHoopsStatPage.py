from flask import Flask
import requests
import pandas as pd
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.endpoints import leaguedashplayerstats


app = Flask(__name__)

@app.route("/Hawks")
def Hawks():
    
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612737')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612737')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Celtics")
def Celtics():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612738')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612738')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Cavaliers")
def Cavaliers():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612739')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612739')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Pelicans")
def Pelicans():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612740')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612740')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Bulls")
def Bulls():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612741')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612741')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Mavericks")
def Mavericks():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612742')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612742')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Nuggets")
def Nuggets():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612743')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612743')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Warriors")
def Warriors():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612744')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612744')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Rockets")
def Rockets():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612745')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612745')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Clippers")
def Clippers():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612746')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612746')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Lakers")
def Lakers():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612747')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612747')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Heat")
def Heat():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612748')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612748')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Bucks")
def Bucks():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612749')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612749')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Timberwolves")
def Timberwolves():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612750')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612750')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Nets")
def Nets():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612751')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612751')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Knicks")
def Knicks():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612752')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612752')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Magic")
def Magic():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612753')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612753')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Pacers")
def Pacers():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612754')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612754')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/76ers")
def SeventySixers():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612755')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612755')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Suns")
def Suns():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612756')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612756')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Blazers")
def Blazers():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612757')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612757')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Kings")
def Kings():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612758')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612758')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Spurs")
def Spurs():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612759')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612759')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Thunder")
def Thunder():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612760')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612760')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)

@app.route("/Raptors")
def Raptors():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612761')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612761')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Jazz")
def Jazz():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612762')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612762')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Grizzlies")
def Grizzlies():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612763')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612763')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)

@app.route("/Wizards")
def Wizards():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612764')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612764')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Pistons")
def Pistons():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612765')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612765')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


@app.route("/Hornets")
def Hornets():

    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(team_id_nullable = '1610612766')
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612766')
    dt = team_stats.league_dash_team_stats.get_data_frame()
    dp = player_stats.league_dash_player_stats.get_data_frame()
    pd.set_option('max_columns', None)
    dtDf = pd.DataFrame(dt)
    dtDf = dtDf.drop(columns = ["GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "CFID","CFPARAMS"])
    dtTable = dtDf.to_html(classes="table table-striped")
    dpDf = pd.DataFrame(dp)
    dpDf = dpDf.drop(columns = ["NICKNAME", "WNBA_FANTASY_PTS", "GP_RANK", "W_RANK", "L_RANK", "W_PCT_RANK", "MIN_RANK", "FGM_RANK", "FGA_RANK", "FG_PCT_RANK", "FG3M_RANK", "FG3A_RANK", "FG3_PCT_RANK", "FTM_RANK", "FTA_RANK", "FT_PCT_RANK", "OREB_RANK", "DREB_RANK", "REB_RANK", "AST_RANK", "TOV_RANK", "STL_RANK", "BLK_RANK", "BLKA_RANK", "PF_RANK", "PFD_RANK", "PTS_RANK", "PLUS_MINUS_RANK", "NBA_FANTASY_PTS_RANK", "DD2_RANK", "TD3_RANK", "WNBA_FANTASY_PTS_RANK", "CFID", "CFPARAMS"])
    dpTable = dpDf.to_html(classes="table table-striped")
    
    return str(dtTable) + "_" + str(dpTable)


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=5000)
