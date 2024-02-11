from ..models import Patient,Gene
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
        pass
    def generate_gene(self,count):
        for i in range(count):
            length = random.randint(2,6)
            gene_name = "".join(random.choices(string.ascii_uppercase,k=length)) + str(random.randint(1,9))
            gene = Gene(gene_name=gene_name,start_position=random.randint(100,1000) , end_position= random.randint(800,2000))
            gene.save()



