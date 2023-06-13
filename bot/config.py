import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DBNAME')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')


__all__ = ['TOKEN', 'DB_USER', 'DB_PASSWORD', 'DB_NAME', 'HOST', 'PORT']
