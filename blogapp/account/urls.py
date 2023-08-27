from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("editorregister", views.editorregister_request, name="editorregister"),
    path("logout", views.logout_request, name="logout"),
    path("myaccount", views.myaccount, name="myaccount"),
    path("inactiveblogs", views.inactiveblogpage, name="inactiveblog")

]