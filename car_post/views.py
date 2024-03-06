from django.shortcuts import render,redirect
from .import forms
# Create your views here.

def addCarPost(request):
    if request.method=="POST":
        post_form= forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('home')
    else:
         post_form= forms.PostForm()

    return render(request,'carPost.html',{'form':post_form})

     
