from fastapi import APIRouter
from .routes import user, product

# Admin
api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(product.router, prefix="/products", tags=["products"])
