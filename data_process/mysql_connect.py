import pymysql
import os


def get_connection():
    connection = pymysql.connect(
        host="127.0.0.1",
        port=13306,
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        charset="utf8mb4"
    )

    return connection