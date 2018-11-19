from google.cloud import bigquery

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('C:\\Users\\bernhard\\Documents\\SODataMining\\MySQL\\My First Project-3077a63e8f7b.json')

project_id = 'sotorrent-org'

client = bigquery.Client(credentials= credentials,project=project_id)

query_ = ("""

  SELECT COUNT(1)

  FROM `2018_09_23.Badges`;

  """)


job = client.query(query_)
result = list(job.result())[0]
print result


