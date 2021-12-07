from django.urls import path
from .views import Projectview

urlpatterns = [
    path('projects/', Projectview.as_view()),
]
