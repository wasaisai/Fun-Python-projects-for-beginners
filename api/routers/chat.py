from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse

from services.recorde_message import recorder
import uuid


router = APIRouter()

@router.get("/api/chat")
async def chat(body:dict):
    message = body.get('message')
    
    recorder(message, '北京今天是晴天', uuid.uuid4(), '天气'  )
    
    if not message:
        print('message不能为空')
        return None
    
    messages = [
        { "roule": "user"},
        { "content": "你好"}
    ]
    
    return messages
    