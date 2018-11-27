USE `sotorrent18_09`;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\Users.xml\\Users.xml'
INTO TABLE `Users`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\Badges.xml\\Badges.xml'
INTO TABLE `Badges`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\Posts.xml\\Posts.xml'
INTO TABLE `Posts`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\Comments.xml\\Comments.xml'
INTO TABLE `Comments`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\PostHistory.xml\\PostHistory.xml'
INTO TABLE `PostHistory`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\PostLinks.xml\\PostLinks.xml'
INTO TABLE `PostLinks`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\Tags.xml\\Tags.xml'
INTO TABLE `Tags`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;

SET foreign_key_checks = 0;
LOAD XML LOCAL INFILE 'E:\\SO_DB_dump\\Votes.xml\\Votes.xml'
INTO TABLE `Votes`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;