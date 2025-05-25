import os
from dotenv import load_dotenv

load_dotenv()

chat_cohere = os.getenv("COHERE_API_KEY")
tavily_search = os.getenv("TAVILY_API_KEY")