from django.shortcuts import render

from car_list.models import Category
from car_post.models import Car


def home(request):
    categories=Category.objects.all()
    data=Car.objects.all()
    return render(request,'home.html',{'categories': categories,'data':data})