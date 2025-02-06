from fastapi import FastAPI
from database.database import Database

app = FastAPI()

db = Database()
_ = db.create_database_add_example_data()

@app.get("/airports")
async def root():
    return db.get_airports()