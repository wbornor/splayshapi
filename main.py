from fastapi import FastAPI

from app.db import initialize_db
from app.domain.items import ItemsDomain
from app.repository.items import ItemsRepository
from app.routers.items import ItemsRouter

app = FastAPI()

db = initialize_db()
items_repository = ItemsRepository(db)
items_domain = ItemsDomain(items_repository)
items_router = ItemsRouter(items_domain)

app.include_router(items_router.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
