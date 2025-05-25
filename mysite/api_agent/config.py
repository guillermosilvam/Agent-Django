
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from .tools import tools

model = init_chat_model("command-r-plus", model_provider="cohere")
memory = MemorySaver()

agent = create_react_agent(
    model=model,
    tools=tools,
    prompt="Eres un agente de IA que puede realizar tareas como sumar, restar y buscar información en la web.",
    checkpointer=memory,
)
