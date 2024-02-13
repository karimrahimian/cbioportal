from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from .generate_fake_data.faker_bio import FakerCbiooprtal
from .models import StudyType, Study


# Create your views here.
def index(request):
    context = {"hasError":False,"study_types":None}
    context["study_types"]= StudyType.objects.annotate(study_count=Count('study')).all()
    context["studies"] = Study.objects.select_related('study_type').annotate(sample_count=Count('studysample')).all()
    return render(request, 'index.html',context = context)
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request,'register.html')
def generate_data(request):
    fake_generator = FakerCbiooprtal()
    #fake_generator.generate_fake_patient(count=100)
    #fake_generator.generate_gene(100)
    #fake_generator.generate_sample(1000)
    #fake_generator.generated_mutant_genes(800)
    fake_generator.generate_study_sample(400)
    return HttpResponse("All data generated")

def analysis(request):
   return render(request,'analysis.html')