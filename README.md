# Live Coding Data Platform
During the live coding session we will be working on two Airflow DAGs that consume, transform and process data.
In order to get our hands dirty from the very start, please make sure your local environment is setup and prepared.

While working on the project you will be able to utilize all ressources that you would have access to, during a
regular workday as well. Feel free to google or read up official docs if you are stuck. We would like to have an open
session about programming and not test if you can remember all python functions by heart.

The live coding session will be cut of after 45 minutes, no matter how far you have gotten during this time. You will 
not be evaluated based on the outcome but only based on the way you got there. So don't pressure yourself into doing 
things as fast as possible.

After the coding session we would still like to have some time to talk about architectural topics and leave room for 
your own questions.

## Before the interview
### Familiarize yourself with Apache Airflow
In case you have not worked with Airflow in the past it does make sense if you briefly read the introduction of Apache
Airflow. Don't worry though, you do not need to be an Airflow pro to finish the session. A basic understanding the Airflow
principles helps though.
This tutorial is a good initial read to understand airflow: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html

### Setup your local environment
Please setup a working local environemnt and make sure you can execute one of the example DAGs provided with the Airflow installation.
This project was built using
```bash
PYTHON_VERSION=3.9.1
AIRFLOW_VERSION=2.3.0
# To enable demo DAGs change this env variable to True in standalone.sh
export AIRFLOW__CORE__LOAD_EXAMPLES=True
```

Have an IDE setup that you are comfortable working with. We recommend running the code in a new virtual environment.

To install airflow and dependencies follow the tutorial here: https://airflow.apache.org/docs/apache-airflow/stable/start/local.html


# INSTRUCTIONS DURING INTERVIEW
Before starting the challenge please read through all tasks and ask us if you did not understand a task or are unsure what we try to achieve. Asking questions earlier usually saves more trouble later.

To start things of try to run the unittests.
```bash
make test
```
 
## Executing and testing DAGs / Tasks
```bash
# Execute all tasks in a dag sequentially
AIRFLOW_HOME=$(pwd) PYTHONPATH=$(pwd):${PYTHONPATH} airflow dags test task_1_csv 2022-05-12
# Execute a single task in a dag
AIRFLOW_HOME=$(pwd) PYTHONPATH=$(pwd):${PYTHONPATH} airflow tasks test task_1_csv store_csv 2022-05-12
```

# Taks
## Task 1: Process records from CSV file into SQlite using PythonOperators
The first DAG will read data from a CSV file `dags/data/sample.csv` and store all rows into the SQLite table already setup.  
    Step 1: Read dags/data/sample.csv and inserts all rows into demo_data table.  
    Step 2: Read table data from sqlite based on input dict and print to console.  
    Step 4: Review code and suggest how and why a custom operator would improve the code.  

# Task2: Streaming records daily from file, aggregate and filter
This time the DAG should stream records from csv files. The files are split by day and you should convert them into a binary format of your choice.  
In the end we would like to filter one value per day.  
    Step 1: Read file based on date of airflow task instance from list of transactions files `dags/data/transactions_*.csv`.   
            Convert to a binary format and store in temporary file.  
            *Hint: Make sure all rows streamed follow the same format.*  
    Step 2: Read the temporary binary file and then return the key with the 3rd highest number for any date  
            *Hint: aggregate records with the same key before looking for the 3rd highest number*  
    Step 3: Write a unittest to check if your validation works on known cases of wrong data.  
