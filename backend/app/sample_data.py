import sqlalchemy
from app import db
from app.models import Team, Player, Competition, Match, Area
import random
from datetime import datetime, timedelta

# Define the sample data for teams, players, etc.
POSITIONS = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']
AREAS = [
    {'id': 1, 'name': 'Old Trafford', 'city': 'Manchester', 'country': 'England', 'capacity': 74140},
    {'id': 2, 'name': 'Camp Nou', 'city': 'Barcelona', 'country': 'Spain', 'capacity': 99354},
    {'id': 3, 'name': 'Santiago Bernabeu', 'city': 'Madrid', 'country': 'Spain', 'capacity': 81044},
    {'id': 4, 'name': 'Allianz Arena', 'city': 'Munich', 'country': 'Germany', 'capacity': 75024},
    {'id': 5, 'name': 'Anfield', 'city': 'Liverpool', 'country': 'England', 'capacity': 53394},
]

PLAYERS = [
    {'id': 1, 'name': 'David De Gea', 'position': 'Goalkeeper', 'age': 32, 'nationality': 'Spain', 'team_id': 1},
    {'id': 2, 'name': 'Harry Maguire', 'position': 'Defender', 'age': 30, 'nationality': 'England', 'team_id': 1},
    {'id': 3, 'name': 'Bruno Fernandes', 'position': 'Midfielder', 'age': 28, 'nationality': 'Portugal', 'team_id': 1},
    {'id': 4, 'name': 'Marcus Rashford', 'position': 'Forward', 'age': 25, 'nationality': 'England', 'team_id': 1},
    {'id': 5, 'name': 'Marc-André ter Stegen', 'position': 'Goalkeeper', 'age': 31, 'nationality': 'Germany', 'team_id': 2},
    {'id': 6, 'name': 'Ronald Araujo', 'position': 'Defender', 'age': 24, 'nationality': 'Uruguay', 'team_id': 2},
    {'id': 7, 'name': 'Pedri', 'position': 'Midfielder', 'age': 20, 'nationality': 'Spain', 'team_id': 2},
    {'id': 8, 'name': 'Robert Lewandowski', 'position': 'Forward', 'age': 34, 'nationality': 'Poland', 'team_id': 2},
    {'id': 9, 'name': 'Thibaut Courtois', 'position': 'Goalkeeper', 'age': 31, 'nationality': 'Belgium', 'team_id': 3},
    {'id': 10, 'name': 'David Alaba', 'position': 'Defender', 'age': 31, 'nationality': 'Austria', 'team_id': 3},
    {'id': 11, 'name': 'Luka Modric', 'position': 'Midfielder', 'age': 37, 'nationality': 'Croatia', 'team_id': 3},
    {'id': 12, 'name': 'Vinicius Jr', 'position': 'Forward', 'age': 23, 'nationality': 'Brazil', 'team_id': 3},
    {'id': 13, 'name': 'Manuel Neuer', 'position': 'Goalkeeper', 'age': 37, 'nationality': 'Germany', 'team_id': 4},
    {'id': 14, 'name': 'Matthijs de Ligt', 'position': 'Defender', 'age': 23, 'nationality': 'Netherlands', 'team_id': 4},
    {'id': 15, 'name': 'Joshua Kimmich', 'position': 'Midfielder', 'age': 28, 'nationality': 'Germany', 'team_id': 4},
    {'id': 16, 'name': 'Harry Kane', 'position': 'Forward', 'age': 30, 'nationality': 'England', 'team_id': 4},
    {'id': 17, 'name': 'Alisson', 'position': 'Goalkeeper', 'age': 30, 'nationality': 'Brazil', 'team_id': 5},
    {'id': 18, 'name': 'Virgil van Dijk', 'position': 'Defender', 'age': 32, 'nationality': 'Netherlands', 'team_id': 5},
    {'id': 19, 'name': 'Mohamed Salah', 'position': 'Forward', 'age': 31, 'nationality': 'Egypt', 'team_id': 5},
    {'id': 20, 'name': 'Darwin Núñez', 'position': 'Forward', 'age': 24, 'nationality': 'Uruguay', 'team_id': 5},
]

TEAMS = [
    {'id': 1, 'name': 'Manchester United', 'country': 'England', 'founded': 1878, 'home_area_id': 1},
    {'id': 2, 'name': 'Barcelona', 'country': 'Spain', 'founded': 1899, 'home_area_id': 2},
    {'id': 3, 'name': 'Real Madrid', 'country': 'Spain', 'founded': 1902, 'home_area_id': 3},
    {'id': 4, 'name': 'Bayern Munich', 'country': 'Germany', 'founded': 1900, 'home_area_id': 4},
    {'id': 5, 'name': 'Liverpool', 'country': 'England', 'founded': 1892, 'home_area_id': 5},
]

COMPETITIONS = [
    {'id': 1, 'name': 'UEFA Champions League', 'country': 'Europe', 'type': 'Club'},
    {'id': 2, 'name': 'Premier League', 'country': 'England', 'type': 'Club'},
    {'id': 3, 'name': 'La Liga', 'country': 'Spain', 'type': 'Club'},
    {'id': 4, 'name': 'Bundesliga', 'country': 'Germany', 'type': 'Club'},
    {'id': 5, 'name': 'Serie A', 'country': 'Italy', 'type': 'Club'},
    {'id': 6, 'name': 'Ligue 1', 'country': 'France', 'type': 'Club'},
    {'id': 7, 'name': 'Copa del Rey', 'country': 'Spain', 'type': 'Club'},
    {'id': 8, 'name': 'DFB-Pokal', 'country': 'Germany', 'type': 'Club'},
    {'id': 9, 'name': 'FIFA World Cup', 'country': 'World', 'type': 'International'},
    {'id': 10, 'name': 'UEFA European Championship', 'country': 'Europe', 'type': 'International'},
]

def generate_match_date():
    """Generates a random date in the next 7 days."""
    return datetime.now() + timedelta(days=random.randint(0, 7))

def generate_random_score():
    """Generates a random match score (between 0 and 5 goals for both teams)."""
    return random.randint(0, 5), random.randint(0, 5)

def init_db():
    # Add Areas (Stadiums)
    for area in AREAS:
        existing_area = Area.query.get(area['id'])
        if not existing_area:
            new_area = Area(**area)
            db.session.add(new_area)

    # Add Teams
    for team in TEAMS:
        existing_team = Team.query.get(team['id'])
        if not existing_team:
            new_team = Team(**team)
            db.session.add(new_team)

    # Add Players
    for player in PLAYERS:
        existing_player = Player.query.get(player['id'])
        if not existing_player:
            new_player = Player(**player)
            db.session.add(new_player)

    # Add Competitions
    for competition in COMPETITIONS:
        existing_competition = Competition.query.get(competition['id'])
        if not existing_competition:
            new_competition = Competition(**competition)
            db.session.add(new_competition)

    # Generate Matches (3 matches per day)
    match_id = 1
    for day in range(1, 8):  # Generate matches for the next 7 days
        match_date = generate_match_date()
        for _ in range(3):  # 3 matches per day
            # Randomly choose two teams from different countries
            home_team = random.choice(TEAMS)
            away_team = random.choice([team for team in TEAMS if team['country'] != home_team['country']])

            # Select a random competition and area (stadium)
            competition = random.choice(COMPETITIONS)
            area = random.choice(AREAS)

            # Generate a random score
            home_score, away_score = generate_random_score()

            # Create a match object
            new_match = Match(
                id=match_id,
                competition_id=competition['id'],
                home_team_id=home_team['id'],
                away_team_id=away_team['id'],
                area_id=area['id'],
                date=match_date,
                home_score=home_score,
                away_score=away_score,
                status='Scheduled'
            )
            db.session.add(new_match)
            match_id += 1  # Increment match ID to keep it unique

    # Commit all additions to the database
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        db.session.rollback()
        print(f"Integrity error: {e}")

