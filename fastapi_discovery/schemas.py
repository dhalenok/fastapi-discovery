from pydantic import BaseModel


class ExpenseBase(BaseModel):
    amount: int
    category: str


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int

    class Config:
        orm_mode = True
