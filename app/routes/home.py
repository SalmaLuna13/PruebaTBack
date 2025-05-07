from flask import Blueprint, jsonify

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Bienvenido a la API de Tamákas Explor.'})
