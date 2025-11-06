from django.urls import path
from . import views,auth_views


urlpatterns = [
    path("", views.index ,  name="home"),
    path('register/', auth_views.register, name='register'),
    path("add-post/", views.add_post, name="add_post"),
    path('login/', auth_views.sgin_out, name='login')


]
