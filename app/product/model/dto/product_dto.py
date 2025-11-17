from marshmallow import Schema, fields, validate

class ProductDTO(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    quantity = fields.Int()
    location = fields.Str()
    category = fields.Str()