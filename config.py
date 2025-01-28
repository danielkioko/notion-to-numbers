import os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')
NUMBERS_DOC_NAME = os.getenv('NUMBERS_DOC_NAME', 'Notion Data.numbers') 