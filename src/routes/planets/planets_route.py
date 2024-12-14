from flask import Blueprint, request, jsonify
from models import db, Planets


planet_bp = Blueprint('planets',__name__)

@planet_bp.route('/get',methods=['GET'])
def get_planet_list():
    return "Lista de planetas: ",200

@planet_bp.route('/get/<int:planet_id>',methods=['GET'])
def get_ser(planet_id):
    return "Planeta .... encontrado",200
