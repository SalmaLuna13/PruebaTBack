from marshmallow import Schema, fields, ValidationError

class ReseñaSchema(Schema):
    id_informacion = fields.Int(required=True)
    id_usuarios = fields.Int(required=True)  
    cali = fields.Int(required=True)
    comentarios = fields.Str(required=True)
    URL_Foto = fields.Str(required=True)
