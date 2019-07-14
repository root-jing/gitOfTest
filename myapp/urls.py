from django.urls import path
from . import views
app_name="myapp"
urlpatterns = [
    path("",views.index,name="index"),
    path("fruits/",views.fruits,name="fruits"),
    path("add/",views.add,name="add"),
]