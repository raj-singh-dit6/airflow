from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


class DynamicDagGeneratorTemplate(object):

    def __init__(self,dag_configs_dag):
        self.dag_configs_dag=dag_configs_dag
        pass

    def create_dag(self):
        main_dag = DAG(
            self.dag_configs_dag["dag_id"],
            default_args=self.dag_configs_dag["default_args"],
            schedule_interval=self.dag_configs_dag.get("schedule_interval", None),
            start_date=self.dag_configs_dag.get("start_date", None),
            catchup=self.dag_configs_dag.get("catchup", False)
        )
        main_dag.doc_md = __doc__  # adds the module docstring to the Airflow UI

        tasks = {}

        with main_dag:
            ##############
            # TASK  1#
            ##############
            tasks["start_task"] = {}

            docstring = """
                    Starts the pipeline
                    """
            task_id = "start_task"
            tasks["start_task"][task_id] = EmptyOperator(
                task_id=task_id,
                dag=main_dag
            )
            tasks["start_task"][task_id].doc_md = docstring


            # TASK  2#
            ##############
            tasks["print_hello_world"] = {}

            docstring = """ Print HelloWords!
                                """
            task_id = "print_hello_world"
            tasks["print_hello_world"][task_id] = BashOperator(
                task_id=task_id,
                bash_command='echo "HelloWorld!"',
                dag=main_dag
            )
            tasks["print_hello_world"][task_id].doc_md = docstring



            # TASK  3#
            ##############
            tasks["end"] = {}

            docstring = """ Ends the pipeline
                                """
            task_id = "end"
            tasks["end"][task_id] = EmptyOperator(
                task_id=task_id,
                dag=main_dag
            )
            tasks["end"][task_id].doc_md = docstring



        return main_dag