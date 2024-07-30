# 1. Folder Structure
```
├── model
│   ├── Data analysis.ipynb  
│   ├── model.ipynb
│   ├── model.joblib   # model serial to serve the model
├── db
│   ├── db.py          # creation of the database to store the future incoming data that ML makes predictions on
│   ├── test.db        # SQLITE database in which the data entries are saved from serve.py (FastAPI app) or app.py
├── tests
│   ├── __init__.py
│   ├── conftest.py    # configuring the tests that is connecting to the database 
│   ├── test_db.py     # test to check the schema of the database
├── Dockerfile         # To build the docker image
├── app.py             # run the ML predictions 
├── app.log            # logging the database issues/activities
├── server.py          # serving the ML on FastAPI
├── server.log         # logging the database activities on the server.log
├── requirements.txt   # packages to be installed
├── README.md          
├── notes
├── environment.yml    # conda environment to setup the python environment
└── .gitignore
```
