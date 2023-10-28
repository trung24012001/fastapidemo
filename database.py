from models import *
from db.session import engine


Base.metadata.create_all(engine)
