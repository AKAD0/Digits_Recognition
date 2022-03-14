from django.urls import path
from . import views
from .img_load import img_load
from .model_init_response import model_init_response
from .img_recognition import img_recognition

urlpatterns = [
    path('', views.Page1),
    path('img_load', img_load.img.load_response),
    path('model_init_response', model_init_response.model.model_init_response),
    path('img_recognition', img_recognition.img_recognition),
]