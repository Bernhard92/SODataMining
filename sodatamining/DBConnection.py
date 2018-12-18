'''
Created on 3 Nov 2018

@author: Bernhard
'''

import mysql.connector
from mysql.connector import Error


class DBConnection:
        
    def __init__(self, db_name="sotorrent18_09"):
        self.db_name = db_name
        self.conn = self.connect()
         
    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database=self.db_name,
                                           user='root',
                                           password=self.get_db_password())
            if conn.is_connected():
                print 'Connected to MySQL database'
            return conn
        except Error as e:
            print e 
            
    def store_readability_metrics(self, id_, table, metrics):
        """ Stores the calculated metrics directly in the given table """
        try:
            cursor = self.conn.cursor()
            query = """ UPDATE """ + table + """  
                        SET
                        `kincaid` = %s, 
                        `ari` = %s,
                        `coleman_liau` = %s, 
                        `flesch_reading_ease` = %s,
                        `gunning_fog_index` = %s,
                        `smog_index` = %s,
                        `dale_chall` = %s
                        WHERE `id` = %s; """
                            
            data = (
                metrics['readability grades']['Kincaid'],
                metrics['readability grades']['ARI'],
                metrics['readability grades']['Coleman-Liau'],
                metrics['readability grades']['FleschReadingEase'],
                metrics['readability grades']['GunningFogIndex'],
                metrics['readability grades']['SMOGIndex'],
                metrics['readability grades']['DaleChallIndex'],
                id_)
            
            cursor.execute(query, data)
            # accept the changes
            self.conn.commit()
            
        except Error as e:
            print e 
        
        finally:
            cursor.close()
        
    def get_number_of_entries(self, table):
        """ Gets number of posts in table """
        try: 
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM " + self.db_name + "." + table + ";")
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result
    
    """ 
        PostBlockVersion readability
    
    """

    def get_id_content_from_postblockversion(self):
        """ Gets the hole post entry form the posts table """
        try:
            query = """ SELECT id, content FROM 
                    """ + self.db_name + """.postblockversion
                    WHERE PostBlockTypeId = 1;
                    """
            
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
     
        except Error as e:
            print e
            
        finally:
            cursor.close()
            return result
    
    """
        posthistory readability
    
    """

    def get_ids_from_posthistory(self):
        """ returns the id attribute from table at the give position """
        
        query = """SELECT id 
                FROM posthistory
                order by id;"""
                
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result
            
        
    def get_content_from_posthistory(self, phId):
        query = """SELECT v.content
                FROM posthistory h, postblockversion v
                WHERE h.id = v.PostHistoryId
                AND v.PostBlockTypeId = 1
                AND h.id = """ + str(phId) + """;"""
        
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result
        
    """
        Post readability
        
    """
    
    def get_most_recent_score(self):
        """Gets the readability score of the most recent 
        posthistory entry"""
        
        query = """SELECT a.postid, a.kincaid, a.ari, 
                    a.coleman_liau, a.flesch_reading_ease, 
                    a.gunning_fog_index, a.smog_index, a.dale_chall
                FROM posthistory a
                WHERE a.PostHistoryTypeId IN (2, 5, 8)
                AND a.creationDate = 
                    (Select max(b.CreationDate)
                    FROM posthistory b 
                    WHERE b.postid = a.postid
                    AND PostHistoryTypeId IN (2, 5, 8)
                )
                GROUP BY postid;
                """
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result      
        
    """
        Post sentiment 
    
    """

    def store_sentiment(self, id_, table, sentiment):
        try:
            cursor = self.conn.cursor()
            query = """ UPDATE """ + table + """  
                        SET
                        `neg` = %s, 
                        `neu` = %s,
                        `pos` = %s, 
                        `compound` = %s
                        WHERE `id` = %s; """
                            
            data = (
                sentiment['neg'],
                sentiment['neu'],
                sentiment['pos'],
                sentiment['compound'],
                id_)
            
            cursor.execute(query, data)
            # accept the changes
            self.conn.commit()
            
        except Error as e:
            print e 
        
        finally:
            cursor.close()

    def get_most_recent_sentiment(self):
        """Gets the sentiment score of the most recent 
        posthistory entry"""
        
        query = """SELECT a.postid, a.neg, a.neu, 
                    a.pos, a.compound
                FROM posthistory a
                WHERE a.PostHistoryTypeId IN (2, 5, 8)
                AND a.creationDate = 
                    (Select max(b.CreationDate)
                    FROM posthistory b 
                    WHERE b.postid = a.postid
                    AND PostHistoryTypeId IN (2, 5, 8)
                )
                GROUP BY postid;
                """
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result     
        
    def get_comment_text(self):
        query = """SELECT id, text
                FROM comments;"""
            
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result 

    """
    Code Evolution
    
    """
    def get_posthistoryid_from_texttype(self):        
        query = """SELECT id 
                FROM posthistory
                WHERE posthistorytypeid IN (2,5,8)
                order by id;"""
                
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result
        
    def get_ids_from_postblockversion(self):
        query = """SELECT  a.id
                FROM postblockversion a, postblockversion b
                where a.postblocktypeid = 1
                and a.gunning_fog_index is not null
                and a.flesch_reading_ease is not null
                and a.PredPostBlockVersionId = b.Id
                and b.postblocktypeid = 1
                and b.gunning_fog_index is not null
                and b.flesch_reading_ease is not null
                order by id;
                """
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result 
    
    def get_postblock_value(self, id_):
        """gets the desired metrics from the entry 
        with the given id"""
        
        query = """SELECT posthistoryid, id, 
                        predpostblockversionid, 
                        flesch_reading_ease, 
                        gunning_fog_index, 
                        neg, neu, pos, compound 
                FROM postblockversion
                WHERE id = """ + str(id_)
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result 
        
    def get_posthistory_value(self, id_):
        """gets the desired metrics from the entry 
        with the given id"""
        
        query = """SELECT  null as placeholder, 
                        h.id, v.PredPostHistoryId,
                        h.flesch_reading_ease, h.gunning_fog_index, 
                        h.neg, h.neu, h.pos, h.compound
                    FROM posthistory h, postversion v
                    WHERE h.id = v.PosthistoryId
                    AND h.id = """ + str(id_)
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result 
        
    def get_predposthistory_value(self, id_):
        """gets the desired metrics from the entry 
        with the given id"""
        
        #I'm asking for the id twice because
        #i want to have the same structure as above
        query = """SELECT  null as placeholder, null as placeholder2,
                    id, flesch_reading_ease, 
                    gunning_fog_index, neg, neu, pos, compound
                    from posthistory
                    where id = """ + str(id_)
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            return result 
        
    def insert_postblockevolution_entry(self, values):
        
        query = """ INSERT INTO `sotorrent18_09`.`postblockevolution`
                (
                `PostHistoryId`,
                `ChangeType`,
                `PostBlockId`,
                `PredPostBlockId`,
                `ValueNew`,
                `ValueOld`)
                VALUES
                (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s);"""
                            
        data = (
            values['posthistoryid'], 
            values['changetype'],
            values['postblockid'],
            values['predpostblockid'],
            values['valuenew'],
            values['valueold']
            )
            
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query, data)
            # accept the changes
            self.conn.commit()
        except Error as e: 
            print e 
        finally:
            cursor.close()
            
    def insert_posthistoryevolution_entry(self, values):
        query = """ INSERT INTO `sotorrent18_09`.`posthistoryevolution`
                (
                `ChangeType`,
                `PostHistoryId`,
                `PredPostHistoryId`,
                `ValueNew`,
                `ValueOld`)
                VALUES
                (
                %s,
                %s,
                %s,
                %s,
                %s);"""
                            
        data = (
            values['changetype'],
            values['posthistoryid'],
            values['predposthistoryid'],
            values['valuenew'],
            values['valueold']
            )
            
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query, data)
            # accept the changes
            self.conn.commit()
        except Error as e: 
            print e 
        finally:
            cursor.close()
    
    """
    Posthistoryevolution analysis
    
    """
    
    def get_closed_posts_stats(self):
        """Count ocurence of changeTyps of closed posts"""
        query = """SELECT count(1), e.changeType
                FROM posthistoryevolution e, posts p, posthistory h
                WHERE e.PostHistoryId = h.Id
                AND h.PostId = p.id
                AND p.ClosedDate is not NULL 
                GROUP BY e.ChangeType"""
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result 
        
    def get_open_posts_stats(self):
        """Count ocurence of changeTyps of open posts"""
        query = """SELECT count(1), e.changeType
                FROM posthistoryevolution e, posts p, posthistory h
                WHERE e.PostHistoryId = h.Id
                AND h.PostId = p.id
                AND p.ClosedDate is NULL 
                GROUP BY e.ChangeType"""
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result 
        
    def get_not_accepted_posts_stats(self):
        """Count ocurence of changeTyps of closed posts"""
        query = """SELECT count(1), e.changeType
                FROM posthistoryevolution e, posts p, posthistory h
                WHERE e.PostHistoryId = h.Id
                AND h.PostId = p.id
                AND p.AcceptedAnswerId = 0
                GROUP BY e.ChangeType"""
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result 
        
    def get_accepted_posts_stats(self):
        """Count ocurence of changeTyps of open posts"""
        query = """SELECT count(1), e.changeType
                FROM posthistoryevolution e, posts p, posthistory h
                WHERE e.PostHistoryId = h.Id
                AND h.PostId = p.id
                AND p.AcceptedAnswerId != 0 
                GROUP BY e.ChangeType"""
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result 
        
    def list_of_evolution_steps(self):
        """returns postid and number of nodes in evolution table
        with the most evolution steps on top"""
        query = """select count(*), postid 
                from posthistory
                where PostHistoryTypeId in (2,5,8)
                group by PostId
                order by count(*) desc"""
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result 
        
    def list_of_closed_evolution_steps(self):
        """returns postid and number of nodes in evolution table
        with the most evolution steps depth on top"""
        query = """select count(*), h.postid 
                from posthistory h, posts p
                where h.PostHistoryTypeId in (2,5,8)
                and h.postid = p.id
                and p.ClosedDate is not null
                group by h.PostId
                order by count(*) desc
                """
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result
        
    def list_of_accepted_evolution_steps(self):
        """returns postid and number of nodes in evolution table
        with the most evolution steps depth on top"""
        query = """select count(*), h.postid 
                from posthistory h, posts p
                where h.PostHistoryTypeId in (2,5,8)
                and h.postid = p.id
                and p.AcceptedAnswerId != 0
                group by h.PostId
                order by count(*) desc
                """
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result
        
    def get_all_predecessors(self, pId):
        """gets all entries from posthistorytable order by creation date"""
        query = """select * 
                from posthistory
                where postid = """ + str(pId)+ """
                and PostHistoryTypeId in (2,5,8)
                order by CreationDate asc"""
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
        except Error as e: 
            print e 
        finally:
            return result 
        
    def get_closed_date(self, pId):
        query = """select closedDate
                from posts
                where id = """ + str(pId)
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            return result
        
    def get_post_with_id(self, pId):
        query = """select *
                from posts
                where id = """ + str(pId)
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            return result
    
    def get_answer_with_id(self, pId):
        query = """select *
                from acceptedanswers
                where id = """ + str(pId)
             
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
        except Error as e: 
            print e 
        finally:
            return result
    
    """
        Operational stuff
        
    """

    def close_connection(self):
        self.conn.close() 
        
    def get_db_password(self):
        log_in_file = open("../.login_data")
        return log_in_file.readline()
    
    def add_readability_columns(self, table):
        """Adds columns for readability metrics to existing posts table"""
        try:
            cursor = self.conn.cursor(); 
            query = """ ALTER TABLE """ + table + """ 
                        ADD COLUMN `kincaid`                 FLOAT(10),
                        ADD COLUMN `ari`                     FLOAT(10) AFTER `kincaid`,
                        ADD COLUMN `coleman_liau`             FLOAT(10) AFTER `ari`,
                        ADD COLUMN `flesch_reading_ease`     FLOAT(10) AFTER `coleman_liau`,
                        ADD COLUMN `gunning_fog_index`         FLOAT(10) AFTER `flesch_reading_ease`,  
                        ADD COLUMN `smog_index`             FLOAT(10) AFTER `gunning_fog_index`, 
                        ADD COLUMN `dale_chall`             FLOAT(10) AFTER `smog_index`; """
            cursor.execute(query)
            self.conn.commit()
        except Error as e:
            print e
        finally:
            cursor.close()
            
    def add_sentiment_columns(self, table):
        try:
            cursor = self.conn.cursor() 
            query = """ ALTER TABLE """ + table + """ 
                        ADD COLUMN `neg`        FLOAT(10),
                        ADD COLUMN `neu`        FLOAT(10) AFTER `neg`,
                        ADD COLUMN `pos`        FLOAT(10) AFTER `neu`,
                        ADD COLUMN `compound`   FLOAT(10) AFTER `pos`; """
            cursor.execute(query)
            self.conn.commit()
        except Error as e:
            print e
        finally:
            cursor.close()
            
            
    def create_indices(self):
        query = """USE `sotorrent18_09`;
        CREATE INDEX `comments_index_1` ON Comments(UserId);
        CREATE INDEX `comments_index_2` ON Comments(UserDisplayName);
        
        CREATE INDEX `post_history_index_1` ON PostHistory(UserId);
        CREATE INDEX `post_history_index_2` ON PostHistory(UserDisplayName);
        
        CREATE INDEX `posts_index_1` ON Posts(OwnerUserId);
        CREATE INDEX `posts_index_2` ON Posts(LastEditorUserId);
        CREATE INDEX `posts_index_3` ON Posts(OwnerDisplayName);
        
        CREATE INDEX `users_index_1` ON Users(DisplayName);
        
        ALTER TABLE `PostBlockDiff` ADD INDEX postblockdiff_index_1 (LocalId);
        ALTER TABLE `PostBlockDiff` ADD INDEX postblockdiff_index_2 (PredLocalId);
        
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_1 (LocalId);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_2 (PredLocalId);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_3 (RootLocalId);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_4 (PredSimilarity);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_5 (PredCount);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_6 (SuccCount);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_7 (Length);
        ALTER TABLE `PostBlockVersion` ADD INDEX postblockversion_index_8 (LineCount);
        
        ALTER TABLE `CommentUrl` ADD INDEX commenturl_index_1 (PostId);
        
        ALTER TABLE `PostReferenceGH` ADD INDEX postreferencegh_index_1 (FileId);
        ALTER TABLE `PostReferenceGH` ADD INDEX postreferencegh_index_2 (RepoName);
        ALTER TABLE `PostReferenceGH` ADD INDEX postreferencegh_index_3 (Branch);
        ALTER TABLE `PostReferenceGH` ADD INDEX postreferencegh_index_4 (FileExt);
        ALTER TABLE `PostReferenceGH` ADD INDEX postreferencegh_index_5 (Size);
        ALTER TABLE `PostReferenceGH` ADD INDEX postreferencegh_index_6 (Copies);
        
        ALTER TABLE `TitleVersion` ADD INDEX titleversion_index_1 (PredEditDistance);
        ALTER TABLE `TitleVersion` ADD INDEX titleversion_index_2 (SuccEditDistance);
        """
        try: 
            cursor = self.conn.cursor()
            cursor.execute(query)
        except Error as e: 
            print e 
        finally:
            cursor.close()
        
    def create_evolution_tables(self):
        # Open and read the file as a single buffer
        fd = open('../MySQL/create_evolution_tables.sql', 'r')
        sqlFile = fd.read()
        fd.close()
        
        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')

        # Execute every command from the input file
        for command in sqlCommands:
            try:
                cursor = self.conn.cursor(); 
                cursor.execute(command)
                self.conn.commit()
            except Error as e:
                print e
            finally:
                cursor.close()
                    
        
        