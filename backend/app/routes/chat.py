from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import ask_llm
from app.services.rag_service import retrieve_context

from app.services.conversation_memory import add_message, get_history

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):

    user_message = req.message

    session_id = "web_user"

    # Save user message and session ID to conversation memorygit commit -m "fixed routes folder"
    add_message(session_id, "user", user_message)

    # Retrieve conversation history
    history = get_history(session_id)

    # Retrieve relevant contextt
    context = retrieve_context(user_message)

    # Generate AI response
    answer = ask_llm(user_query=user_message, context=context, history=history)

    # Save AI response
    add_message(session_id, "assistant", answer)

    return {"response": answer}
