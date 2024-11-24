from flask import Blueprint, jsonify, request
from app.models import db, Area, Team, Player, Competition, Match
from datetime import datetime

api_bp = Blueprint('api', __name__)

# Route to get all areas
@api_bp.route('/api/areas', methods=['GET'])
def get_areas():
    areas = Area.query.all()
    return jsonify([{
        'id': area.id,
        'name': area.name,
        'city': area.city,
        'country': area.country,
        'capacity': area.capacity
    } for area in areas])

# Route to get all teams
@api_bp.route('/api/teams', methods=['GET'])
def get_teams():
    teams = Team.query.all()
    return jsonify([{
        'id': team.id,
        'name': team.name,
        'country': team.country,
        'founded': team.founded,
        'home_area': team.home_area.name
    } for team in teams])

# Route to get players of a specific team
@api_bp.route('/api/teams/<int:team_id>/players', methods=['GET'])
def get_team_players(team_id):
    players = Player.query.filter_by(team_id=team_id).all()
    return jsonify([{
        'id': player.id,
        'name': player.name,
        'position': player.position,
        'age': player.age,
        'nationality': player.nationality
    } for player in players])

# Route to get all players
@api_bp.route('/api/players', methods=['GET'])
def get_players():
    players = Player.query.all()
    return jsonify([{
        'id': player.id,
        'name': player.name,
        'position': player.position,
        'age': player.age,
        'nationality': player.nationality,
        'team': player.team.name
    } for player in players])

# Route to get all matches
@api_bp.route('/api/matches', methods=['GET'])
def get_matches():
    # Filter parameters
    team_id = request.args.get('team_id', type=int)
    area_id = request.args.get('area_id', type=int)
    date_from = request.args.get('date_from', type=str)
    date_to = request.args.get('date_to', type=str)
    
    query = Match.query
    
    if team_id:
        query = query.filter((Match.home_team_id == team_id) | (Match.away_team_id == team_id))
    if area_id:
        query = query.filter_by(area_id=area_id)
    if date_from:
        query = query.filter(Match.date >= datetime.strptime(date_from, '%Y-%m-%d').date())
    if date_to:
        query = query.filter(Match.date <= datetime.strptime(date_to, '%Y-%m-%d').date())
    
    matches = query.all()
    return jsonify([{
        'id': match.id,
        'competition': match.competition.name,
        'home_team': match.home_team.name,
        'away_team': match.away_team.name,
        'date': match.date.strftime('%Y-%m-%d'),
        'area': match.area.name,
        'home_score': match.home_score,
        'away_score': match.away_score,
        'status': match.status
    } for match in matches])

# Route to get all competitions
@api_bp.route('/api/competitions', methods=['GET'])
def get_competitions():
    competitions = Competition.query.all()
    return jsonify([{
        'id': comp.id,
        'name': comp.name,
        'country': comp.country,
        'type': comp.type
    } for comp in competitions])

# Route to get upcoming matches
@api_bp.route('/api/matches/upcoming', methods=['GET'])
def get_upcoming_matches():
    today = datetime.now().date()
    matches = Match.query.filter(
        Match.date >= today,
        Match.status == 'Scheduled'
    ).order_by(Match.date).limit(5).all()
    
    return jsonify([{
        'id': match.id,
        'competition': match.competition.name,
        'home_team': match.home_team.name,
        'away_team': match.away_team.name,
        'date': match.date.strftime('%Y-%m-%d'),
        'area': match.area.name
    } for match in matches])