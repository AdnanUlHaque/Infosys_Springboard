#ex1
CREATE TABLE Player (
  PId INTEGER PRIMARY KEY,
  PName VARCHAR2(20) NOT NULL,
  Ranking INTEGER
);


#ex2
CREATE TABLE Tournament (
  TId INTEGER PRIMARY KEY,
  TName VARCHAR2(30) NOT NULL,
  StartDt DATE NOT NULL,
  EndDt DATE NOT NULL,
  Prize INTEGER NOT NULL
);


#ex3
CREATE TABLE Match(
MId INTEGER ,
TId INTEGER CONSTRAINT match_tid_fk REFERENCES Tournament(TId),
Player1 INTEGER CONSTRAINT match_player1_fk REFERENCES Player(PId),
Player2 INTEGER CONSTRAINT match_player2_fk REFERENCES Player(PId),
MatchDt DATE NOT NULL,
Winner INTEGER CONSTRAINT match_winner_fk REFERENCES Player(PId),
Score VARCHAR2(30) NOT NULL,
CONSTRAINT match_mid_pk PRIMARY KEY(MId,TId),
CONSTRAINT match_player_ck CHECK(Player1<>Player2)
);


#ex4
ALTER TABLE Player ADD (MatchesPlayed NUMBER,MatchesWon NUMBER)


#ex7
ALTER TABLE Player DROP (ContactNo)

#ex8
ALTER TABLE Player RENAME COLUMN PId TO PlayerId

#ex9
ALTER TABLE Player MODIFY PName VARCHAR2(50)


#ex10
INSERT INTO Salesman (SId, SName, Location)
VALUES (11, 'Elizabeth', 'London');


#ex11
INSERT INTO Product (ProdId, PDesc, Price, Category, Discount)
VALUES (110, 'Bat', 50, 'Sports', NULL);


#ex12
SELECT Prodid, Pdesc, Price, Category, Discount
FROM Product;


#ex13
SELECT Prodid, Price, Category
FROM Product;


#ex14
SELECT DISTINCT Category
FROM Product;


#ex7
SELECT Prodid, Pdesc, Category, Discount
FROM Product
WHERE Category = 'Apparel';


#ex8
SELECT Prodid, Pdesc, Category, Discount
FROM Product
WHERE Pdesc IS NULL;


#ex9
SELECT Prodid, Pdesc, Category, Discount
FROM Product
WHERE Category = 'Apparel' AND Discount > 5;


#colass2
CREATE TABLE Shopper (
  Shopperid NUMBER PRIMARY KEY,
  ShopperName VARCHAR2(20) NOT NULL,
  Gender CHAR(6) CHECK (Gender IN ('Male', 'Female')),
  MobileNo NUMBER NOT NULL,
  Address VARCHAR2(50)
);


#colass3
ALTER TABLE Shopper MODIFY MobileNo VARCHAR2(15)


#ass1
CREATE TABLE Article(
ArCode CHAR(5) PRIMARY KEY  CHECK(ArCode LIKE 'A%'),
ArName VARCHAR2(30) NOT NULL,
RATE NUMBER(8,2),
Quantity NUMBER(4) DEFAULT 0 CHECK(Quantity>=0),
Class CHAR(1) CHECK(Class IN('A','B','C'))
)


#ass5
CREATE TABLE Store(
Name VARCHAR2(20) PRIMARY KEY,
Location VARCHAR2(30) NOT NULL,
ManagerName VARCHAR2(30) UNIQUE
)


#ass6
ALTER TABLE Store RENAME COLUMN Name TO StoreName


#ass7
CREATE TABLE Bill(
BillNo NUMBER PRIMARY KEY,
StoreName VARCHAR2(20) REFERENCES Store(StoreName),
ShopperId NUMBER REFERENCES Shopper(ShopperId),
Arcode CHAR(5) REFERENCES Article(ArCode),
Amount NUMBER,
BillDate DATE,
Quantity NUMBER(4) DEFAULT 1 CHECK(Quantity>0)
)

#ass8
CREATE TABLE Supplier(
SupplierId VARCHAR2(6) PRIMARY KEY,
Name VARCHAR2(30),
ContactNo VARCHAR2(15) NOT NULL,
EmailId VARCHAR2(30)
)


#ass9
ALTER TABLE Supplier ADD City VARCHAR2(10);


#ass10
ALTER TABLE Supplier DROP COLUMN Emailid;


#ass11
CREATE TABLE City (
  City VARCHAR2(20) UNIQUE
);

#ass12
ALTER TABLE City DROP COLUMN City;


#ass13
CREATE TABLE Address (
  HouseNo NUMBER PRIMARY KEY,
  Street VARCHAR2(30),
  City VARCHAR2(20),
  Zip NUMBER(6) CHECK (Zip >= 0),
  State VARCHAR2(5),
  FOREIGN KEY (City) REFERENCES City(City)
);


#ass14
ALTER TABLE Address MODIFY state VARCHAR2(20);



#ass15
INSERT INTO Shopper
(ShopperId, ShopperName, Gender, MobileNo, Address) 
VALUES 
(101, 'Mark Jane', 'Male', 1234567890, 'Allen Street, New York')


#ass2
INSERT INTO Article (ArCode, ArName, Rate, Quantity, Class)
VALUES ('A1001', 'Mouse', 500, 0, 'C');


#ass17
