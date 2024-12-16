from flask import Blueprint, request, jsonify
from models.planets.planets_model import Planets
from models import db, Planets
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required

planets_bp = Blueprint('planets1',__name__)
bcrypt = Bcrypt()

@planets_bp.route("/", methods=["GET"])
def get_planets():
    list_planets = Planets.query.all()
    list_planets = [planets.serialize() for planets in list_planets]  
    return jsonify({"list_planets":list_planets})

@planets_bp.route("/<int:planets_id>", methods = ["GET"]) 
def get_planet(planets_id):
        planet = Planets.query.get(planets_id)
        return jsonify({"planet":planet.serialize()})

@planets_bp.route('/create',methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_planet = Planets(**user_data)
    db.session.add(new_planet)
    new_planet.password = bcrypt.generate_password_hash(new_planet.password).decode('utf-8')
    print(new_planet.password)
    db.session.commit()
    print(new_planet)
    return "Planeta creado",200