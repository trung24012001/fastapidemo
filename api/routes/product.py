from fastapi import APIRouter


router = APIRouter()

products = [{"name": "product1"}]


@router.get("/", response_model=list)
def get_products():
    return products
