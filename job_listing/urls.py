from django.urls import path
from . import views

urlpatterns = [
    path('listing/', views.posting, name="listing")
    ]