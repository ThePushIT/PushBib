import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_URL = os.getenv("DATABASE_URL")
ENV = os.getenv("FLASK_ENV") or "production"
SECRET_KEY = os.getenv('SECRET_KEY')

if DATABASE_URL is None:
    raise Exception(
        f"Database URI is not defined with the DATABASE_URL environment variable"
    )

# Fix for Fly
DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://')
