import datetime
from config import *

# One-time connection establish
global context
context = establish_db_connection()

def add_new_record(name):    
    cursor = context.cursor()
    add_new = ("INSERT INTO obu_data"
               "(name)"
               "VALUES (%s)")
    cursor.execute(add_new, [name])
    record_no = cursor.lastrowid
    print("New data inserted into:", record_no)
    context.commit()

    # finally, close all connections
    cursor.close()
    #close_connection()

def search_record(search_by, key):
    cursor = context.cursor()

    query = ("SELECT name FROM obu_data WHERE {} = '%s'".format(search_by))

    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query, [key])

    # for (first_name, last_name, hire_date) in cursor:
    #     print("{}, {} was hired on {:%d %b %Y}".format(
    #         last_name, first_name, hire_date))
    res = cursor.fetchall()
    print(res)
    # finally, close all connections
    cursor.close()
    close_connection()

def delete_record(delete_by, keys):
    cursor = context.cursor()
    for i in keys:
        query = ("DELETE FROM obu_data WHERE {} = '%s'".format(delete_by))
        cursor.execute(query, [i])
    context.commit()
    # finally, close all connections
    cursor.close()
    close_connection()
