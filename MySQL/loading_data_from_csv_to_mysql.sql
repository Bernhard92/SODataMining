#Load data into badges table

Truncate Table `badges`;
SET foreign_key_checks = 0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Badges\\A_Badges_000000000000'
INTO TABLE `badges` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,UserId,Name,Date,Class,TagBased);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Badges\\A_Badges_000000000001'
INTO TABLE `badges` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,UserId,Name,Date,Class,TagBased);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Badges\\A_Badges_000000000002'
INTO TABLE `badges` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,UserId,Name,Date,Class,TagBased);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Badges\\A_Badges_000000000003'
INTO TABLE `badges` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,UserId,Name,Date,Class,TagBased);
SET foreign_key_checks = 1;


#Load data into comments table

Truncate Table `comments`;
SET foreign_key_checks = 0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Comments\\A_Comments'
INTO TABLE `comments` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostId,Score,Text,CreationDate,UserDisplayName,UserId);
SET foreign_key_checks = 1;


#Load data into posthistory table

Truncate Table `posthistory`;
SET foreign_key_checks = 0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000000'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000001'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000002'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000003'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000004'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000005'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000006'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000007'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000008'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000009'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000010'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000011'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000012'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_PostHistory\\A_PostHistory_000000000013'
INTO TABLE `posthistory` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostHistoryTypeId,PostId,RevisionGUID,CreationDate,UserId,UserDisplayName,Comment,Text);
SET foreign_key_checks = 1;


#Load data into posts table

Truncate Table `posts`;
SET foreign_key_checks = 0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000000'
INTO TABLE `posts` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,DeletionDate,Score,ViewCount,
	Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,LastEditorDisplayName,LastEditDate,
	LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000001'
INTO TABLE `posts` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,DeletionDate,Score,ViewCount,
	Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,LastEditorDisplayName,LastEditDate,
	LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000002'
INTO TABLE `posts` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,DeletionDate,Score,ViewCount,
	Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,LastEditorDisplayName,LastEditDate,
	LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000003'
INTO TABLE `posts` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,DeletionDate,Score,ViewCount,
	Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,LastEditorDisplayName,LastEditDate,
	LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000004'
INTO TABLE `posts` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,DeletionDate,Score,ViewCount,
	Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,LastEditorDisplayName,LastEditDate,
	LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000005'
INTO TABLE `posts` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,AcceptedAnswerId,ParentId,CreationDate,DeletionDate,Score,ViewCount,
	Body,OwnerUserId,OwnerDisplayName,LastEditorUserId,LastEditorDisplayName,LastEditDate,
	LastActivityDate,Title,Tags,AnswerCount,CommentCount,FavoriteCount,ClosedDate,CommunityOwnedDate);
SET foreign_key_checks = 1;


#Load data into users table

Truncate Table `users`;
SET foreign_key_checks = 0;
LOAD XML INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Votes\\A_Votes'
INTO TABLE `users`
ROWS IDENTIFIED BY '<row>';
SET foreign_key_checks = 1;


#Load data into votes table

Truncate Table `votes`;
SET foreign_key_checks = 0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Votes\\A_Votes'
INTO TABLE `votes` 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostId,VoteTypeId,UserId,CreationDate,BountyAmount);
SET foreign_key_checks = 1;















#Load data into posts table

Truncate Table `posts`;
SET foreign_key_checks = 0;
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000000'
INTO TABLE `posts` 
FIELDS TERMINATED BY '","' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,@AcceptedAnswerId,@ParentId,CreationDate,@DeletionDate,Score,ViewCount,
	Body,@OwnerUserId,OwnerDisplayName,@LastEditorUserId,@LastEditorDisplayName,@LastEditDate,
	LastActivityDate,Title,Tags,@AnswerCount,@CommentCount,@FavoriteCount,@ClosedDate,@CommunityOwnedDate)
SET
AcceptedAnswerId = nullif(@AcceptedAnswerId,''),
ParentId = nullif(@ParentId,''),
DeletionDate = nullif(@DeletionDate,''),
OwnerUserId = nullif(@OwnerUserId,''),
LastEditorUserId = nullif(@LastEditorUserId,''),
LastEditorDisplayName = nullif(@LastEditorDisplayName,''),
LastEditDate = nullif(@LastEditDate,''),
AnswerCount = nullif(@AnswerCount,''),
CommentCount = nullif(@CommentCount,''),
FavoriteCount = nullif(@FavoriteCount,''),
ClosedDate = nullif(@ClosedDate,''),
CommunityOwnedDate = nullif(@CommunityOwnedDate,'');

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000001'
INTO TABLE `posts` 
FIELDS TERMINATED BY '","' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,@AcceptedAnswerId,@ParentId,CreationDate,@DeletionDate,Score,ViewCount,
	Body,@OwnerUserId,OwnerDisplayName,@LastEditorUserId,@LastEditorDisplayName,@LastEditDate,
	LastActivityDate,Title,Tags,@AnswerCount,@CommentCount,@FavoriteCount,@ClosedDate,@CommunityOwnedDate)
SET
AcceptedAnswerId = nullif(@AcceptedAnswerId,''),
ParentId = nullif(@ParentId,''),
DeletionDate = nullif(@DeletionDate,''),
OwnerUserId = nullif(@OwnerUserId,''),
LastEditorUserId = nullif(@LastEditorUserId,''),
LastEditorDisplayName = nullif(@LastEditorDisplayName,''),
LastEditDate = nullif(@LastEditDate,''),
AnswerCount = nullif(@AnswerCount,''),
CommentCount = nullif(@CommentCount,''),
FavoriteCount = nullif(@FavoriteCount,''),
ClosedDate = nullif(@ClosedDate,''),
CommunityOwnedDate = nullif(@CommunityOwnedDate,'');

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000002'
INTO TABLE `posts` 
FIELDS TERMINATED BY '","' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,@AcceptedAnswerId,@ParentId,CreationDate,@DeletionDate,Score,ViewCount,
	Body,@OwnerUserId,OwnerDisplayName,@LastEditorUserId,@LastEditorDisplayName,@LastEditDate,
	LastActivityDate,Title,Tags,@AnswerCount,@CommentCount,@FavoriteCount,@ClosedDate,@CommunityOwnedDate)
SET
AcceptedAnswerId = nullif(@AcceptedAnswerId,''),
ParentId = nullif(@ParentId,''),
DeletionDate = nullif(@DeletionDate,''),
OwnerUserId = nullif(@OwnerUserId,''),
LastEditorUserId = nullif(@LastEditorUserId,''),
LastEditorDisplayName = nullif(@LastEditorDisplayName,''),
LastEditDate = nullif(@LastEditDate,''),
AnswerCount = nullif(@AnswerCount,''),
CommentCount = nullif(@CommentCount,''),
FavoriteCount = nullif(@FavoriteCount,''),
ClosedDate = nullif(@ClosedDate,''),
CommunityOwnedDate = nullif(@CommunityOwnedDate,'');


LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000003'
INTO TABLE `posts` 
FIELDS TERMINATED BY '","' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,@AcceptedAnswerId,@ParentId,CreationDate,@DeletionDate,Score,ViewCount,
	Body,@OwnerUserId,OwnerDisplayName,@LastEditorUserId,@LastEditorDisplayName,@LastEditDate,
	LastActivityDate,Title,Tags,@AnswerCount,@CommentCount,@FavoriteCount,@ClosedDate,@CommunityOwnedDate)
SET
AcceptedAnswerId = nullif(@AcceptedAnswerId,''),
ParentId = nullif(@ParentId,''),
DeletionDate = nullif(@DeletionDate,''),
OwnerUserId = nullif(@OwnerUserId,''),
LastEditorUserId = nullif(@LastEditorUserId,''),
LastEditorDisplayName = nullif(@LastEditorDisplayName,''),
LastEditDate = nullif(@LastEditDate,''),
AnswerCount = nullif(@AnswerCount,''),
CommentCount = nullif(@CommentCount,''),
FavoriteCount = nullif(@FavoriteCount,''),
ClosedDate = nullif(@ClosedDate,''),
CommunityOwnedDate = nullif(@CommunityOwnedDate,'');

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000004'
INTO TABLE `posts` 
FIELDS TERMINATED BY '","'
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,@AcceptedAnswerId,@ParentId,CreationDate,@DeletionDate,Score,ViewCount,
	Body,@OwnerUserId,OwnerDisplayName,@LastEditorUserId,@LastEditorDisplayName,@LastEditDate,
	LastActivityDate,Title,Tags,@AnswerCount,@CommentCount,@FavoriteCount,@ClosedDate,@CommunityOwnedDate)
SET
AcceptedAnswerId = nullif(@AcceptedAnswerId,''),
ParentId = nullif(@ParentId,''),
DeletionDate = nullif(@DeletionDate,''),
OwnerUserId = nullif(@OwnerUserId,''),
LastEditorUserId = nullif(@LastEditorUserId,''),
LastEditorDisplayName = nullif(@LastEditorDisplayName,''),
LastEditDate = nullif(@LastEditDate,''),
AnswerCount = nullif(@AnswerCount,''),
CommentCount = nullif(@CommentCount,''),
FavoriteCount = nullif(@FavoriteCount,''),
ClosedDate = nullif(@ClosedDate,''),
CommunityOwnedDate = nullif(@CommunityOwnedDate,'');

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\SO_DATA\\A_Posts\\A_Posts_000000000005'
INTO TABLE `posts` 
FIELDS TERMINATED BY '","' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
(Id,PostTypeId,@AcceptedAnswerId,@ParentId,CreationDate,@DeletionDate,Score,ViewCount,
	Body,@OwnerUserId,OwnerDisplayName,@LastEditorUserId,@LastEditorDisplayName,@LastEditDate,
	LastActivityDate,Title,Tags,@AnswerCount,@CommentCount,@FavoriteCount,@ClosedDate,@CommunityOwnedDate)
SET
AcceptedAnswerId = nullif(@AcceptedAnswerId,''),
ParentId = nullif(@ParentId,''),
DeletionDate = nullif(@DeletionDate,''),
OwnerUserId = nullif(@OwnerUserId,''),
LastEditorUserId = nullif(@LastEditorUserId,''),
LastEditorDisplayName = nullif(@LastEditorDisplayName,''),
LastEditDate = nullif(@LastEditDate,''),
AnswerCount = nullif(@AnswerCount,''),
CommentCount = nullif(@CommentCount,''),
FavoriteCount = nullif(@FavoriteCount,''),
ClosedDate = nullif(@ClosedDate,''),
CommunityOwnedDate = nullif(@CommunityOwnedDate,'');
SET foreign_key_checks = 1;