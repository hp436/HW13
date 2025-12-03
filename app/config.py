from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # ---------------------------------------------------------
    # Database configuration
    # ---------------------------------------------------------
    DATABASE_URL: str = "sqlite:///./fastapi.db"


    # ---------------------------------------------------------
    # JWT configuration
    # ---------------------------------------------------------
    JWT_SECRET: str = "your-secret-key"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
