from fastapi import FastAPI, HTTPException , WebSocket
from db.mongo import db
from models import User, Message
from datetime import datetime
from bson import ObjectId

app = FastAPI()

@app.post("/users/")
async def create_user(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    result = await db.users.insert_one(user.dict())
    return {"id": str(result.inserted_id), "message": "User created successfully"}

@app.post("/messages/")
async def send_message(message: Message):
    message_data = message.dict()
    message_data["timestamp"] = message.timestamp or datetime.utcnow()

    result = await db.messages.insert_one(message_data)
    return {"id": str(result.inserted_id), "message": "Message sent"}

@app.get("/messages/{sender_id}/{receiver_id}")
async def get_messages(sender_id: str, receiver_id: str):
    messages = db.messages.find({
        "$or": [
            {"sender_id": sender_id, "receiver_id": receiver_id},
            {"sender_id": receiver_id, "receiver_id": sender_id}
        ]
    })

    result = []
    async for msg in messages:
        msg["_id"] = str(msg["_id"])
        result.append(msg)
    return result

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")