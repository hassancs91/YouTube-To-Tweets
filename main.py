from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Access the environment variables
api_key = os.environ.get('OPENAI_API_KEY')


