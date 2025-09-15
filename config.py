import os

# Secret key for JWT
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour

# Database URL (JSON file for testing or SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test_db.sqlite")  # fallback to SQLite

# Email credentials (for OTP)
EMAIL_USER = os.getenv("EMAIL_USER", "nothingisimpossiblebrother@gmail.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "agntmvxlgazptvow")