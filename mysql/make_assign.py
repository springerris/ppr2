import random
from datetime import date
from faker import Faker
from transliterate import translit

faker = Faker('ru_RU')

queuefile = open("queueassign.txt", "w+")
dol=[1,2,2,3,3,3,4]
queue = "INSERT INTO assign(room_id,em_id) VALUES"
employees = [i+1 for i in range(50)]
print(employees)
k = 0

for i in range(8):
    parts = ""
    random.shuffle(employees)
    ch1 = random.randint(4,9)
    for j in range(ch1):
        parts = parts + f"({i+1},{employees[j]})" + ","
        k = k + 1   

    parts = parts + "\n"
    queue = queue  + parts

     
    
    
    
print(k)

queuefile.write(queue)

print(queue)