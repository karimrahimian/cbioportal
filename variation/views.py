from django.http import HttpResponse
from django.shortcuts import render
from .generate_fake_data.faker_bio import FakerCbiooprtal
from .models import StudyType, Study


# Create your views here.
def index(request):
    context = {"hasError":False,"study_types":None}
    context["study_types"]= StudyType.objects.all()

    return render(request, 'index.html',context = context)
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request,'register.html')
def generate_data(request):
    fake_generator = FakerCbiooprtal()
    #fake_generator.generate_fake_patient(count=30)
    fake_generator.generate_gene(30)
    return HttpResponse("All data generated")