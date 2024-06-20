import random
from datetime import date
from faker import Faker
from transliterate import translit

faker = Faker('ru_RU')

queuefile = open("queueemp.txt", "w+")
dol=[1,2,2,3,3,3,4]
queue = "INSERT INTO employee(FIO,dolzh_id) VALUES"

for i in range(50):
    dolid = random.choice(dol)
    full = faker.name()
    fioparts = full.split(" ")
    fio = "\'" + fioparts[1] + " " + fioparts[0][0] + ". " + fioparts[2][0] + ".\'"
    print(fio)

    part = f'({fio},{dolid})'
    if i != 49:
        part = part + ","
    else:
        part = part + ";"
    if i % 2 == 0:
        part = part + "\n"
    queue = queue + part


queuefile.write(queue)

print(queue)