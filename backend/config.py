import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    def __init__(self):
        self.jwt_secret_key = os.getenv('SECRET_KEY')
        self.algorithm = os.getenv('ALGORITHM')
        self.access_token_expire_minutes = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))
        self.refresh_token_expire_days = int(os.getenv('REFRESH_TOKEN_EXPIRE_DAYS'))

        self.db_url = f'postgresql+asyncpg://{os.getenv("PG_USERNAME")}:{os.getenv("PG_PASSWORD")}@{os.getenv("PG_HOST")}/{os.getenv("PG_DB")}'


config = Config()
