from marshmallow import Schema, fields, validate

class ProductDTO(Schema):
    id = fields.Integer(dump_only=True)
    index = fields.Str(required=True)
    name = fields.Str(required=True)
    quantity = fields.Int()
    location = fields.Str()
    category = fields.Str()
    product_type = fields.Str()

class ProductSaveDTO(Schema):
    index = fields.Str(required=True, validate=validate.Length(min=3))
    name = fields.Str(required=True, validate=validate.Length(min=3))
    quantity = fields.Int(required=True, validate=validate.Range(min=0))
    location = fields.Str(required=False, allow_none=True)
    category = fields.Str(required=False, allow_none=True)
    product_type = fields.Str(required=True, validate=validate.OneOf(["product", "manufactured"]))