import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from databases import Database

load_dotenv()

DB_URL = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
)

database = Database(DB_URL)
metadata = MetaData()
engine = create_engine(DB_URL)
