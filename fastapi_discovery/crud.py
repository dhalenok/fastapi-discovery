from sqlalchemy.orm import Session
from fastapi_discovery import models, schemas


def get_expense(db: Session, expense_id: int):
    return db.query(models.Expense).filter(models.Expense.id == expense_id).first()


def get_expenses(db: Session):
    return db.query(models.Expense).all()


def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_item = models.Expense(**expense.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
