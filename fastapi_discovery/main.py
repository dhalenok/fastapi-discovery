from typing import Dict
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from fastapi_discovery import crud, schemas
from fastapi_discovery.database import SessionLocal, engine, Base

app = FastAPI()

Base.metadata.create_all(engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/expenses/")
async def get_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)


@app.get("/expenses/{expense_id}/")
async def get_expense(expense_id: int, db: Session = Depends(get_db)):
    return crud.get_expense(db=db, expense_id=expense_id)


@app.post("/expenses/", response_model=schemas.Expense, status_code=201)
async def create_expense(
    expense: schemas.ExpenseCreate, db: Session = Depends(get_db)
) -> Dict:
    return crud.create_expense(db=db, expense=expense)
