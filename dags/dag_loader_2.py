from airflow.models import DAG #Importing this causes the file to be loaded as part of the dagbag
from utility import dynamic_dags
globals().update(dynamic_dags.initiate_dynamic_dags_loader(__file__))
