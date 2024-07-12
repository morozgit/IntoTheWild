import platform

from envparse import Env

env = Env()

if platform.system() == "Linux":
    DATABASE_URL = env.str(
        "DATABASE_URL",
        default="postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/postgres",
    )
elif platform.system() == "Windows":
    DATABASE_URL = env.str(
        "DATABASE_URL",
        default="postgresql+asyncpg://postgres:postgres@127.0.0.1:5433/postgres",
    )
