# Goal: 
The main goal of this project is to create ETL pipeline and finally create a analytics table database. To accomplish the specified goal,I worked on two datasets namely U.S.city demographics, temperature data.
# use case:
To know the number of male, female, and Total population based on country and State.

# etl.py : 
Establishes the connection to the Sparkify database, process the data, and insert records for fact and dimension tables.

# etl.ipynb : 
Performed the ETL process, extracted the data, created tables, and inserted values.To insert Records into the table, I have implemented the insert query in sql_queries.py and executed the required code to insert records for the fact and dimension tables and executed create_tables.py to create tables in the sparkify database.
# create_tables.py : 
create_tables.py creates database connection to the default database - studentdb. subsequently, created a database called - Sparkify and established a connection to the sparkify database. This database is responsible to create fact and dimension tables in the database based on the etl.py, etl.ipynp,s ql_queries.py.
# The capstone project contains the following steps
Step 1: Scope the Project and Gather Data
Step 2: Explore and Assess the Data
Step 3: Define the Data Model
Step 4: Run ETL to Model the Data
Step 5: Complete Project Write Up

# scoping and identifing the related data : 
1) To optimize the project, I have first gathered the data, throughly looked through all the datatsets and variables.
2) I was provided with four differnt datasets namely : immigration to the United States, airport codes, U.S. city demographics, and temperature data.
3) Explored the immigration to the United States, understood the common variables across other datasets, performed exploartory data analysis to find the number of missing values, summary statics, data quality issues. 
4) Explored the airport codes, understood the common variables across other datasets, performed the exploratory data analysis to find the number of missing values, summary statics, data quality issues. 
5) Explored the U.S. city demographics, understood the common variables across other datasets, performed the exploratory data analysis to find the number of missing values, and data quality issues.
6) Intially, to make a meaningfull and valuable dataset, I thought to include all four datasets, but eventually, I understood that it is not optimal or feseabile to unify all the datasets since there were no common variables across the datasets.
7) To achieve my goal, it was good to combine two datasets namely:  U.S. city demographics, and temperature data. A meaningful dataset was made by leveraging the above mentioned datasets. I combined both datasets by a commom column namely City. 
5) After combining the datasets, my next task was to explore the datasets to find the missing values, data issues, and duplicate records. I have excluded the variables if there were number of missing values.
6) As the datasets are realatively small, I prefered to use Relational Data Modelling to NOSQL. since the volume of the data is rather small, it is a good idea to use  Realational data modelling using Postgres. Using relational database,I have created start schema, which conatins fact and dimension tables. To sumaarise in short, I have used relational data modelling using postgres to create star schema

# Created Star schema : Fact and dimensions tables 
I have created Four tables namely demo_table_create, population_table_create, time_table_create, temp_table_create.



# Defining constariants while creating the schemas:

There were no unique identifier columns to uniquely identify each row. Consequently, I didn't specify Primary key option when I created the schemas.
All the required data types have been defined while creating the schemas.

# ETL : 
Intially, the data was sitting in the following paths "/home/workspace/demographics/", '../../data2/',so extracted the data, transformed the data into fact and dimension tables,finally loaded the data into the sparkify database. 
Sql_queries.py : Drops the tables if there are any already existing tables, create new tables, inserts values into the newly created tables

# Data qulaity checks:

Data quality checks have been implemented to check the completness of the data. I have counted the number of unique cities, state, race and cretaed three different data quality check to ensure the correctness and completness of the data

Write a description of how you would approach the problem differently under the following scenarios:
# The data was increased by 100x.
I would use Nosql Apache cassandra database since it handles and process large datasets efficiently.

# The data populates a dashboard that must be updated on a daily basis by 7am every day.
In the DAG define a parmeter schedule and assign the value as 7am

# The database needed to be accessed by 100+ people.
I will create redshift cluster database with several instances of EC2


