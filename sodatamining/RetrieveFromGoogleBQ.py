import time

from google.cloud import bigquery
from google.cloud.bigquery.table import Table
from google.cloud.bigquery.dataset import Dataset


class Client(object):

    def __init__(self, origin_project, origin_dataset, origin_table,
                 destination_dataset, destination_table):
        """
        A Client that performs a hardcoded SELECT and INSERTS the results in a
        user-specified location.

        All init args are strings. Note that the destination project is the
        default project from your Google Cloud configuration.
        """
        self.project = origin_project
        self.dataset = origin_dataset
        self.table = origin_table
        self.dest_dataset = destination_dataset
        self.dest_table_name = destination_table
        self.client = bigquery.Client()

    def run(self):
        query = ("SELECT * FROM `{project}.{dataset}.{table}`;".format(
            project=self.project, dataset=self.dataset, table=self.table))

        job_config = bigquery.QueryJobConfig()

        # Set configuration.query.destinationTable
        destination_dataset = self.client.dataset(self.dest_dataset)
        destination_table = destination_dataset.table(self.dest_table_name)
        job_config.destination = destination_table

        # Set configuration.query.createDisposition
        job_config.create_disposition = 'CREATE_IF_NEEDED'

        # Set configuration.query.writeDisposition
        job_config.write_disposition = 'WRITE_APPEND'

        # Start the query
        job = self.client.query(query, job_config=job_config)

        # Wait for the query to finish
        job.result()
        
if __name__ == "__main__":
    client = Client()