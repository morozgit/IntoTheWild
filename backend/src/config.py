# from dotenv import dotenv_values

# config = dotenv_values(".env")

# DB_HOST = config.get("DB_HOST")
# DB_PORT = config.get("DB_PORT")
# DB_NAME = config.get("DB_NAME")
# DB_USER = config.get("DB_USER")
# DB_PASS = config.get("DB_PASS")

# # DB_HOST_TEST = os.environ.get("DB_HOST_TEST")
# # DB_PORT_TEST = os.environ.get("DB_PORT_TEST")
# # DB_NAME_TEST = os.environ.get("DB_NAME_TEST")
# # DB_USER_TEST = os.environ.get("DB_USER_TEST")
# # DB_PASS_TEST = os.environ.get("DB_PASS_TEST")

# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: str
    
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

# from dotenv import dotenv_values

# config = dotenv_values(".env")

# DB_HOST=config.get("DB_HOST")
# DB_PORT=config.get("DB_PORT")
# DB_USER=config.get("DB_USER")
# DB_PASS=config.get("DB_PASS")
# DB_NAME=config.get("DB_NAME")
# DATABASE_URL=f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# class settings:
#     DB_HOST=DB_HOST
#     DB_PORT=DB_PORT
#     DB_USER=DB_USER
#     DB_PASS=DB_PASS
#     DB_NAME=DB_NAME
#     DATABASE_URL=DATABASE_URL