"""cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

from cookbook.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    # 입력된 graphql 을 검증하기 위한 schema 를 무엇을 할 것인지 설정이 필요한데
    #   1) GraphQLView.as_view(schema=schema) 에서 하거나
    #   2) settings.py 에서 GRAPHENE.SCHEMA 에 등록하거나 (공식 튜토리얼)
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    # for Postman (CSRF 검사 안하도록 우회)
    path('graphql/api', csrf_exempt(GraphQLView.as_view())),
]
