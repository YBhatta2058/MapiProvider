from django.shortcuts import render,HttpResponse
from .models import BlogDB
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

def serialize_blogs(blogs):
    serialized_data = serializers.serialize('json',blogs,fields = ('title','img','content'))
    return serialized_data

def blog_list(request):
    blogs = BlogDB.objects.all()
    serialized_data = serialize_blogs(blogs)
    return JsonResponse(serialized_data,safe = False)