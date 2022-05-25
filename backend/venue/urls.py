from django.urls import path, include
from venue import views

urlpatterns = [
    path('', views.user_venues),
    path('all/', views.get_all_venues)
    ]