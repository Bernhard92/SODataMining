#get postHistoryId of most recent changed block
select v.PostHistoryId  
from postblockversion v, posts p
where p.id = v.PostId
and p.id = 36881
and v.PostBlockTypeId = 1
and SuccCount = 0 
#There was a change
and v.PredSimilarity < 1;

#Get the hole text from the most recent version
select v.Content
from postblockversion v
where v.PostHistoryId = 36658080
and v.PostBlockTypeId = 1


