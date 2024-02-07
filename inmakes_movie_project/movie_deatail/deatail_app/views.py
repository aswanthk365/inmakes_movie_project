from django.shortcuts import render,redirect
from .models import *
from . forms import update_form
# Create your views here.

def index(request):
    movie=movies.objects.all()
    return render(request,'index.html',{'movie':movie})

def movie_deatail(request,mov_id):
    get_id=movies.objects.get(id=mov_id)
    return render(request,'deatail.html',{'get_id':get_id})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        discription=request.POST.get('discription')
        year=request.POST.get('year')
        movie_image=request.FILES['movie_image']
        movie=movies(name=name,discription=discription,year=year,movie_image=movie_image)
        movie.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie_id=movies.objects.get(id=id)
    form=update_form(request.POST or None,request.FILES,instance=movie_id)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie_id':movie_id})

def delete(request,id):
    if request.method=='POST':
        delete_id=movies.objects.get(id=id)
        delete_id.delete()
        return redirect('/')
    return render(request,'delete.html')
