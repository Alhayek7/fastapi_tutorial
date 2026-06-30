
from fastapi import FastAPI,Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


class Item(BaseModel):
          bmi: float
          message: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calculate_bmi")
async def calculate_bmi(
        weight :float=Query(..., gt=20 , lt = 300 ,description="Weight in kilograms"),
        height: float=Query(..., gt=0.5 , lt = 3 ,description="Height in meters")
):
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            message = "Underweight"
        elif bmi < 25:
            message = "Normal weight"
        elif bmi < 30:
            message = "Overweight"
        else:
            message = "Obese"

        return Item(bmi=bmi, message=message)


