from crud.base import CRUDBase
from schemas import ProductSchema, ProductCreate, ProductUpdate
from models import Product


class CRUDProduct(CRUDBase[ProductSchema, ProductCreate, ProductUpdate]):
    pass


product = CRUDProduct(Product)
