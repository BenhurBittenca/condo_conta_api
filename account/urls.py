from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account import views

prefix = "account/v1/"

urls = [
    path('current-account/', views.currentAccountViewSet.as_view()),
    path('current-account/<pk>', views.currentAccountViewSet.as_view()),
    path('savings-account/', views.savingsAccountViewSet.as_view()),
    path('savings-account/<pk>', views.savingsAccountViewSet.as_view()),
    path('get-account/', views.getAccountViewSet.as_view()),
    path('transfer-account/', views.transferAccountViewSet.as_view()),
]

urlpatterns = [
    path(prefix, include(urls))
]