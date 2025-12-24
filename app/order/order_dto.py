from marshmallow import Schema, fields, validate

class OrderItemInputDTO(Schema):
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True, validate=validate.Range(min=1))

class OrderDTO(Schema):
    id = fields.Integer(dump_only=True)
    customer = fields.Str(required=True)
    address = fields.Str(required=True)
    phone_number = fields.Integer()
    items = fields.Nested('OrderItemDTO', many=True)

class OrderItemDTO(Schema):
    id = fields.Integer()
    product_name = fields.String(attribute="product.name")
    quantity = fields.Integer()

class OrderSaveDTO(Schema):
    customer = fields.Str(required=True, validate=validate.Length(min=3))
    address = fields.Str(required=True, validate=validate.Length(min=3))
    phone_number = fields.Integer(required=True)
    products = fields.List(fields.Nested(OrderItemInputDTO), required=True)