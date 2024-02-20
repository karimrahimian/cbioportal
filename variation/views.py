from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .generate_fake_data.faker_bio import FakerCbiooprtal
from .models import StudyType, Study, StudySample, SNP_Mutation, Sample, Snpmutant
from .utils.graphtools import Graph

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
    fake_generator.generated_mutant_genes(800)
    #fake_generator.generate_study_sample(400)
    return HttpResponse("All data generated")

def analysis(request):
   context = {"snpmutant":None,'sexpie':None}
   if request.method == 'POST':
        study_id = (request.POST['study_id'])
        sample_id = list(StudySample.objects.filter(study_id=study_id).values_list('sample_id').all())
        snp = list(SNP_Mutation.objects.
                                filter(sample__in=sample_id).
                                select_related('gene').
                                values_list('gene__gene_name').
                                annotate(count_sample=Count('gene')).order_by('count_sample'))
        sample_ids = []
        for id in sample_id:
            sample_ids.append(id[0])
        patinetdata = Sample.objects.filter(pk__in=sample_ids).select_related('patient_id').values_list('patient__age','patient__sex','patient__race')
        graph = Graph()
        context['sexpie'] = graph.pie_plot_patient(patinetdata,"Sex","Sex")
        context['racepie'] = graph.pie_plot_patient(patinetdata,"Race","Race")
        context['agebar'] = graph.bar_plot_patient(patinetdata,"Age","Age")
        context['snpmutant'] = snp[::-1]
        patinetdata = Sample.objects.filter(pk__in=sample_ids).values_list('patient_id', 'patient__age','patient__sex','patient__race','patient__code',
                                                                      'tissue__name','organ__name','sample_type__sample_type').distinct()
        context['dataset'] = patinetdata

        tt= 1


   return render(request,'analysis.html',context=context)
@csrf_exempt
def queryApi(request):
    print("Salam")
    return HttpResponse('Salam')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
