USE python_db;

ALTER TABLE `posts` 
ADD COLUMN `kincaid` 				FLOAT(10),
ADD COLUMN `ari` 					FLOAT(10) AFTER `kincaid`,
ADD COLUMN `coleman_liau` 			FLOAT(10) AFTER `ari`,
ADD COLUMN `flesch_reading_ease` 	FLOAT(10) AFTER `coleman_liau`,
ADD COLUMN `gunning_fog_index` 		FLOAT(10) AFTER `flesch_reading_ease`,  
ADD COLUMN `smog_index` 			FLOAT(10) AFTER `gunning_fog_index`, 
ADD COLUMN `dale_chall` 			FLOAT(10) AFTER `smog_index`; 