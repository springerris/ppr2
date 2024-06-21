DROP DATABASE IF EXISTS  computer_db;
CREATE DATABASE IF NOT EXISTS computer_db;
USE computer_db;

CREATE TABLE pccpu(
id_c int primary key auto_increment,
model varchar(50) NOT NULL,
freq smallint,
cores tinyint,
cost int
CHECK (cost > 0),
CHECK (cores > 0),
CHECK (freq > 0)
);

CREATE TABLE gpu(
id_g int primary key auto_increment,
model varchar(50) NOT NULL,
vram tinyint,
cost int
CHECK (cost > 0),
CHECK (vram > 0)
);

CREATE TABLE ram(
id_r int primary key auto_increment,
model varchar(50) NOT NULL,
capacity tinyint NOT NULL,
freq smallint NOT NULL,
cost int
CHECK (capacity > 0),
CHECK (freq > 0),
CHECK (cost > 0)
);

CREATE TABLE drive(
id_dr int primary key auto_increment,
model varchar(50) NOT NULL,
capacity smallint NOT NULL,
cost int
CHECK (cost > 0),
CHECK (capacity > 0)
);

CREATE TABLE room(
id_room int primary key auto_increment,
adres VARCHAR(100) NOT NULL
);

CREATE TABLE keyboard(
id_k int primary key auto_increment,
model varchar(50) NOT NULL,
cost int
CHECK (cost > 0)
);

CREATE TABLE mouse(
id_m int primary key auto_increment,
model varchar(50) NOT NULL,
cost int
CHECK (cost > 0)
);

CREATE TABLE monitor(
id_mon int primary key auto_increment,
model varchar(50) NOT NULL,
width smallint,
height smallint,
freq smallint,
cost int
CHECK (cost > 0),
CHECK (height > 0),
CHECK (width > 0),
CHECK (freq > 0)
);

CREATE TABLE computer(
id_pc int primary key auto_increment,
cpu_id integer NOT NULL,
gpu_id integer NOT NULL,
dr_id1 integer NOT NULL,
dr_id2 integer,
ram1_id integer NOT NULL,
ram2_id integer,
kb_id integer NOT NULL,
m_id integer NOT NULL,
mon_id integer NOT NULL,
room_id integer,
assign_date DATE,
move_date DATE,
FOREIGN KEY (room_id) REFERENCES room(id_room),
FOREIGN KEY(cpu_id) REFERENCES pccpu(id_c), 
FOREIGN KEY(gpu_id) REFERENCES gpu(id_g),
FOREIGN KEY(dr_id1) REFERENCES drive(id_dr),
FOREIGN KEY(dr_id2) REFERENCES drive(id_dr),
FOREIGN KEY(ram1_id) REFERENCES ram(id_r),
FOREIGN KEY(ram2_id) REFERENCES ram(id_r),
FOREIGN KEY(m_id) REFERENCES mouse(id_m),
FOREIGN KEY(kb_id) REFERENCES keyboard(id_k),
FOREIGN KEY(mon_id) REFERENCES monitor(id_mon)
);




CREATE TABLE dolzhnost(
id_dol int primary key,
naz VARCHAR(20) NOT NULL,
pay int
CHECK (pay >= 0)
);

CREATE TABLE employee(
id_em int primary key auto_increment,
FIO VARCHAR(50) NOT NULL,
dolzh_id int,
FOREIGN KEY(dolzh_id) REFERENCES dolzhnost(id_dol)
);

CREATE TABLE assign(
em_id int NOT NULL,
room_id int NOT NULL,
FOREIGN KEY(em_id) REFERENCES employee(id_em),
FOREIGN KEY(room_id) REFERENCES room(id_room)
);

CREATE TABLE users(
login VARCHAR(50) NOT NULL,
pwd   VARCHAR(50) NOT NULL,
role  VARCHAR(3) NOT NULL DEFAULT "USR",
CHECK (role = "USR" OR role = "ADM" OR role = "MNG")
);

ALTER TABLE computer ADD state VARCHAR(20) NOT NULL DEFAULT "Хорошее";
ALTER TABLE computer ADD check(state IN ("Хорошее","Удовлетворительное","Критическое"));
SELECT * from computer c WHERE room_id is NULL; 
UPDATE computer SET state = "Удовлетворительное" WHERE id_pc IN (133,135,137,33,66,55,90,10,22,100,60,65);
UPDATE computer SET state = "Критическое" WHERE id_pc IN (133,10,15,9);

