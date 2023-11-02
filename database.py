from models import *
from db.session import engine
from db.session import SessionLocal
from schemas import UserSchema, ProductSchema
import crud

Base.metadata.create_all(engine)

db = SessionLocal()


def init_users():
    users = [
        UserSchema(id=1, name="Trung", username="trung", role="admin", products=[])
    ]
    for user in users:
        crud.user.create(db, obj_in=user)


def init_products():
    products = [
        ProductSchema(id=1, name="Product1", description="This is product1", user_id=1)
    ]
    for product in products:
        crud.product.create(db, obj_in=product)


def remove_user():
    user = crud.user.get(db, id=1)
    crud.user.remove(db, obj=user)


def init_db():
    init_users()
    init_products()


init_db()
# remove_user()
