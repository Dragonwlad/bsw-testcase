import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    DB_URL: str = os.getenv('DB_URL', default=None)
    QUEUE_URL: str = os.getenv('QUEUE_URL', default=None)
    LINE_PROVIDER_URL: str = os.getenv('LINE_PROVIDER_URL', default=None)

    model_config = {
        'env_file': '.env',
        'env_file_encoding': 'utf-8',
    }


settings = Settings()
