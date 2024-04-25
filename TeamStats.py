import requests
import numpy as np
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats


headers  = {
    "data_sets": {
        "LeagueDashTeamStats": [
            "TEAM_ID",
            "TEAM_NAME",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS"
        ]
    },
    "endpoint": "LeagueDashTeamStats",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameScope",
        "GameSegment",
        "LeagueID",
        "Location",
        "Outcome",
        "PORound",
        "PlayerExperience",
        "PlayerPosition",
        "SeasonSegment",
        "ShotClockRange",
        "StarterBench",
        "TeamID",
        "TwoWay",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "Conference": "((East)|(West))?",
        "DateFrom": None,
        "DateTo": None,
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "GameScope": "((Yesterday)|(Last 10))?",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": None,
        "LeagueID": None,
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
        "Month": None,
        "OpponentTeamID": None,
        "Outcome": "^((W)|(L))?$",
        "PORound": None,
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": None,
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": None,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
        "StarterBench": "((Starters)|(Bench))?",
        "TeamID": None,
        "TwoWay": None,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameScope",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlayerExperience",
        "PlayerPosition",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "StarterBench",
        "TeamID",
        "TwoWay",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "LastNGames",
        "Location",
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}

#nba_teams = teams.get_teams()
#df = pd.DataFrame(nba_teams)
#print(df)

#season = '22019'
#team_stats = leaguedashteamstats.LeagueDashTeamStats(season = season, headers = headers, timeout = 100)
#team_stats_df = team_stats.get_data_frames()
#print(team_stats_df)
#team_stats_df.head()

#atl_team_id = '1610612737'

#team_stats = leaguedashteamstats.LeagueDashTeamStats(season = '22019')
team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612737')

#team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id_nullable = '1610612737', per_mode_detailed = 'Per48')

#df = team_stats.get_data_frames()[0]
df = team_stats.league_dash_team_stats.get_data_frame()

#df = pd.DataFrame(index=np.arange(5), columns=np.arange(30))

pd.set_option('max_columns', None)


#df = team_stats.get_data_frames()[0]
#print(df)

print(df)

