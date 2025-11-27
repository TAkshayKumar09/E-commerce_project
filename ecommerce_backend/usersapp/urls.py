from django.urls import path
from . import views


urlpatterns=[
    path("register/",view=views.register),
    path("login/", view=views.login),
    path("update_user/", view=views.update_user),
    path("delete_user/", view=views.delete_user),

    path("home/",view=views.home),
    path("adminUser/",view=views.admin),
    path("delete_product/<str:title>/", view=views.delete_product)
]