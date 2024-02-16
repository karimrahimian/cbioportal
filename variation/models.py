from django.db import models

# Create your models here.

class StudyType(models.Model):
    name = models.CharField(max_length=50)
class Study(models.Model):
    name = models.CharField(max_length=100)
    abstract = models.CharField(max_length=2000)
    findings = models.CharField(max_length=1000)
    doi = models.CharField(max_length=100)
    references = models.CharField(max_length=1000, null=True)
    study_type = models.ForeignKey(StudyType,on_delete=models.CASCADE)
class Tissue(models.Model):
    name = models.CharField(max_length=50)
class Organ(models.Model):
    name = models.CharField(max_length=50)
class ReferenceGenome(models.Model):
    species = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    genome_size = models.IntegerField()
    url = models.URLField()
    build_name = models.CharField(max_length=50)
class CancertType(models.Model):
    identifier = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    reference_genome = models.ForeignKey('ReferenceGenome',on_delete=models.CASCADE)
class Gene(models.Model):
    gene_name = models.CharField(max_length=50)
    start_position = models.IntegerField()
    end_position = models.IntegerField()
class MoleculeProfile(models.Model):
    name = models.CharField(max_length=50)
class SampleType(models.Model):
    sample_type = models.CharField(max_length=50)
class Patient(models.Model):
    sex = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    age = models.IntegerField()
    race = models.CharField(max_length=50)
class Sample(models.Model):
    sample_type = models.ForeignKey(SampleType,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    tissue = models.ForeignKey(Tissue,on_delete=models.CASCADE)
    organ = models.ForeignKey(Organ,on_delete=models.DO_NOTHING,null=True)
class SNP_Mutation(models.Model):
    gene = models.ForeignKey(Gene,on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample,on_delete=models.CASCADE)
    molecular_profile = models.ForeignKey(MoleculeProfile,on_delete=models.CASCADE)
class Snpmutant(models.Model):
    gene = models.ForeignKey(Gene,on_delete=models.CASCADE)
    sample = models.ForeignKey(Sample,on_delete=models.CASCADE)
    molecular_profile = models.ForeignKey(MoleculeProfile,on_delete=models.CASCADE)
class StudySample(models.Model):
    sample = models.ForeignKey(Sample,on_delete=models.CASCADE)
    study = models.ForeignKey(Study,on_delete=models.CASCADE)
    cancer_type = models.ForeignKey(CancertType,on_delete=models.CASCADE)