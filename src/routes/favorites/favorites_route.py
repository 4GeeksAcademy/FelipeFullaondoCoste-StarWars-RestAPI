from flask import Blueprint, request, jsonify
from models.user.user_model import User
from models.people.people_model import People
from models.planets.planets_model import Planets
from models.favorites.favorites_model import Favorites
from models import db

favorites_bp = Blueprint('favorites1',__name__)

@favorites_bp.route("/", methods=["GET"])
def get_planets():
    list_favorites = Favorites.query.all()
    list_favorites = [favorites.serialize() for favorites in list_favorites]  
    return jsonify({"list_favorites":list_favorites})

@favorites_bp.route('/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    person = People.query.get(people_id)
    if not user or not person:
        return jsonify({'error': 'User or Person not found'}), 404
    favorites = Favorites(user_id=user.id, people_id=person.id, is_active=True)
    db.session.add(favorites)
    db.session.commit()
    return jsonify({'message': 'Persona agregada a favoritos'})

@favorites_bp.route('/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    planet = Planets.query.get(planet_id)
    if not user or not planet:
        return jsonify({'error': 'User or Planet not found'}), 404
    favorites = Favorites(user_id=user.id, planet_id=planet.id, is_active=True)
    db.session.add(favorites)
    db.session.commit()
    return jsonify({'message': 'Planeta agregado a favoritos'})

@favorites_bp.route('/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_person(people_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    person = People.query.get(people_id)
    if not user or not person:
        return jsonify({'error': 'User or Person not found'}), 404
    favorites = Favorites(user_id=user.id, people_id=person.id)
    db.session.delete(favorites)
    db.session.commit()
    return jsonify({'message': 'Persona eliminada de favoritos'})

@favorites_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    planet = Planets.query.get(planet_id)
    if not user or not planet:
        return jsonify({'error': 'User or Planet not found'}), 404
    favorites = Favorites(user_id=user.id, planet_id=planet.id)
    db.session.delete(favorites)
    db.session.commit()
    return jsonify({'message': 'Planeta eliminada a favoritos'})