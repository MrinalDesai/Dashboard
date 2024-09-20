# Import the necessary module
from dotenv import load_dotenv
import os
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

# Example usage
print(f'SECRET_KEY: {PASSWORD}')