from django.db.models import Max

from ..models import Patient, Gene, Tissue, Organ, SampleType, Sample, MoleculeProfile, SNP_Mutation, Study, \
    CancertType, StudySample, Snpmutant
import string
import random
class FakerCbiooprtal():
    def generate_fake_patient(self,count):
        from faker import Faker
        faker = Faker()
        fake_sex = ["Male","Female"]
        fake_race = ["Asia","Pacific Islander","White","Black","Hispanic"]
        for i in range(count):
            patient = Patient(sex=random.choice(fake_sex),
                              race=random.choice(fake_race),
                              code=str(faker.numerify(text="####")),
                              age = random.randint(50,60))
            patient.save()
    def generate_sample(self,count ):
        count_tissue = Tissue.objects.aggregate(Max('id'))
        count_organ = Organ.objects.aggregate(Max('id'))
        count_sample_type = SampleType.objects.aggregate(Max('id'))
        count_patient = Patient.objects.aggregate(Max('id'))

        for i in range(count):
            sample_type = SampleType.objects.get(id=random.randint(1,count_sample_type['id__max']))
            organ = Organ.objects.get(id=random.randint(1,count_organ['id__max']))
            patient = Patient.objects.get(id=random.randint(1,count_patient['id__max']))
            tissue = Tissue.objects.get(id=random.randint(1,count_tissue['id__max']))
            sample = Sample(sample_type = sample_type,tissue = tissue, organ = organ, patient = patient)
            sample.save()

    def generate_gene(self,count):
        for i in range(count):
            length = random.randint(2,6)
            gene_name = "".join(random.choices(string.ascii_uppercase,k=length)) + str(random.randint(1,9))
            gene = Gene(gene_name=gene_name,start_position=random.randint(100,1000) , end_position= random.randint(800,2000))
            gene.save()
    def generated_mutant_genes(self,count):
        count_gene = Gene.objects.aggregate(Max('id'))
        count_molecule = MoleculeProfile.objects.aggregate(Max('id'))
        count_sample = Sample.objects.aggregate(Max('id'))

        for i in range(count):
            sample = Sample.objects.get(id=random.randint(1, count_sample['id__max']))
            molecule = MoleculeProfile.objects.get(id=random.randint(1, count_molecule['id__max']))
            gene = Gene.objects.get(id=random.randint(1, count_gene['id__max']))
            mutanted_gene = SNPMutant (sample=sample,molecular_profile=molecule,gene=gene)
            mutanted_gene.save()

    def generate_study_sample(self,count):
        count_study = Study.objects.aggregate(Max('id'))
        count_cancer_type = CancertType.objects.aggregate(Max('id'))
        count_sample = Sample.objects.aggregate(Max('id'))

        for i in range(count):
            sample = Sample.objects.get(id=random.randint(1, count_sample['id__max']))
            cancer_type = CancertType.objects.get(id=random.randint(1, count_cancer_type['id__max']))
            study = Study.objects.get(id=random.randint(1, count_study['id__max']))
            study_sample = StudySample (sample=sample,cancer_type=cancer_type,study=study)
            study_sample.save()