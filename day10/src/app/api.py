from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import get_db
from .models import Item

app = FastAPI()

# Create reusable DB dependency type
DBSession = Annotated[Session, Depends(get_db)]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/db/items")
def create_item(data: dict, db: DBSession):
    item = Item(
        name=data["name"],
        price=data["price"],
        in_stock=data["in_stock"],
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@app.get("/db/items")
def list_items(db: DBSession):
    return db.query(Item).all()
