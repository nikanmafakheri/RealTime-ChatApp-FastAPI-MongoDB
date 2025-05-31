from fastapi import FastAPI
from db.mongo import db
from models import User , Message
from datetime import datetime

app = FastAPI()

@app.post("/users/")
async def get_users():
    await db["users"].insert_one()