USE sotorrent18_09;

CREATE TABLE postblockevolution(
Id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
PostHistoryId TINYINT(4) NOT NULL,
ChangeType VARCHAR(30) NOT NULL,
PostBlockId INT(11),
PredPostBlockId INT(11),
ValueOld FLOAT(11), 
ValueNew FLOAT(11)
); 


CREATE TABLE posthistoryevolution(
Id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
ChangeType VARCHAR(30) NOT NULL,
PostHistoryId INT(11),
PredPostHistoryId INT(11),
ValueOld FLOAT(11), 
ValueNew FLOAT(11)
);