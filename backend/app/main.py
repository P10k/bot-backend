from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.admin import router as admin_router


app = FastAPI(title="AI Admission Assistant API")


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://bot-frontend-brown.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(chat_router)

app.include_router(admin_router)


# Root Route
@app.get("/")
def home():

    return {"message": "AI Admission Assistant Backend Running"}
