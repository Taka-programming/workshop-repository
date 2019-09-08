import sqlite3
from datetime import datetime
import serial

# 温度、湿度データを表示する
def print_distance_data(ser):
    str_data = ser.readline().decode(encoding='utf-8')
    print(str_data)

# 温度、湿度データを取得する
def get_distance_data(ser):
    str_data = ser.readline().decode(encoding='utf-8').replace("\n", "")
    distance = str_data.split(", ")[0].split(":")[1]
    return distance

# データベースdb.sqlite3に対してクエリqueryを実行する
def execute_query(dbname, query):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    conn.close()
# テーブルtableにデータ(date, distance, source)を挿入する
def create_insert_query(table, date, distance, source):
    query = "insert into {} (date, distance, source) values ('{}', {}, '{}')".format(table, date, distance, source)
    print(query)
    return query
# テストデータを挿入する
def insert_test_data():
    date = datetime.now()
    distance = 0.0
    source = "query.py"
    query = create_insert_query(table, date, distance, source)
    execute_query(dbname, query)
if __name__ == "__main__":
    # print_distance_data()
    # insert_test_data()
    dbname = "db.sqlite3"
    table = "distance"
    #portは各自正しい値に設定してください
    port = "/dev/cu.usbmodem143401"
    ser = serial.Serial(port=port, baudrate=9600, timeout=None)
    print("Press ctrl + c to stop.")

    while True:
        date = datetime.now()
        humid, distance = get_distance_data(ser)
        source = "query.py"
        query = create_insert_query(table, date, distance, source)
        execute_query(dbname, query)
    ser.close()
