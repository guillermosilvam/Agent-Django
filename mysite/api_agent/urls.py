from .views import ApiAgentView
from django.urls import path


urlpatterns = [
    path('api/agent/', ApiAgentView.as_view(), name='api_agent'),
]