from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    username : str
    email : str 
    
class Message(BaseModel):
    sender_id : str
    receiver_id : Optional[str] = None 
    message : str 
    timestamp : Optional[datetime] = None     
    