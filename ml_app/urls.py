from django.urls import path
from . import views

urlpatterns = [
    path('',views.predict),
    path('predict',views.predict)
]