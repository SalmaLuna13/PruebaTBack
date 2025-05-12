from flask import Flask, request, jsonify, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields
from flask_cors import CORS  # Importar CORS
from app.models import registro, Usuarios, reseña, Favoritos, Niveles
from app.Schemas.schemas_reseña import ReseñaSchema
from marshmallow import ValidationError
from app import db

bp = Blueprint('auth', __name__)

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://salmaluna13.github.io"}}, methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])  # Configurar CORS para permitir solicitudes desde el origen del frontend


@bp.route('/api/saludo')
def saludo():
    return jsonify({"mensaje": "Hola desde Flask!"})




@bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        return jsonify({'message': 'Método GET no implementado para esta ruta.'}), 405

    data = request.json
    usuario = data.get('usuario')
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    # Datos del modelo Usuarios
    nombre = data.get('nombre')
    apellido_p = data.get('apellido_p')
    apellido_m = data.get('apellido_m')
    ciudad = data.get('ciudad')
    estado = data.get('estado')

    # Verificar si el usuario o correo ya existen
    if registro.query.filter((registro.correo == correo) | (registro.usuario == usuario)).first():
        return jsonify({'message': 'El usuario o correo ya están registrados.'}), 400

    # Crear nuevo registro con contraseña encriptada
    hashed_password = generate_password_hash(contraseña, method='pbkdf2:sha256')
    nuevo_registro = registro(usuario=usuario, correo=correo, contraseña=hashed_password)
    db.session.add(nuevo_registro)
    db.session.commit()  # Necesario para obtener el id_registro generado
    return jsonify({'message': 'Usuario registrado exitosamente.'}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')

    # Buscar al usuario en la base de datos
    registro_usuario = registro.query.filter_by(usuario=usuario).first()
    if not registro_usuario or not check_password_hash(registro_usuario.contraseña, contraseña):
        return jsonify({'message': 'Usuario o contraseña incorrectos.'}), 401

    return jsonify({'message': f'Bienvenido, {registro_usuario.usuario}'}), 200


@bp.route('/reseñas', methods=['POST'])
def agregar_reseña():
    data = request.json

    reseña_schema = ReseñaSchema()

    try:
        datos_validados = reseña_schema.load(data)
    except ValidationError as err:
        return jsonify({'error': ' Datos inválidos', 'mensajes': err.messages}), 400

    try:
        nueva_reseña = reseña(
            id_informacion=data['id_informacion'],
            id_usuarios=data['id_usuarios'],
            cali=data['cali'],
            comentarios=data['comentarios'],
            URL_Foto=data['URL_Foto']
        )

        db.session.add(nueva_reseña)
        db.session.commit()

        return jsonify({'message': '✅ Reseña agregada con éxito', 'id_reseña': nueva_reseña.id_reseña}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al gucdardar la reseña: {str(e)}'}), 500
    
    
@bp.route('/favoritos', methods=['POST'])
def agregar_favorito():
    data = request.get_json()
    id_usuario = data.get('id_usuario')
    id_informacion = data.get('id_informacion')

    if not id_usuario or not id_informacion:
        return jsonify({'error': 'Faltan campodadasdss obligatorios'}), 400

    try:
        favorito = Favoritos.query.filter_by(id_usuario=id_usuario, id_informacion=id_informacion).first()

        if favorito:
            # Si ya existe, actualiza el estado
            favorito.estado = True
        else:
            favorito = Favoritos(
                id_usuario=id_usuario,
                id_informacion=id_informacion,
                estado=True
            )
            db.session.add(favorito)

        db.session.commit()
        return jsonify({'message': '✅ Agregado a favoritos', 'id_favorito': favorito.id_favoritos}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al agregar favorito: {str(e)}'}), 500


# Eliminar (desactivar) de favoritos
@bp.route('/favoritos', methods=['DELETE'])
def eliminar_favorito():
    data = request.get_json()
    id_usuario = data.get('id_usuario')
    id_informacion = data.get('id_informacion')

    if not id_usuario or not id_informacion:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    try:
        favorito = Favoritos.query.filter_by(id_usuario=id_usuario, id_informacion=id_informacion).first()

        if not favorito:
            return jsonify({'message': ' No se encontró el favorito'}), 404

        favorito.estado = False
        db.session.commit()
        return jsonify({'message': ' Favorito eliminado'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Error al eliminar favorito: {str(e)}'}), 500


@bp.route('/nivel', methods=['GET'])
def obtener_nivel():
    try:
        xp = int(request.args.get('xp', 0))
        nivel = get_level_by_xp(xp)
        return jsonify({"xp": xp, "nivel": nivel})
    except ValueError:
        return jsonify({"error": "XP debe ser un número entero"}), 400
    
    
# Tabla de experiencia mínima por nivel
levels = {
    1: 100,
    2: 600,
    3: 1200
}

def get_level_by_xp(xp):
    level = 0
    for lvl, min_xp in sorted(levels.items()):
        if xp >= min_xp:
            level = lvl
        else:
            break
    return level