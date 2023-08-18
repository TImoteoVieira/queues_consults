from dotenv import load_dotenv
load_dotenv()
import os
import pymysql.cursors

def get_clients():
    consult = os.environ.get("CONSULT")
    config = {
        'user': os.environ.get("POST_USER"),
        'password': os.environ.get("POST_PASS"),
        'host': os.environ.get("POST_HOST"),
        'database': os.environ.get("POST_DATABASE")}
    connection = pymysql.connect(**config)
    cursor = connection.cursor()
    cursor.execute(consult)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result