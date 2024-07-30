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

# 2. Setting up the project by conda
   
```
conda env create -f environment.yml
conda activate imperial_de
```

# 3. Setup the database to collect the data entered into the API

```
python db/db.py
```

# 4. Run the Model Serving
By using the argparse. For example,

```
python app.py --home-id "fknr324" --bathroom1 3423 --hallway 342143
```

Or by running the app on FastAPI
``` 
uvicorn serve:app
```

# 5. (Optionally) Run the app on the Docker. Docker enables us to run the app on any platform without requiring specific configuration

```
docker push 785854/mlapp:latest
docker run -d --name mlapp -p 8000:8000 785854/mlapp:latest
```

6. Test the FastAPI on the localhost with port number as below;

```
http://127.0.0.1:8000/docs
```
