DROP DATABASE IF EXISTS  computer_db;
CREATE DATABASE IF NOT EXISTS computer_db;
USE computer_db;

CREATE TABLE pccpu(
id_c int primary key auto_increment,
model varchar(30),
freq smallint,
cores tinyint,
cost int
CHECK (cost >= 0)
);

CREATE TABLE gpu(
id_g int primary key auto_increment,
model varchar(30),
vram tinyint,
cost int
CHECK (cost >= 0)
);

CREATE TABLE ram(
id_r int primary key auto_increment,
model varchar(30),
capacity tinyint,
freq smallint,
cost int
CHECK (cost >= 0)
);

CREATE TABLE drive(
id_dr int primary key auto_increment,
model varchar(30),
capacity smallint,
cost int
CHECK (cost >= 0)
);

CREATE TABLE room(
id_room int primary key auto_increment,
adres VARCHAR(100)
);

CREATE TABLE computer(
id_pc int primary key auto_increment,
cpu_id integer NOT NULL,
gpu_id integer NOT NULL,
dr_id1 integer NOT NULL,
dr_id2 integer,
ram1_id integer NOT NULL,
ram2_id integer,
room_id integer,
assign_date DATE,
move_date DATE,
FOREIGN KEY (room_id) REFERENCES room(id_room),
FOREIGN KEY(cpu_id) REFERENCES pccpu(id_c), 
FOREIGN KEY(gpu_id) REFERENCES gpu(id_g),
FOREIGN KEY(dr_id1) REFERENCES drive(id_dr),
FOREIGN KEY(dr_id2) REFERENCES drive(id_dr),
FOREIGN KEY(ram1_id) REFERENCES ram(id_r),
FOREIGN KEY(ram2_id) REFERENCES ram(id_r)
);




CREATE TABLE dolzhnost(
id_dol int primary key,
naz VARCHAR(20),
pay smallint
CHECK (pay >= 0)
);

CREATE TABLE employee(
id_em int primary key auto_increment,
FIO VARCHAR(50),
dolzh_id int,
FOREIGN KEY(dolzh_id) REFERENCES dolzhnost(id_dol)
);

CREATE TABLE assign(
em_id int,
room_id int,
FOREIGN KEY(em_id) REFERENCES employee(id_em),
FOREIGN KEY(room_id) REFERENCES room(id_room)
);

CREATE TABLE users(
login VARCHAR(50) NOT NULL,
pwd   VARCHAR(50) NOT NULL,
role  VARCHAR(3) NOT NULL,
CHECK (role = "USR" OR role = "ADM" OR role = "MNG")
)