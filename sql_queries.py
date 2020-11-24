# DROP TABLES
demo_table_drop = "DROP TABLE if exists demo"
population_table_drop = "DROP TABLE if exists population"
time_table_drop = "DROP TABLE if exists time"
temp_table_drop = "DROP TABLE if exists temperatures"

# CREATE TABLES

demo_table_create = ("""CREATE TABLE IF NOT EXISTS demo (
state_code varchar,
city varchar,
state varchar,
race text
);""")

population_table_create = ("""CREATE TABLE IF NOT EXISTS population (
city varchar,
male_population float,
median_age float,
female_population float,
total_population int,
number_of_veterans float,
foreign_born float,
average_household_size float,
count int
);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
day int,
month int,
year int
);""")

temp_table_create = ("""CREATE TABLE IF NOT EXISTS temperatures (
city varchar,
country varchar,
latitude varchar,
longitude varchar
);""")

# INSERT RECORDS

demo_table_insert = ("""INSERT INTO demo(
city,
state_code,
state,
race)
VALUES(%s,%s,%s,%s)
""")

population_table_insert = ("""INSERT INTO population(
city,
male_population,
median_age,
female_population,
total_population,
number_of_veterans,
foreign_born,
average_household_size,
count)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

time_table_insert = ("""INSERT INTO time(

day,
month,
year)
VALUES(%s,%s,%s)
ON CONFLICT DO NOTHING
""")

temp_table_insert = (""" INSERT INTO temperatures(
city,
country,
latitude,
longitude)
VALUES(%s,%s,%s,%s)
ON CONFLICT DO NOTHING
""")

#query to import distinct race values
race_select =("""select count(distinct race) from demo""")


demo_temp = ("""SELECT city, demo.city FROM demo JOIN demo ON temperatures.city = demo.city where state=%s AND state_code=%s AND country=%s""")

# QUERY LISTS

create_table_queries = [demo_table_create, population_table_create, time_table_create, temp_table_create]
drop_table_queries = [demo_table_drop,population_table_drop,time_table_drop, temp_table_drop] 

