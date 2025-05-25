from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from langchain_core.messages import HumanMessage
from .config import agent
from rest_framework.response import Response
from .serializer import PromptSerializer

class ApiAgentView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = PromptSerializer

    def post(self, request):
        prompt = request.data.get("prompt")
        thread_id = request.data.get("id")
        config = {
            "configurable": {"thread_id": thread_id}
        }

        messages = [HumanMessage(content=prompt)]
        messages = agent.invoke({"messages" : messages}, config)
        return Response ({
            "message" : "successfully fetched response",
            "data" : messages["messages"][-1].content
        })
