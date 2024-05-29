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
VALUES("Corsair Vengeance LPX DDR4",8,3200,2000),("Corsair Vengeance LPX DDR4",16,3200,3800)
,("G.SKILL Trident Z DDR4",16,3200,3600),("G.SKILL Trident Z DDR4",8,2666,1800)
,("Corsair Vengeance RGB PRO DDR4",32,3100,6000);