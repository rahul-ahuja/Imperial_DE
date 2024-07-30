from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String

# Database URL (SQLite in this case)
DATABASE_URL = "sqlite:///./db/test.db"

# Create an instance of the Database class
database = Database(DATABASE_URL)

# Define the metadata object
metadata = MetaData()

# Define the table schema
features_table = Table(
    "features",
    metadata,
    Column("home_id", String, nullable=False),
    Column("bathroom1", Integer, nullable=False),
    Column("hallway", Integer, nullable=False),
)

# Create an engine and create all tables
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
