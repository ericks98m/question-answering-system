from django.urls import path
from . import views

app_name = 'qansweringApp'
urlpatterns = [
    path("",views.index, name = "index"),
    path("qaimprovado/",views.qanswering_view, name = "qaimprovado")
]
