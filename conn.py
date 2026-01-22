from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:<your_password>@127.0.0.1:5432/Superstore_db"
)

# Test connection
try:
    connection = engine.connect()
    print("Connection successful ✅")
    connection.close()
except Exception as e:
    print("Connection failed ❌")
    print(e)
