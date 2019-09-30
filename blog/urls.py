from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.blogposts, name="blogposts"),
    path("<int:blog_id>/", views.detail, name="detail"),
]
