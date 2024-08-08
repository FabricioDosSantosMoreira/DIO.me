from store.models.base import CreateBaseModel, UpdateBaseModel
from store.schemas.product import ProductBase


class ProductCreateModel(ProductBase, CreateBaseModel):
    pass

class ProductUpdateModel(ProductBase, UpdateBaseModel):
    pass
