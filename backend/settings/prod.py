import os
from .base import *

from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['.vercel.app','.now.sh'] 