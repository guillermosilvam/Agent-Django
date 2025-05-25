from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

@tool
def suma(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

@tool
def resta(a: float, b: float) -> float:
    """Resta dos números."""
    return a - b


tavilysearch = TavilySearch(
    max_results=3,
    topic="general",
)

tools = [
    suma, 
    resta, 
    tavilysearch
]