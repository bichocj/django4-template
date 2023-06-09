from django.urls import path, include
from .views import views

app_name = "dashboard"

urlpatterns = [
    path("", view=views.home_view, name="home"),
    path(r"api/", include(views.router.urls)),
]
