from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import AgentSerializer
from .models import Agent


class AgentListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None


class AgentView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.filter(top_seller=True)
    serializer_class = AgentSerializer
    pagination_class = None
