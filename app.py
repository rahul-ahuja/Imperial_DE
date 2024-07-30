import argparse
import joblib
import pandas as pd 
import logging
import sqlite3
from typing import Union

parser = argparse.ArgumentParser(description="This is for putting the data values")
parser.add_argument("--home-id", "-home_id", type=str, help="home id of the data values", required=True)
parser.add_argument("--bathroom1", "-bathroom1", type=int, help="Total sensor frequency to the bathroom1 across a month", required=True)
parser.add_argument("--hallway", "-hallway", type=int, help="Total sensor frequency to the bathroom1 across a month", required=True)

args = parser.parse_args()

class_labels = {0: "Single Occupant", 1: "Multiple Occupants"}

# Load the trained model from joblib
loaded_model = joblib.load('./model/model.joblib')

# Configure logging
logging.basicConfig(
    filename="app.log", 
    filemode='a',  # Append mode (default is 'a'), 'w' for write mode which overwrites the file
    level=logging.INFO,  # Set the logging level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # Define the log message format
)

# Get a logger instance
logger = logging.getLogger(__name__)

def database_conn():
    # Connect to the SQLite database if it exists 
    try:
        conn = sqlite3.connect('./db/test.db')
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}. Try running the following in python \n python db/db.py")
        logger.error("Database connection failed: {e}.")
        return None


def predict(args, conn) -> Union[dict, None]:
    """
    Endpoint for making the prediction \n
    Enter in the Request body the values of the total sensor frequency of bathroom1 and hallway along with the home id
    """
    # Convert input data to pandas DataFrame
    data = pd.DataFrame([{"bathroom1": args.bathroom1, 'hallway': args.hallway}])

    # Make prediction
    prediction = loaded_model.predict(data)
    predict_value = int(prediction[0])
    class_label = class_labels[predict_value]

    response = {
        "prediction_value": predict_value,
        "description": f"The prediction based on the data is that the home id {args.home_id} has {class_label}"
    }

    if conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO features (home_id, bathroom1, hallway) VALUES (?, ?, ?)", (args.home_id, args.bathroom1, args.hallway))
        conn.commit()

        logger.info("Data entries saved successfully to the database")

        return response
    else:
        logger.info("Data entries were not saved into the Database. Try connecting to the database if not connected")
        return None


if __name__ == "__main__":
    conn = database_conn()
    print(predict(args, conn))
    conn.close()

