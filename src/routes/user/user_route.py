from flask import Blueprint, request, jsonify
from models import db, User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required


user_bp = Blueprint('user1',__name__)
bcrypt = Bcrypt()

@user_bp.route('/create',methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_user = User(**user_data)
    db.session.add(new_user)
    new_user.password = bcrypt.generate_password_hash(new_user.password).decode('utf-8')
    print(new_user.password)
    db.session.commit()
    print(new_user)
    return "Usuario creado",200

@user_bp.route('/login',methods=['POST'])
def login():
    user_data = request.get_json()
    user = User.query.filter_by(email=user_data["email"]).first()
    if user and bcrypt.check_password_hash(user.password, user_data["password"]):
        access_token = create_access_token(identity=str(user.id))
        return jsonify({"msg": "Login corrector","access_token":access_token})
    else:
        return jsonify({"msg": "Email no registrado o datos incorrectos"})

@user_bp.route('/',methods=['GET'])
# @jwt_required()
def get_user_list():
    user_list = User.query.all()
    user_list = [user.serialize() for user in user_list]
    print(user_list)
    return jsonify({"user_list":user_list})

@user_bp.route('/<int:id>',methods=['GET'])
# @jwt_required()
def get_user(id):
    user = User.query.get(id)
    print(user)
    return jsonify({"user":user.serialize()})