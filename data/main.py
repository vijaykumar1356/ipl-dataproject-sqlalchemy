import csv
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
# importing the engine and the table classes from schema
from schema import engine, Delivery, Match, Umpire


def add_csv_to_db(session):
    """
    function to add 3 csv files data into iplproject database in
    separate tables
    """
    with open('deliveries.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            delivery = Delivery(match_id=row['match_id'], inning=row['inning'],
                                batting_team=row['batting_team'],
                                bowling_team=row['bowling_team'],
                                over=row['over'], ball=row['ball'],
                                batsman=row['batsman'],
                                non_striker=row['non_striker'],
                                bowler=row['bowler'],
                                batsman_runs=row['batsman_runs'],
                                total_runs=row['total_runs'])
            session.add(delivery)

    with open('matches.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            match = Match(**row)
            session.add(match)

    with open('umpires_nation.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            umpire = Umpire(**row)
            session.add(umpire)

    # commit changes to db through db engine
    session.commit()


def question1(session):
    """
    this function extracts from database, data of all teams and their total
    runs from all seasons played and creates a json object of that data
    """
    qry = session.query(Delivery.batting_team, func.sum(Delivery.total_runs))\
        .group_by(Delivery.batting_team)\
        .order_by(func.sum(Delivery.total_runs).desc()).all()
    teams_runs = dict(qry)
    json_obj = {
        "teams": list(teams_runs.keys()),
        "total_runs": list(teams_runs.values())
    }
    with open('teams_scores.json', 'w') as f:
        json.dump(json_obj, f, indent=2)


def question2(session):
    """
    this function extracts from database Top 15 RCB batsman and their total
    runs scored for team from all seasons played in IPL
    """
    data = session.query(Delivery.batsman, func.sum(Delivery.batsman_runs))\
        .filter(Delivery.batting_team == 'Royal Challengers Bangalore')\
        .group_by(Delivery.batsman)\
        .order_by(func.sum(Delivery.batsman_runs).desc()).limit(15).all()

    rcb_batsmen_scores = dict(data)
    json_obj = {
        "batsmen": list(rcb_batsmen_scores.keys())[:15],
        "total_score": list(rcb_batsmen_scores.values())[:15],
        }
    with open("rcb_batsmen_runs.json", 'w') as f:
        json.dump(json_obj, f, indent=2)


def question3(session):
    """
    this function extracts from database all umpires and their nationality who
    are of not Indian region and creates a Json object of country and number
    of umpires represented from that country.
    """

    data = session.query(Umpire.nationality, func.count(Umpire.umpire))\
        .filter(Umpire.nationality != 'India').group_by(Umpire.nationality)\
        .order_by(func.count(Umpire.umpire).desc()).all()
    country_umpires = dict(data)
    json_obj = {
        "countries": list(country_umpires.keys()),
        "no_of_umpires": list(country_umpires.values())
    }
    with open('./country_umpire_count.json', 'w') as f:
        json.dump(json_obj, f, indent=2)


def question4(session):
    """
    This function extracts the number of matches played by each unique team in
    IPL separated by season wise and creates a json object of all unique teams
    and a list consist of the number of matches played by team season wise.
    """
    seasons = session.query(Match.season).distinct()\
        .order_by(Match.season).all()
    seasons = [i[0] for i in seasons]
    teams = session.query(Match.team1).distinct()\
        .order_by(Match.team1).all()
    # unique teams from all seasons ordered alphabetically
    unique_teams = [i[0] for i in teams]

    team1 = session.query(Match.season, Match.team1, func.count(Match.team1))\
        .group_by(Match.season, Match.team1)\
        .order_by(Match.season, Match.team1).all()
    team2 = session.query(Match.season, Match.team2, func.count(Match.team2))\
        .group_by(Match.season, Match.team2)\
        .order_by(Match.season, Match.team2).all()
    season_data = {}

    # Initializing a mega dictionary of seasons as keys and all unique teams
    # nested in a dictionary as a values for each season.
    # Each team in that nested dictionary will be initialized
    #  with a default value of zero.
    for season in seasons:
        season_data.setdefault(season, {})
        for team in unique_teams:
            season_data[season].setdefault(team, 0)
    for team in team1:
        season_data[team[0]][team[1]] += team[2]
    for team in team2:
        season_data[team[0]][team[1]] += team[2]

    # creating data for plotting on html page using hightcharts library
    season_wise_matches = []
    for key in season_data:
        season_wise_matches.append((list(season_data[key].values())))
    # creating json object
    json_obj = {
        "teams": unique_teams,
        "seasonData": season_wise_matches
    }
    with open('./all_seasons.json', 'w') as file:
        json.dump(json_obj, file, indent=1)


if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    # creating a new session
    session = Session()
    add_csv_to_db(session)
    question1(session)
    question2(session)
    question3(session)
    question4(session)

    # closing session
    session.close()
