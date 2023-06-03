import os
from .base import *

from dotenv import load_dotenv

dotenv_path = os.path.join(BASE_DIR,'.env')

load_dotenv(dotenv_path = dotenv_path)
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['.vercel.app','.now.sh','127.0.0.1'] 