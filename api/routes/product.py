from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api import deps
from schemas import ProductSchema, ProductCreate
import crud

router = APIRouter()


@router.get("/", response_model=list)
def get_products(db: Session = Depends(deps.get_db)):
    return crud.product.get_all(db)


@router.get("/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(deps.get_db)):
    product = crud.product.get(db, id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )
    return product


@router.post("/", response_model=ProductSchema)
def create_product(product_in: ProductCreate, db: Session = Depends(deps.get_db)):
    product = crud.product.create(db, product_in)
    return product
