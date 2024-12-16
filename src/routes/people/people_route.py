from flask import Blueprint, request, jsonify
from models.people.people_model import People
from models import db, People
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required

people_bp = Blueprint('people1',__name__)
bcrypt = Bcrypt()

@people_bp.route("/", methods=["GET"])
def get_people():
    list_people = People.query.all()
    list_people = [people.serialize() for people in list_people] 
    return jsonify({"list_people":list_people})

@people_bp.route("/<int:people_id>", methods = ["GET"]) 
def get_character(people_id):
        person = People.query.get(people_id)
        return jsonify({"person":person.serialize()})

@people_bp.route('/create',methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_people = People(**user_data)
    db.session.add(new_people)
    new_people.password = bcrypt.generate_password_hash(new_people.password).decode('utf-8')
    print(new_people.password)
    db.session.commit()
    print(new_people)
    return "Persona creada",200