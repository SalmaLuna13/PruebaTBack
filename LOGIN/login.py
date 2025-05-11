from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["https://salmaluna13.github.io"]) 

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sotelo@localhost/TamakásExplor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

    # Middleware para configurar CORS (se ejecuta después de cada solicitud)
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://salmaluna13.github.io'  # Origen permitido
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'  # Métodos permitidos
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'  # Encabezados permitidos
    return response

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Bienvenido a la API de inicio de sesión.'})

# Ruta para iniciar sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    name = data.get('name')
    password = data.get('password')

    # Buscar al usuario en la base de datos
    user = User.query.filter_by(name=name).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Usuario o contraseña incorrectos.'}), 401

    return jsonify({'message': f'Bienvenido, {user.name}'}), 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)