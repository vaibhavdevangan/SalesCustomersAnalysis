from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:new_password@127.0.0.1:5432/Superstore_db"
)
print("Conn Successfull")