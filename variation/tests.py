import random

import mysql.connector
from mysql.connector import Error
from faker import Faker

Faker.seed(33422)
fake = Faker()

conn = mysql.connector.connect(host="localhost", database="cbioportal",
                               user="root", password="123456",port=3307)
cursor = conn.cursor()

row = [fake.first_name(), random.randint(0, 99), fake.date_of_birth()]
fake.last_name()


cursor.execute(f"INSERT INTO `patients` (name, age, birth_day) VALUES ('{row[0]}', '{row[1]}', '{row[2]}')")

conn.commit()