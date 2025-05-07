from flask import Blueprint, request, jsonify
from ..models import Usuarios
from .. import db

bp = Blueprint('usuarios', __name__)

@bp.route('/', methods=['POST'])
def usuarios():
    if not request.is_json:
        return jsonify({'error': 'El encabezado Content-Type debe ser application/json.'}), 415

    data = request.json
    id_registro = data.get('id_registro')
    nombre = data.get('nombre')
    apellido_p = data.get('apellido_p')
    apellido_m = data.get('apellido_m')
    ciudad = data.get('ciudad')
    estado = data.get('estado')

    if not all([id_registro, nombre, apellido_p, apellido_m, ciudad, estado]):
        return jsonify({'error': 'Faltan datos obligatorios.'}), 400

    nuevo_usuario = Usuarios(
        id_registro=id_registro,
        nombre=nombre,
        apellido_p=apellido_p,
        apellido_m=apellido_m,
        ciudad=ciudad,
        estado=estado
    )
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado exitosamente.'}), 201


@bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuarios.query.all()
    usuarios_json = [
        {
            "id_registro": usuario.id_registro,
            "nombre": usuario.nombre,
            "apellido_p": usuario.apellido_p,
            "apellido_m": usuario.apellido_m,
            "ciudad": usuario.ciudad,
            "estado": usuario.estado
        } for usuario in usuarios
    ]
    return jsonify(usuarios_json), 200


