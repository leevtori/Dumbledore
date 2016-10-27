INSERT INTO staff VALUES
('100','D','Doctor Who', 'jammydodger','ihatedaleks'),
('101','D','Dr.Doofenshmirtz', 'SQLinator','damnyouperry'),
('102','D','Dr.Elmer Hartman', 'askwebMD','1234'),
('103','D','Sheldon Cooper','physicsnerd','amy'),
('123','N','Meg Griffin', 'pinkhat','0000'),
('124','N','Sponge Bob','frycook','patties'),
('125','N','Patrick Star','icantseemyforehead','duuuh'),
('126','N','Eugene Krabs','moneeey','pennypincher'),
('127','N','Sandy Cheeks','acornmuncher','hiya'),
('200','A','Lois Griffin','ohpeter','password'),
('201','A','Amelia Pond','thegirlwhowaited','41625'),
('202','A','Rory Williams','iheartamy','46256'),
('203','A','River Song','spoilers','hellosweetie');

Insert Into patients VALUES
('10000', 'Dalek', '19-35', '1414 Edmonton, Alberta', '7801001000', '7809999966'),
('10001', 'Silence', '0-18', '1313 Edmonton, Alberta', '7801001001', '7809996666'),
('10002', 'Angel', '0-18', '1515 Edmonton, Alberta', '7801001002', '7806666999'),
('10003', 'Tardis', '36-60', '1616 Edmonton, Alberta', '7801001003', '7801111444'),
('10004', 'Melody Pond', '36-60', '1717 Edmonton, Alberta', '7801001004', '7804444111'),
('10005', 'Prisoner Zero', '0-18', '1818 Calgary, Alberta', '7801001005', '7804545131'),
('10006', 'Pandorica', '19-35', '1919 Calgary, Alberta', '7801001006', '7805555555'),
('10007', 'Silurian', '36-60', '1919 Calgary, Alberta', '7801001007', '7805555464');

INSERT INTO charts Values
('000','10000', '2010-10-02', '2010-10-16'),
('001','10001', '2010-06-06', '2010-06-17'),
('002','10002', '2010-02-22', '2010-03-16'),
('003','10003', '2011-01-16',NULL),
('004','10004', '2011-04-16',NULL),
('005','10005', '2011-06-16', '2012-07-05'),
('006','10006', '2011-06-16', '2012-01-01'),
('007','10007', '2011-12-24',NULL),
('008','10000', '2011-10-02', '2011-10-16'),
('009','10001', '2011-06-06',NULL);

INSERT INTO symptoms VALUES
('10000', '000','123', '2010-10-02','uncontrollable gas' ),
('10000', '008','124', '2011-10-03','stomachache' ),
('10001', '001','125', '2010-06-06','cough' ),
('10002', '002','125', '2010-02-28','headache' ),
('10004', '004','125', '2010-05-09','cough' ),
('10002', '002','125', '2010-02-25','diarrhea' ),
('10002', '002','100', '2010-02-25','stomachache' ),
('10003', '003','103', '2011-01-22','uncontrollable gas' ),
('10004', '004','123', '2011-04-25','uncontrollable gas' ),
('10005', '005','123', '2011-07-01','stomachache' ),
('10006', '006','125', '2011-06-16','diarrhea' ),
('10007', '007','124', '2011-12-27','uncontrollable gas' ),
('10007', '007','125', '2011-12-25','stomachache' );

INSERT INTO diagnoses VALUES
('10000','000','100','2010-10-03','cancer'),
('10001','001','101','2010-06-07','diabetes'),
('10002','002','103','2010-03-07','malaria'),
('10003','003','102','2011-01-25','worms'),
('10004','004','102','2011-04-26','cancer'),
('10005','005','100','2011-07-08','worms'),
('10006','006','103','2011-06-17','food poisoning');

INSERT INTO drugs VALUES 
('Aspirin', 'Pain killers'),
('Vicodin', 'Pain killers'),
('Ibuprofen', 'Pain killers'),
('Xanax', 'Tranquillizer'),
('Diazepan', 'Tranquillizer'),
('Hemp', 'Recreational'),
('Cocaine', 'Recreational');

INSERT INTO medications VALUES
('10000','000','100','2010-10-03','2010-10-03','2010-11-03',3,'Cocaine'),
('10001','001','102','2010-06-07','2010-06-07','2010-07-07',10,'Xanax'),
('10002','002','100','2010-03-07','2010-03-07','2010-04-07',300,'Ibuprofen'),
('10003','003','103','2011-01-25','2011-01-25','2011-01-30',1,'Hemp'),
('10004','004','102','2011-04-26','2011-04-26','2011-05-15',7,'Hemp'),
('10006','006','101','2011-06-17','2011-06-17','2011-06-20',50,'Aspirin'),
('10007','007','100','2011-01-20','2011-01-20','2011-01-25',25,'Vicodin'),
('10007','007','100','2011-02-20','2011-02-20','2011-02-26',50,'Vicodin'),
('10007','007','100','2011-03-20','2011-03-20','2011-03-27',100,'Vicodin');

INSERT INTO reportedallergies VALUES 
('10000','Vicodin'),
('10003','Diazepan'),
('10005','Aspirin');

INSERT INTO inferredallergies VALUES
('Vicodin','Ibuprofen'),
('Cocaine','Xanax');

INSERT INTO dosage VALUES
('Aspirin','0-18',2),
('Aspirin','19-35',4),
('Aspirin','36-60',4),
('Vicodin','0-18',1),
('Vicodin','19-35',2),
('Vicodin','36-60',3),
('Ibuprofen','0-18',2),
('Ibuprofen','19-35',4),
('Ibuprofen','36-60',5),
('Xanax', '0-18',1),
('Xanax', '19-35',2),
('Xanax', '36-60',2),
('Diazepan','0-18',3),
('Diazepan','19-35',5),
('Diazepan','36-60',10),
('Hemp','0-18',1),
('Hemp','19-35',3),
('Hemp','36-60',4),
('Cocaine','0-18',1),
('Cocaine','19-35',5),
('Cocaine','36-60',10);




