# coding: utf-8
#quickstart/views.py
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer