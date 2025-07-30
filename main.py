
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from database import SessionLocal, engine, Base, Transaction
from model import classify_transaction

app = FastAPI()

Base.metadata.create_all(bind=engine)

class TransactionInput(BaseModel):
    merchant: str
    description: str
    amount: float
    date: str

@app.post("/analyze_transaction")
def analyze_transaction(data: TransactionInput):
    db = SessionLocal()
    try:
        text = data.merchant + " " + data.description
        category = classify_transaction(text)
        new_tx = Transaction(
            merchant=data.merchant,
            description=data.description,
            amount=data.amount,
            date=data.date,
            category=category
        )
        db.add(new_tx)
        db.commit()
        db.refresh(new_tx)
        return {"status": "added", "category": category}
    finally:
        db.close()

@app.get("/expenses_summary")
def get_summary(month: str, year: str):
    db = SessionLocal()
    try:
        from collections import Counter
        results = db.query(Transaction.category).filter(Transaction.date.like(f"{year}-{month}-%")).all()
        count = Counter([r[0] for r in results])
        return {"summary": [{"category": k, "transactions_count": v} for k, v in count.items()]}
    finally:
        db.close()
