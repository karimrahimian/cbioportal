import csv

import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count, Sum, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .generate_fake_data.faker_bio import FakerCbiooprtal
from .models import StudyType, Study, StudySample, SNP_Mutation, Sample, Snpmutant, Tissue
from .utils.graphtools import Graph


# Create your views here.
def index(request):
    context = {"hasError": False, "study_types": None}
    context["study_types"] = StudyType.objects.annotate(study_count=Count('study')).all()
    context["studies"] = Study.objects.select_related('study_type').annotate(sample_count=Count('studysample')).all()
    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def generate_data(request):
    fake_generator = FakerCbiooprtal()
    fake_generator.generate_fake_patient(count=100)
    # fake_generator.generate_gene(100)
    # fake_generator.generate_sample(1000)
    #fake_generator.generated_mutant_genes(800)
    # fake_generator.generate_study_sample(400)
    return HttpResponse("All data generated")


def analysis(request):
    context = {"snpmutant": None, 'sexpie': None}
    if request.method == 'POST':
        study_id = (request.POST['study_id'])
        sample_id = list(StudySample.objects.filter(study_id=study_id).values_list('sample_id').all())
        snp = list(SNP_Mutation.objects.
                   filter(sample__in=sample_id).
                   values_list('gene__gene_name').
                   annotate(count_sample=Count('gene')).order_by('count_sample'))
        sample_ids = []
        for id in sample_id:
            sample_ids.append(id[0])
        patinetdata = Sample.objects.filter(pk__in=sample_ids).values_list('patient__age', 'patient__sex',
                                                                           'patient__race')
        graph = Graph()
        context['sexpie'] = graph.pie_plot_patient(patinetdata, "Sex", "Sex")
        context['racepie'] = graph.pie_plot_patient(patinetdata, "Race", "Race")
        context['agebar'] = graph.bar_plot_patient(patinetdata, "Age", "Age")
        context['snpmutant'] = snp[::-1]
        patinetdata = (
            Sample.objects.filter(pk__in=sample_ids).values_list('patient_id', 'patient__age', 'patient__sex',
                                                                 'patient__race', 'patient__code',
                                                                 'tissue__name', 'organ__name',
                                                                 'sample_type__sample_type').distinct())
        context['dataset'] = patinetdata

        tt = 1

    return render(request, 'analysis.html', context=context)


def queryApi(request):
    print()
    return HttpResponse('Salam')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


def tissuelist(request):
    if request.method == 'GET':
        tissues = Tissue.objects.all().values()
        json_data = json.dumps(list(tissues))
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def api(request):
    query = Q()
    if request.method == 'POST':
        data = json.loads(request.body)
        age_from = data['ageFrom']
        age_to = data['ageTo']
        gender = data['gender']
        race = data['race']
        organ_name = data['organName']
        sample_type = data['sampleType']
        if age_from and age_to:
            query &= Q(patient__age__range=(age_from,age_to))
        if race :
            query &= Q(patient__race__in = race)
        if gender:
            query &= Q(patient__sex__in = gender)
        if organ_name and len(organ_name)>0 and len(organ_name[0])>0:
            query &= Q(organ__name__in = organ_name)
        if sample_type and len(sample_type)>0 and len(sample_type[0])>0:
            query &= Q(sample_type__in = sample_type)

        patinetdata = Sample.objects.filter(query).values_list('patient_id', 'patient__age', 'patient__sex',
                                                  'patient__race', 'patient__code',
                                                  'tissue__name', 'organ__name',
                                                  'sample_type__sample_type').distinct()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename="patientdata.csv"'
        field_names = ['patient_id', 'patient__age', 'patient__sex',
                                                  'patient__race', 'patient__code',
                                                  'tissue__name', 'organ__name',
                                                  'sample_type__sample_type']
        df = pd.DataFrame(list(patinetdata), columns=field_names)

        df.to_csv(path_or_buf=response,index=False)

        return response