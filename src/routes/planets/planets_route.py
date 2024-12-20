from flask import Blueprint, request, jsonify
from models.planets.planets_model import Planets
from models import db

planets_bp = Blueprint('planets1',__name__)

@planets_bp.route("/", methods=["GET"])
def get_planets():
    list_planets = Planets.query.all()
    list_planets = [planets.serialize() for planets in list_planets]  
    return jsonify({"list_planets":list_planets})

@planets_bp.route("/<int:planets_id>", methods = ["GET"]) 
def get_planets_by_id(planets_id):
        planets = Planets.query.get(planets_id)
        return jsonify({"planets":planets.serialize()})

@planets_bp.route('/create',methods=['POST'])
def create_planets():
    planets_data = request.get_json()
    new_planets = Planets(**planets_data)
    db.session.add(new_planets)
    db.session.commit()
    print(new_planets)
    return "Planeta creado",200