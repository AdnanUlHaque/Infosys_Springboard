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


