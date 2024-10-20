from flask import Blueprint, request, jsonify
from .models import init_db  # Asegúrate de llamar a init_db

api_routes = Blueprint('api', __name__)

@api_routes.route('/items', methods=['GET'])
def get_items():
    # Implementa la lógica para obtener todos los elementos
    return jsonify({"items": []})

@api_routes.route('/items', methods=['POST'])
def create_item():
    # Implementa la lógica para crear un nuevo elemento
    return jsonify({"message": "Item created"}), 201
