import logging
from typing import Dict, List
from fastapi import HTTPException
from config import client

logger = logging.getLogger(__name__)
async def chat_helper(message: Dict, model: str = "gpt-4",
                       system_configuration: str = "You are a helpful assistant.",
                       message_history: List[Dict] = []):
    messages = [{"role":"system", "content": system_configuration}] + message_history + [message]
    logger.debug(f"Sending message to model {model}: {messages}")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        answer = response.choices[0].message.content
        logger.debug(f"Received response from model {model}: {answer}")
        return answer
    except Exception as e:
        logger.error(f"Error in chat_helper: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")