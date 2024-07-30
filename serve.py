from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import uvicorn
import logging
import sys
from databases import Database
from db.db import features_table
from sqlalchemy import Table, Column, Integer, String, MetaData


app = FastAPI(
    title="Machine Learning Model API",
    description="API to test ML model",
    version="1.0.0"
)

logger = logging.getLogger(__name__)
logging.basicConfig(filename="serve.log")


# Define the input data schema
class Feature(BaseModel):
    home_id: str = Field(description="The unique identifier for the home")
    bathroom1: int = Field(description="Total sensor frequency to the bathroom1 in a month")
    hallway: int = Field(description="Total sensor frequency to the hallway in a month")

class_labels = {0: "Single Occupant", 1: "Multiple Occupants"}

# Define the response schema
class PredictionResponse(BaseModel):
    prediction_value: int = Field(description="ML Prediction")
    description: str = Field(description="Giving the multiple occupancy information")

# Load the trained model from joblib
loaded_model = joblib.load('./model/model.joblib')

# Database URL
DATABASE_URL = "sqlite:///./db/test.db"
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

#gracefully shuts down the database
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction Endpoint"])
async def predict(feature: Feature):
    """
    Endpoint for making the prediction \n
    Enter in the Request body the values of the total sensor frequency of bathroom1 and hallway along with the home id
    """
    # Convert input data to pandas DataFrame
    data = pd.DataFrame([{"bathroom1": feature.bathroom1, 'hallway': feature.hallway}])

    # Make prediction
    prediction = loaded_model.predict(data)
    predict_value = int(prediction[0])
    class_label = class_labels[predict_value]


    # Write data to the database
    query = features_table.insert().values(
        home_id=feature.home_id,
        bathroom1=feature.bathroom1,
        hallway=feature.hallway
    )
    try:
        await database.execute(query)
    except Exception as e:
        logger.error(f"Failed to save data to database {e}")
        raise HTTPException(status_code=500, detail="Failed to save data to database")



    response = {
        "prediction_value": predict_value,
        "description": f"The prediction based on the data is that the home id {feature.home_id} has {class_label}"
    }

    return response

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
