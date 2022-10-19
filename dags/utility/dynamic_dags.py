import re

from datetime import datetime,timedelta
import logging

from dags.pipeline_templates.dag_template import DynamicDagGeneratorTemplate

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
def initiate_dynamic_dags_loader(file):

    filename = re.search('([0-9]+).py', file)

    if filename:
        my_slice = int(filename.group(1))
        LOGGER.info('Total Dag Loaders: {}, Slice: {}'.format(5, my_slice))
        return build_dynamic_dags(5, my_slice)
    else:
        raise Exception('Dynamic Dags Loader file name must end with #.py')

def build_dynamic_dags(total_workers, worker_id):
    dynamic_dags={}

    for i in range(0,10):
        if i%total_workers == worker_id:
            dynamic_dags[i] = generate_dag(i)
    #print(dynamic_dags)
    return dynamic_dags



def generate_dag(worker_id):
    dag_id='PIPELINE'.join(str(worker_id))

    dag_configs = {
        "dag_id": dag_id,
        "schedule_interval": '@daily',
        "start_date": datetime.now(),
        "catchup": True,
        "default_args": {
            "owner": "airflow",
            "depends_on_past": False,
            "start_date": None,
            "retries": 2,
            "retry_delay": timedelta(seconds=5)

        }
    }

    pipeline=None


    #We can chosse any template
    pipeline=DynamicDagGeneratorTemplate(dag_configs)

    return pipeline.create_dag()







