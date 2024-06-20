import random
from datetime import date

queuefile = open("queuepc.txt", "w+")
pcs = [1,2,3,4,5]
gpus = [1,2,2,3,3,4,4,4,5,6]
rams = [1,2,3,4,5]
drives = [1,2,3,4,5,6]
rooms = [1,2,3,4,5,6,7,8]
mice = [1,2,3]
kboards = [1,2,3]
mons = [1,2,3]
queue = "INSERT INTO computer(cpu_id,gpu_id,dr_id1,dr_id2,ram1_id,ram2_id,m_id,kb_id,mon_id,room_id,assign_date,move_date) VALUES"

for i in range(28):
    ch1 = random.randint(1,10)
    ch2 = random.randint(1,10)
    ch3 = random.randint(1,3)
    ch4 = random.randint(1,100)
    pc =  random.choice(pcs)
    gp =  random.choice(gpus)
    ram1= random.choice(rams)
    dr1 = random.choice(drives)
    m_id = random.choice(mice)
    kb_id = random.choice(kboards)
    mon_id = random.choice(mons)

    if ch4 < 95:
        room = random.choice(rooms)
        move = '\'' + str(date.today()) + '\''
    else:
        room = "NULL"
        move = "NULL"

    if ch3 == 1: adate = "\'2024-04-04\'"
    if ch3 == 2: adate = "\'2024-01-01\'"
    if ch3 == 3: adate = "\'2024-10-10\'"
    

    if ch1 < 7:
        ram2 = ram1
    else:
        ram2 = "NULL"
    
    if ch2 < 6:
        dr2 = dr1
    else:
        dr2 = "NULL"
    
    for i in range(10):
        part = f'({pc},{gp},{dr1},{dr2},{ram1},{ram2},{m_id},{kb_id},{mon_id},{room},{adate},{move})'
        part = part + ","
        if i % 2 == 0:
            part = part + "\n"
        queue = queue + part
queuefile.write(queue)

print(queue)