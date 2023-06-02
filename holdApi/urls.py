from django.urls import path
from . import views

urlpatterns = [
    path('api/blogs/',views.blog_list,name = "blog-list")
]