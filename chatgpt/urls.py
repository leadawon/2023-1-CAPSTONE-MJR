from django.urls import path
from . import views

app_name = 'chatgpt'

urlpatterns = [
    path('', views.index, name='index'),
    path('bulk/',views.bulk_import, name='bulk'),
]