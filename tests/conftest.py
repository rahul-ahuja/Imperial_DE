import pytest
import sqlite3
import os

@pytest.fixture
def db_connection():
    db_path = './db/test.db'  
    assert os.path.exists(db_path), f"Database file not found: {db_path}"
    connection = sqlite3.connect(db_path)
    yield connection
    connection.close()

@pytest.fixture
def db_cursor(db_connection):
    return db_connection.cursor()
