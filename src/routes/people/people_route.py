from flask import Blueprint, request, jsonify
from models.people.people_model import People
from models import db

people_bp = Blueprint('people1',__name__)

@people_bp.route("/", methods=["GET"])
def get_people():
    list_people = People.query.all()
    list_people = [people.serialize() for people in list_people] 
    return jsonify({"list_people":list_people})

@people_bp.route("/<int:people_id>", methods = ["GET"]) 
def get_people_by_id(people_id):
        people = People.query.get(people_id)
        return jsonify({"people":people.serialize()})

@people_bp.route('/create',methods=['POST'])
def create_people():
    people_data = request.get_json()
    new_people = People(**people_data)
    db.session.add(new_people)
    db.session.commit()
    print(new_people)
    return "Persona creada",200