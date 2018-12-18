1811127 com

1811085 fog

1811085 flesch




#Counting of values from the postblock table that should be considered for the postblockevolution table
SELECT  count(1)
FROM postblockversion a, postblockversion b
where a.postblocktypeid = 1
and a.gunning_fog_index is not null
and a.flesch_reading_ease is not null
and a.PredPostBlockVersionId = b.Id
and b.postblocktypeid = 1
and b.gunning_fog_index is not null
and b.flesch_reading_ease is not null
