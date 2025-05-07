from . import db
from sqlalchemy import Enum  # Importación necesaria para usar Enum

class Usuarios(db.Model):
    id_usuarios = db.Column(db.Integer, primary_key=True)
    id_registro = db.Column(db.Integer, db.ForeignKey('registro.id_registro'), nullable=False)  # Ajuste del nombre de la clave foránea
    nombre = db.Column(db.String(80), nullable=False)
    apellido_p = db.Column(db.String(80), nullable=False)
    apellido_m = db.Column(db.String(80), nullable=False)
    ciudad = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)

class Niveles(db.Model):
    id_nivel = db.Column(db.Integer, primary_key=True)
    id_usuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuarios'), nullable=False)  # Ajuste del nombre de la clave foránea
    nivel = db.Column(db.Integer, nullable=False)
    puntos = db.Column(db.Integer, nullable=False)

class Tipos_de_niveles(db.Model):
    __tablename__ = 'tipos_de_niveles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)

class registro(db.Model):
    id = db.Column(db.Integer, primary_key=True, name='id_registro')  # Ajuste del nombre de la columna
    usuario = db.Column(db.String(50), unique=True, nullable=False)  # Cambiar a 'usuario'
    correo = db.Column(db.String(50), unique=True, nullable=False)   # Cambiar a 'correo'
    contraseña = db.Column(db.String(255), unique=True, nullable=False)  # Cambiar a 'contraseña'

class informacion(db.Model):
    id_informacion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(80), nullable=False)
    direccion = db.Column(db.String(80), nullable=False)
    reseña = db.Column(db.String(300), nullable=False)
    redsocial = db.Column(db.String(80), nullable=False)
    sitio_web = db.Column(db.String(80), nullable=False)
    costo = db.Column(db.Double, nullable=False)
    Tipo = db.Column(db.Enum('Restaurantes', 'Hoteles', 'Productos_Artesanales', 'Lugar_Turistico', name='tipo_enum'), nullable=False)  # Ajuste de valores enumerados

class reseña(db.Model):
    id_reseña = db.Column(db.Integer, primary_key=True)
    id_informacion = db.Column(db.Integer, db.ForeignKey('informacion.id_informacion'), nullable=False)
    id_usuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuarios'), nullable=False)  # Ajuste del nombre de la clave foránea
    cali = db.Column(db.Integer, nullable=False)
    comentarios = db.Column(db.String(300), nullable=False)
    URL_Foto = db.Column(db.String(80), nullable=False)

class ruta(db.Model):
    id_Ruta = db.Column(db.Integer, primary_key=True)
    id_usuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuarios'), nullable=False)  # Ajuste del nombre de la clave foránea
    fecha = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.Boolean, nullable=False)

class detalles_ruta(db.Model):
    id_detalles = db.Column(db.Integer, primary_key=True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('ruta.id_Ruta'), nullable=False)
    id_informacion = db.Column(db.Integer, db.ForeignKey('informacion.id_informacion'), nullable=False)
    URL_Foto = db.Column(db.String(255), nullable=False)    

class Favoritos(db.Model):
    id_favoritos = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuarios'), nullable=False)
    id_informacion = db.Column(db.Integer, db.ForeignKey('informacion.id_informacion'), nullable=False)
    estado = db.Column(db.Boolean, nullable=False, default=True)

class preguntas(db.Model):
    id_preguntas = db.Column(db.Integer, primary_key=True)
    preguntas = db.Column(db.String(80), nullable=False)

class respuestas(db.Model):
    id_respuestas = db.Column(db.Integer, primary_key=True)
    id_preguntas = db.Column(db.Integer, db.ForeignKey('preguntas.id_preguntas'), nullable=False)
    respuestas = db.Column(db.String(80), nullable=False)
    tipo_recomendado = db.Column(db.Enum('Restaurantes', 'Hoteles', 'Productos_Artesanales', 'Lugar_Turistico', name='recomendado_enum'), nullable=False)  # Ajuste de valores enumerados

class Respuestas_usuario(db.Model):
    id_respuestas_usuario = db.Column(db.Integer, primary_key=True)
    id_usuarios = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuarios'), nullable=False)  # Ajuste del nombre de la clave foránea
    id_respuestas = db.Column(db.Integer, db.ForeignKey('respuestas.id_respuestas'), nullable=False)

