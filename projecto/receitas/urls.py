from django.urls import path
from receitas.views import home 


app_name = "receitas"

urlpatterns = [
     
    path("", home, name="home"),
 
]







