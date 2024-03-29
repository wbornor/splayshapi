from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from mangum import Mangum

from app.domain.items import ItemsDomain
from app.internal.db import initialize_db
from app.repository.items import ItemsRepository
from app.routers.items import ItemsRouter

# app = FastAPI(root_path="/Prod")
app = FastAPI()

lambda_handler = Mangum(app, lifespan="off")

db = initialize_db()
items_repository = ItemsRepository(db)
items_domain = ItemsDomain(items_repository)
items_router = ItemsRouter(items_domain)

app.include_router(items_router.router)


def my_schema():
    DOCS_TITLE = "Splaysh API"
    DOCS_VERSION = "1.0"
    openapi_schema = get_openapi(
        title=DOCS_TITLE,
        version=DOCS_VERSION,
        routes=app.routes,
    )
    openapi_schema["info"] = {
        "title": DOCS_TITLE,
        "version": DOCS_VERSION,
        "description": "REST Interface for Splaysh",
        "servers": [
            {"url": "https://merymlbcs3.execute-api.us-east-1.amazonaws.com/Prod", "description": "Dev environment"}
        ],
        "license": {
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
        },
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = my_schema


@app.get("/")
def read_root():
    return {"Hello": "World"}
