from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, 'first_app/index.html', context)

def add_course(request):
    if request.method == 'POST':
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def process(request, id):
    context = {
        "courses": Course.objects.get(id = id)
    }
    return render(request, 'first_app/destroy.html', context)

def destroy(request,id):
    if request.method == 'POST':
        Course.objects.filter(id = id).delete()
    return redirect('/')
