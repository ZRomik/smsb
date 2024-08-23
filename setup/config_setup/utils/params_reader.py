from os import getenv
from dotenv import load_dotenv

def read_param(key: str, default: str = None, filename: str = '.env') -> str | None:
    load_dotenv(filename)
    return getenv(key, default)