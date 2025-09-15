from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routes import auth, user, chat, group, channel, bot

# Create all tables (for SQLite or SQL DB)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Develop App")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing only, adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(group.router, prefix="/group", tags=["group"])
app.include_router(channel.router, prefix="/channel", tags=["channel"])
app.include_router(bot.router, prefix="/bot", tags=["bot"])

@app.get("/")
def root():
    return {"message": "Develop App is running!"}