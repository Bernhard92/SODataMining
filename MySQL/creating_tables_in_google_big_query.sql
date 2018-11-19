
#retrieving data for Users table
SELECT * FROM [sotorrent-org:2018_09_23.Users] 

#retrieving data for Badges table
SELECT * FROM [sotorrent-org:2018_09_23.Badges]

#creating new posts table
SELECT * FROM [sotorrent-org:2018_09_23.Posts]
WHERE Tags like "%<android>%"

#retrieving Comments table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.Comments]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

#retrieving CommentUrl table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.CommentUrl]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

#retrieving PostHistory table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.PostHistory]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

#retrieving Votes table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.Votes]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

##retrieving TitleVersion table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.TitleVersion]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )
            
#retrieving PostVersion table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.PostVersion]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

#retrieving PostVersionUrl table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.PostVersionUrl]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

#retrieving PostBlockVersion table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.PostBlockVersion]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )

#retrieving PostBlockDiff table from new Post table
SELECT * 
FROM [sotorrent-org:2018_09_23.PostBlockDiff]
WHERE PostId IN 
            (SELECT Id 
             FROM [united-electron-222412:so_torrent_android.A_Posts]
             )