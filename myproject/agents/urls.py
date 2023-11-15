from django.urls import path
from .views import AgentListView, AgentView, TopSellerView
urlpatterns = [
    path('', AgentListView.as_view(), name='agent-list-view'),
    path('topseller/', TopSellerView.as_view(), name='top-seller'),
    path('<pk>/', AgentView.as_view(), name='agentview'),
]
