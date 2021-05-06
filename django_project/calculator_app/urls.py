from django.urls import path
from . import views
urlpatterns = [
    path('', views.root, name='root'),
    path('calculator_app', views.index, name='index'),
    path('submitquery', views.submitquery, name="submitquery")
]