import os
from configparser import RawConfigParser
from dotenv import load_dotenv


def get_database_url():
    load_dotenv()
    config = RawConfigParser()
    config.read('/home/user/Python/IntoTheWild/backend/alembic.ini')
    db_url_template = config.get('alembic', 'sqlalchemy.url')
    print('db_url_template', db_url_template)

    db_url = db_url_template % {
        'DB_USER': os.environ.get('DB_USER'),
        'DB_PASS': os.environ.get('DB_PASS'),
        'DB_HOST': os.environ.get('DB_HOST'),
        'DB_PORT': os.environ.get('DB_PORT'),
        'DB_NAME': os.environ.get('DB_NAME')
    }

    return db_url


if __name__ == "__main__":

    print("Database URL:", get_database_url())
