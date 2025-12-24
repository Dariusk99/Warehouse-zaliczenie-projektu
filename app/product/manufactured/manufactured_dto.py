from marshmallow import Schema, fields, validate
from ..core.product_dto import ProductDTO, ProductSaveDTO

class ManufacturedDTO(ProductDTO):
    bom_id = fields.Int(required=True)

class ManufacturedSaveDTO(ProductSaveDTO):
    type = fields.Constant("manufactured")
    bom_id = fields.Int(required=True)