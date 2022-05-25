from django.urls import path, include
from event import views

urlpatterns = [
    path('', views.user_events),
    path('all/', views.get_all_events)
]