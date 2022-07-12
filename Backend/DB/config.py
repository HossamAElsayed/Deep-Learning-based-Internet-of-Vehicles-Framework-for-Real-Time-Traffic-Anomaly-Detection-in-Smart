import mysql.connector
from mysql.connector import errorcode

#
# This function is used in first time setup only
#
def out_of_box_setup():
    print('')

#
# To connect to the database
#
def establish_db_connection(db_name = 'OBU_DB'):
    # Connection main parameters
    usr = 'admin'
    pw='admin'
    hst = '127.0.0.1'
    

    try:
        # Try to establish connection
        global cnx
        cnx = mysql.connector.connect(user=usr, password=pw, host=hst, database=db_name)
        if cnx:
            print("Connection established successfully")
            return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

#
# To connect to the database
#
def establish_connection_with_main_server(db_name = 'server_db'):
    # Connection main parameters
    usr = 'admin'
    pw='admin'
    hst = '192.168.1.3'
    try:
        # Try to establish connection
        global cnx
        cnx = mysql.connector.connect(user=usr, password=pw, host=hst, database=db_name)
        if cnx:
            print("Connection with the main server established successfully :)")
            return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


#
# To close connection to the database.
#
def close_connection():
    try:
        cnx.close()
        print("Connection to database closed successfully")
    except:
        print('Unable to close the connection')
    
