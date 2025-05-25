# README

## Installation

To use this project, you'll need to have the following dependencies installed:

- Python 3.x
- Django
- Django REST Framework
- Langchain
- Cohere
- Dotenv

You can install these dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

This project provides a Django-based API that allows you to interact with a language model agent. The agent can perform various tasks, such as addition, subtraction, and web search.

To use the API, you can send a POST request to the `/api/agent/` endpoint with a `prompt` and an optional `id` parameter. The agent will process the prompt and return a response.

Here's an example of how to use the API:

```python
import requests

url = "http://localhost:8000/api/agent/"
data = {
    "prompt": "What is 2 + 3?",
    "id": 1
}

response = requests.post(url, json=data)
print(response.json())
```

This will output the agent's response to the provided prompt.

## API

The API provides the following endpoints:

### `/api/agent/`

- **Method**: POST
- **Parameters**:
  - `prompt` (required): The prompt to be processed by the agent.
  - `id` (optional): The ID of the conversation thread.
- **Response**:
  - `message`: A message indicating the successful fetching of the response.
  - `data`: The agent's response to the provided prompt.

The API also provides a Swagger UI documentation at the `/api/schema/swagger-ui/` endpoint, which allows you to explore and interact with the API.
