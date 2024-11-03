from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.

fruits = ['apple','mango','banana']

def index(request):
    data = "Ash"
    data2 = {"name":"Ashish Jain","Profession":"Software Developer"}
    data3 = choice(fruits)
    return HttpResponse(f"Hey {data}! You are a {data2['Profession']}. Random Fruit: {data3.title()}")