from marshmallow import Schema, fields, validate

class ProductDTO(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    quantity = fields.Int()
    location = fields.Str()
    category = fields.Str()

class ProductSaveDTO(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3))
    quantity = fields.Int(required=True, validate=validate.Range(min=0))
    location = fields.Str(required=False, allow_none=True)
    category = fields.Str(required=False, allow_none=True)