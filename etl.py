import os
import glob
import psycopg2
import datetime
import time
import pandas as pd
import numpy as np
from sql_queries import *

def process_demog_file(cur, filepath):
    df_demo = pd.read_csv(filepath, sep=";", header=0)
    # insert demographic records
    demo = df_demo.loc[:,('State Code', 'City','State', 'Race')].values.tolist()
    
    for i in range(len(demo)):
        cur.execute(demo_table_insert, demo[i])
    
    
    #insert population records
    
    population = df_demo.loc[:,('City','Median Age', 'Male Population', 'Female Population', 'Total Population', 'Number of Veterans', 'Foreign-born', 'Average Household Size', 'Count' )].values.tolist()
    for i in range(len(population)):
        cur.execute(population_table_insert, population[i])
    
def process_temperatures_file(cur, filepath):
    df = pd.read_csv(filepath, sep=",", header=0)
    
    # extract year, month, date  and convert string date format to datetime format
    
    df['dt'] = pd.to_datetime(df['dt'], format='%Y-%m-%d')
    #t = df['datetime'] = pd.to_datetime(df['dt'])
    df['year'] = pd.DatetimeIndex(df['dt']).year 
    df['month'] = pd.DatetimeIndex(df['dt']).month
    df['day'] = pd.DatetimeIndex(df['dt']).day
    #df['month'] = df.datetime.dt.month
    #df['year'] = df.datetime.dt.year
    #df['day'] = df.dt.dt.day
    #time_df = df.loc[:,('year', 'month')]
    # insert time data records
    time_data = df.loc[:,('year', 'month','day')]
    time = time_data.values.tolist()
    for i in range(10000):
        cur.execute(time_table_insert, time[i])
    #insert 
    
    #temp = df.loc[:,('AverageTemperature', 'AverageTemperatureUncertainty', 'City', 'Country', 'Latitude', 'Longitude')]
    temp = df.loc[:,('City', 'Country', 'Latitude', 'Longitude')]
    temperatures = temp.values.tolist()
    for i in range(10000):
        cur.execute(temp_table_insert, temperatures[i])
    
    
def process_data(cur, conn, filepath, func):
   
    # get all files matching extension from directory
        all_files = []
        for root, dirs, files in os.walk(filepath):
            files = glob.glob(os.path.join(root,'*.csv'))
            for f in files :
                all_files.append(os.path.abspath(f))

    # get total number of files found
        num_files = len(all_files)
        print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
        for i, datafile in enumerate(all_files, 1):
            func(cur, datafile)
            conn.commit()
            print('{}/{} files processed.'.format(i, num_files))

def race_check(cur, conn):
    cur.execute("select count(distinct race) from demo")
    result1=cur.fetchall()
    if result1[0][0]==5:
        print("Race column QC passed!")
    else:
        print("QC failed!")
def city_check(cur, conn):
    cur.execute("SELECT count(distinct City) from demo")
    result2=cur.fetchall()
    if result2[0][0]==49:
        print("city column QC passed!")
    else:
        print("QC failed!")
def state_check(cur,conn):
    cur.execute("SELECT count(distinct State) from demo")
    result3=cur.fetchall()
    if result3[0][0]==49:
        print("state column QC passes!")
    else:
        print("QC failed!")
        
    
"""Establishes connection to the Sparkifydb and process the song_data and log_data and closes the connenction."""
def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    process_data(cur, conn, filepath ="/home/workspace/demographics/", func=process_demog_file)
    process_data(cur, conn, filepath = '../../data2/', func=process_temperatures_file)
    race_check(cur,conn)
    city_check(cur, conn)
    state_check(cur, conn)
    conn.close()
    
if __name__ == "__main__":
    main()    