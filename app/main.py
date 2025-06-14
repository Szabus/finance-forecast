from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ExpenseInput(BaseModel):
    food: float
    rent: float
    transport: float

@app.get("/")
def read_root():
    return {"message": "Welcome to Finance Forecast App"}

@app.post("/predict")
def predict_expense(data: ExpenseInput):
    total = data.food + data.rent + data.transport
    prediction = total * 1.05  # dummy előrejelzés
    return {"predicted_total": prediction}
