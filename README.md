# 1. Folder Structure
```
├── model
│   ├── Data analysis.ipynb  
│   ├── model.ipynb
│   ├── model.joblib # model serial to serve the model
├── db
│   ├── db.py # creation of the database to store the future incoming data that ML makes predictions on
│   ├── test.db # SQLITE database in which the data entries are saved from serve.py (FastAPI app) or app.py
├── tests
│   ├── __init__.py
│   ├── conftest.py #configuring the tests that is connecting to the database 
│   ├── test_db.py #test to check the schema of the database
├── Dockerfile #To build the docker image
├── app.py 
├── app.log
├── server.py
├── server.log
├── requirements.txt
├── README.md
├── notes
├── environment.yml
├── server.py
└── .gitignore
```
