from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Central settings object.
    Reads all config from the .env file.
    """
    APP_NAME: str
    MODE: str
    APP_PORT: int

    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URL: str

    # ✅ Pydantic V2 configuration
    model_config = SettingsConfigDict(
        env_file=".env",   # read environment variables from .env
        extra="ignore"     # ignore any extra env vars you might add
    )

# Instantiate settings once, can be imported anywhere
settings = Settings()
