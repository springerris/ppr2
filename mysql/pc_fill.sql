use computer_db;

INSERT INTO pccpu(model,freq,cores,cost) 
VALUES("Ryzen 5 5600G",4000 ,12 ,18000),("Core i9-14900K",5000 ,24 ,25000)
,("Ryzen 5 1600",3200 ,6 ,12000),("Ryzen 5 5500U",2100,6 ,11000),
("Core i5-12400F",2600,6 ,16000);
 
INSERT INTO gpu(model,vram,cost) 
VALUES("GeForce RTX 4090",24,150000),("GeForce RTX 4060",8,45000)
,("GeForce RTX 3060 12 GB",12,30000),("GeForce RTX 4070 SUPER",12,70000)
,("Radeon RX 580",8,10000),("Radeon RX 6600",8,25000);

INSERT INTO drive(model,capacity,cost)
VALUES("Samsung 980 PRO",1000 ,12000),("Samsung 980 PRO",500 ,7000)
,("Western Digital SN850X",2000 ,17000),("Western Digital SN850X",1000 ,9000),
("Kingston A400 (Micron B17A)",1000 ,6000),("Samsung 870 EVO (V-NAND V6 512Gb)",1000 ,10000);

INSERT INTO ram(model,capacity,freq,cost)
VALUES("Corsair Vengeance LPX DDR4 8GB",8,3200,2000),("Corsair Vengeance LPX DDR4 16GB",16,3200,3800)
,("G.SKILL Trident Z DDR4 16GB",16,3200,3600),("G.SKILL Trident Z DDR4 8GB",8,2666,1800)
,("Corsair Vengeance RGB PRO DDR4 32GB",32,3100,6000);

INSERT INTO dolzhnost(id_dol,naz,pay) VALUES(4,"Уборщик",18000),(3,"Обслуживающий",30000),
(2,"Помошник админ.",45000),(1,"Администратор",60000);

INSERT INTO employee(FIO,dolzh_id) VALUES('Сергеевна О. Н.',1),
('Тихон П. В.',3),('Лидия М. В.',3),
('Никифоровна П. Г.',3),('Андрей З. В.',1),
('Анжелика М. Б.',4),('Татьяна Р. Т.',3),
('Марина М. П.',3),('Владимировна В. А.',3),
('Анатольевич А. Г.',2),('Анатольевич А. Б.',3),
('Святославовна А. Ф.',2),('Михайловна А. О.',3),
('Галактион С. М.',1),('Порфирий Н. Г.',4),
('София Г. В.',1),('Флорентин Б. Е.',2),
('Федосьевич Ю. Н.',2),('Леоновна И. К.',4),
('Фаина Е. И.',3),('Остап В. Б.',1),
('Мироновна Н. М.',3),('Власович Е. Б.',3),
('Геннадиевна Е. Т.',3),('Акулина Б. В.',2),
('Ангелина Б. А.',4),('Аполлинарий О. Г.',4),
('Федоровна Н. К.',2),('Руслановна А. Д.',3),
('Савва Т. Е.',2),('Ия С. С.',3),
('Александра Ф. Л.',3),('Сидор З. И.',2),
('Наркис К. Т.',1),('Филатович А. С.',1),
('Дмитриевна И. С.',3),('Михайловна Ю. Р.',4),
('Валентинович Т. Б.',1),('Елена П. К.',1),
('Родион С. Т.',2),('Валерьянович О. Е.',3),
('Юльевна Е. С.',3),('Людмила Ш. О.',3),
('Адрианович У. З.',2),('София Щ. К.',2),
('Герман Х. Е.',2),('Макаровна А. Д.',4),
('Афанасьевна М. К.',2),('Станимир П. З.',2),
('Макаровна Л. К.',2);

INSERT INTO room(adres) VALUES("Орловская область, город Шатура, наб. Будапештсткая, 55"),("Магаданская область, город Домодедово, бульвар Балканская, 20"),
("Магаданская область, город Люберцы, шоссе Косиора, 08"),
("Челябинская область, город Лотошино, въезд Будапештсткая, 75"),
("юменская область, город Ступино, въезд Гоголя, 48"),("Тверская область, город Мытищи, пр. Гоголя, 76"),
("Липецкая область, город Раменское, пр. Космонавтов, 88"),("Магаданская область, город Видное, проезд Бухарестская, 25");

INSERT INTO assign(room_id,em_id) VALUES(1,12),(1,1),(1,3),(1,33),(1,18),
(2,30),(2,40),(2,45),(2,25),(2,14),(2,26),
(3,32),(3,3),(3,19),(3,20),(3,31),(3,28),(3,46),
(4,48),(4,39),(4,2),(4,29),
(5,22),(5,17),(5,40),(5,14),(5,19),(5,49),(5,34),(5,4),
(6,48),(6,32),(6,19),(6,16),
(7,27),(7,47),(7,43),(7,18),(7,8),
(8,34),(8,32),(8,33),(8,5),(8,9);

INSERT INTO keyboard(model,cost) VALUES("Razor SUPER GAMING",10000),("ACES",7000),("Bloody",9000);

INSERT INTO mouse(model,cost) VALUES("CATZ",6000),("Mikey PRO",5000),("ACES",5500);

INSERT INTO monitor(model,height,width,freq,cost) VALUES("SAMSUNG HD MONITOR K10",1080,1920,165,9000),
("ASUS 2K GAMING",1440,2560,120,14000),("LG 4K UHD L004",2160,3840,60,25000);

TRUNCATE TABLE computer;
INSERT INTO computer(cpu_id,gpu_id,dr_id1,dr_id2,ram1_id,ram2_id,m_id,kb_id,mon_id,room_id,assign_date,move_date) VALUES(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),
(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),
(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),
(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),
(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),
(5,6,1,NULL,3,3,3,2,3,7,'2024-04-04','2024-06-03'),(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),
(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),
(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),
(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),
(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),
(3,6,1,NULL,4,NULL,2,1,1,5,'2023-10-10','2024-06-03'),(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),
(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),
(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),
(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),
(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),
(4,3,6,NULL,1,NULL,1,3,3,1,'2024-04-04','2024-06-03'),(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),
(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),
(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),
(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),
(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),
(3,4,4,4,4,4,1,2,2,7,'2024-04-04','2024-06-03'),(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),
(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),
(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),
(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),
(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),
(3,4,2,2,2,2,1,2,3,2,'2024-01-01','2024-06-03'),(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),
(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),
(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),
(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),
(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),
(2,4,2,NULL,4,NULL,3,1,2,6,'2023-10-10','2024-06-03'),(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),
(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),
(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),
(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),
(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),
(3,6,1,NULL,2,NULL,2,1,3,4,'2024-04-04','2024-06-03'),(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),
(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),
(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),
(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),
(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),
(3,6,2,NULL,2,NULL,3,2,1,3,'2024-01-01','2024-06-03'),(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),
(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),
(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),
(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),
(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),
(2,2,2,NULL,3,3,1,3,3,4,'2024-01-01','2024-06-03'),(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),
(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),
(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),
(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),
(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),
(1,1,6,6,2,NULL,1,3,3,3,'2024-04-04','2024-06-03'),(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),
(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),
(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),
(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),
(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),
(1,4,6,NULL,1,NULL,1,1,1,5,'2024-01-01','2024-06-03'),(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),
(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),
(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),
(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),
(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),
(2,5,4,NULL,1,1,3,3,1,4,'2023-10-10','2024-06-03'),(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),
(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),
(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),
(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),
(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),
(5,1,6,NULL,2,2,1,1,1,8,'2023-10-10','2024-06-03'),(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),
(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),
(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),
(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),
(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),
(3,4,6,NULL,4,NULL,2,1,1,NULL,'2024-01-01',NULL),(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),
(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),
(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),
(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),
(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),
(3,4,5,5,2,2,3,1,1,7,'2024-04-04','2024-06-03'),(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),
(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),
(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),
(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),
(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),
(3,2,6,6,3,3,2,3,2,2,'2023-10-10','2024-06-03'),(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,6,6,1,1,1,1,1,8,'2024-04-04','2024-06-03'),(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),
(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),
(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),
(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),
(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),
(2,1,5,NULL,4,NULL,2,2,3,4,'2024-01-01','2024-06-03'),(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),
(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),
(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),
(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),
(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),
(5,4,3,3,2,NULL,3,1,3,1,'2023-10-10','2024-06-03'),(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),
(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),
(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),
(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),
(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),
(1,2,4,4,1,1,1,2,1,8,'2024-04-04','2024-06-03'),(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),
(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),
(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),
(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),
(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),
(3,3,6,NULL,3,3,1,1,3,2,'2023-10-10','2024-06-03'),(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),
(4,1,5,NULL,5,NULL,1,1,1,8,'2024-04-04','2024-06-03'),(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),
(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),
(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),
(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),
(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),
(5,4,4,NULL,2,2,2,1,1,3,'2024-04-04','2024-06-03'),(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),
(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),
(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),
(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),
(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),
(4,4,3,NULL,3,3,1,1,3,8,'2024-01-01','2024-06-03'),(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),
(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),
(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),
(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),
(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),
(1,2,1,NULL,4,4,1,2,2,1,'2024-01-01','2024-06-03'),(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),
(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),
(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),
(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),
(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),
(4,4,1,1,2,2,3,2,1,1,'2024-04-04','2024-06-03'),(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),
(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),
(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),
(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),
(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),
(1,4,3,3,4,NULL,3,3,2,2,'2024-01-01','2024-06-03'),(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),
(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),
(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),
(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),
(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),
(2,3,6,NULL,5,NULL,1,3,1,2,'2024-04-04','2024-06-03'),
(1,3,4,4,2,2,1,1,3,1,'2024-01-01','2024-06-03');

SELECT * FROM employee;
SELECT * FROM computer;
SELECT pccpu.model, g.model, d.model, r.model, k.model, m.model, mon.model,assign_date,move_date FROM computer
INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
INNER JOIN gpu g  ON g.id_g = computer.gpu_id
INNER JOIN ram r  ON r.id_r  = computer.ram1_id
INNER JOIN drive d ON d.id_dr = computer.dr_id1
INNER JOIN keyboard k ON k.id_k = computer.kb_id 
INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
INNER JOIN mouse m ON m.id_m = computer.m_id;

SELECT sum(pccpu.cost),sum(g.cost),sum(r.cost),sum(d.cost),sum(k.cost),sum(mon.cost),sum(m.cost)
FROM computer
INNER JOIN pccpu ON pccpu.id_c = computer.cpu_id 
INNER JOIN gpu g  ON g.id_g = computer.gpu_id
INNER JOIN ram r  ON r.id_r  = computer.ram1_id
INNER JOIN drive d ON d.id_dr = computer.dr_id1
INNER JOIN keyboard k ON k.id_k = computer.kb_id 
INNER JOIN monitor mon ON mon.id_mon  = computer.mon_id 
INNER JOIN mouse m ON m.id_m = computer.m_id;

SELECT DISTINCT capacity FROM ram WHERE model = 'Corsair Vengeance LPX DDR4'

SELECT fio,naz FROM employee e 
INNER JOIN assign a ON a.em_id = e.id_em 
INNER JOIN room r ON r.id_room = a.room_id 
INNER JOIN dolzhnost d ON d.id_dol = e.dolzh_id 
WHERE room_id = 1



