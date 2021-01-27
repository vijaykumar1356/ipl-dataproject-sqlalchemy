from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Delivery(Base):
    """
    Creating Delivery table schema
    creating a class Delivery which points to table deliveries, each time an
    instance of Delivery is created or triggered to extract data from DB
    """
    __tablename__ = 'deliveries'
    id = Column(Integer, primary_key=True)
    match_id = Column('match_id', Integer)
    inning = Column('inning', Integer)
    batting_team = Column('batting_team', String(60))
    bowling_team = Column('bowling_team', String(60))
    over = Column('over', Integer)
    ball = Column('ball', Integer)
    batsman = Column('batsman', String(50))
    non_striker = Column('non_striker', String(50))
    bowler = Column('bowler', String(50))
    batsman_runs = Column('batsman_runs', Integer)
    total_runs = Column('total_runs', Integer)

    def __repr__(self):
        return f"<Delivery(match_id={self.match_id}, inning={self.inning},\
        batting_team={self.batting_team}, bowling_team={self.bowling_team},\
        over={self.over}, ball={self.ball}, batsman={self.batsman},\
        not_striker={self.non_striker}, bowler={self.bowler},\
        batsman_runs={self.batsman_runs}, total_runs={self.total_runs}\
        )>"


class Match(Base):
    """
    Creating 'matches' table schema
    Match class points to matches table and and instance of this class is
    considered by sqlalchemy as a row of table 'matches' in database.
    """
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True)
    season = Column(Integer)
    city = Column(String(30))
    date = Column(String(30))
    team1 = Column(String(50))
    team2 = Column(String(50))
    toss_winner = Column(String(50))
    toss_decision = Column(String(20))
    result = Column(String(30))
    dl_applied = Column(Integer)
    winner = Column(String(50))
    win_by_runs = Column(Integer)
    win_by_wickets = Column(Integer)
    player_of_match = Column(String(50))
    venue = Column(String(70))
    umpire1 = Column(String(50))
    umpire2 = Column(String(50))
    umpire3 = Column(String(50))

    def __repr__(self):
        return f"<Match(id={self.id}, season={self.season}, city={self.city},\
            date={self.date}, team1={self.team1}, team2={self.team2},\
            toss_winner={self.toss_winner},\
            toss_decision={self.toss_decision},\
            result={self.result}, dl_applied={self.dl_applied},\
            winner={self.winner}, win_by_runs={self.win_by_runs},\
            win_by_wickets={self.win_by_wickets},\
            player_of_match={self.player_of_match}, venue={self.venue},\
            umpire1={self.umpire1}, umpire2={self.umpire2},\
            umpire3={self.umpire3})>"


class Umpire(Base):
    """
    Creating 'umpires' table schema
    The Umpire class is regarded as a table by sqlalchemy and each instace of
    this class points to row of that table
    """
    __tablename__ = 'umpires'
    id = Column(Integer, primary_key=True)
    umpire = Column(String(60))
    nationality = Column(String(50))

    def __repr__(self):
        return f"<Umpire(id={self.id}, umpire={self.umpire},\
            nationality={self.nationality})>"


# engine URL
engine_url = "postgresql://iplproject:ipl@localhost:5432/iplproject"

# creating an engine which interacts with postgres on localhost
engine = create_engine(engine_url, echo=False)

# generate database schema
Base.metadata.create_all(engine)
