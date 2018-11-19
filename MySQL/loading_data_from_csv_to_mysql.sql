
#Load data into votes table

Truncate Table `votes`;
SET foreign_key_checks = 0;
LOAD DATA LOCAL INFILE 'C:\\SO_DATA\\A_Votes\\A_Votes'
INTO TABLE `votes` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostId,VoteTypeId,UserId,CreationDate,BountyAmount);
SET foreign_key_checks = 1;