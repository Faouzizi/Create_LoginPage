################################################################################
##########################         import packages         #####################
################################################################################
import mysql.connector as MySQLdb
import sys
sys.path.insert(0,'../.')
import config
import pandas as pd

################################################################################
########################## Create Database on mysql server #####################
################################################################################
def create_db(mysql_user=config.mysql_user, mysql_password=config.mysql_password ,mysql_host=config.mysql_host, db_name=config.db_name):
    try:
        conn = MySQLdb.connect(user=mysql_user, host=mysql_host, password=mysql_password)
        print('Connection to mysql server Done : success')
        try:
            cur = conn.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS "+db_name+" ;")
            conn.commit()
            print("database created with success")
        finally:
            conn.close()
            print("connection closed !")
    except:
        print("I am unable to connect to the database")


################################################################################
########################## Create Database on mysql server #####################
################################################################################
def create_table(mysql_user=config.mysql_user, mysql_password=config.mysql_password ,mysql_host=config.mysql_host,table_name=config.table_name, db_name=config.db_name):
    try:
        conn = MySQLdb.connect(user=mysql_user, host=mysql_host, password=mysql_password,  database=db_name)
        print('Connection to mysql server Done : success')
        try:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS %s (id INT AUTO_INCREMENT PRIMARY KEY,
                                                                              email varchar(250), 
                                                                              name varchar(250),
                                                                              password varchar(250) 
                                                                              );""" %(table_name))
            conn.commit()
            print("Table created with success")
        finally:
            conn.close()
            print("connection closed !")

    except:
        print("I am unable to connect to the database")

def insert_row(email, name, password, user_name=config.mysql_user, mysql_password=config.mysql_password, host_name=config.mysql_host, db_name=config.db_name, table_name=config.table_name):
    # Define our connection string
    conn = MySQLdb.connect(user=user_name, password=mysql_password, host=host_name, database=db_name)
    try:
        cursor = conn.cursor()
        cursor.execute("""insert into %s (email, name, password) values ('%s', '%s', '%s'); """ %(table_name, email, name, password))
        conn.commit()
    finally:
        conn.close()
    print('Row inserted')


def import_data(query, mysql_user=config.mysql_user, mysql_password=config.mysql_password, mysql_host=config.mysql_host):
    try:
        conn = MySQLdb.connect(user=mysql_user, host=mysql_host, password=mysql_password)
        print('Connection to mysql server Done : success')
        print(query)
    except:
        print("I am unable to connect to the database")
    try:
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        data = pd.DataFrame(list(results), columns=[row[0] for row in cur.description]).reset_index(drop=True)
        print(data)
    finally:
        conn.close()
    return (data)
