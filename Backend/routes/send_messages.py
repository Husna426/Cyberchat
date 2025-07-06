from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from utils.openai_helpers import chat_helper
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class ChatInput(BaseModel):
    userInput: str

@router.post("/ask")
async def ask_chat(input_data: ChatInput):
    """
    Endpoint to send a message to the chat model and receive a response.
    """
    message = {"role": "user", "content": input_data.userInput}
    try:
        logger.info(f"Received user input: {input_data.userInput}")
        response = await chat_helper(message)
        logger.info(f"Response from chat model: {response}")
        return JSONResponse(content={"answer": response})
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")    