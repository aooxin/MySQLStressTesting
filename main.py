import pymysql
import threading
import time
import os
import datetime
import random
import csv

f = open("train.txt", encoding='UTF-8')
# fw = open("record.txt", 'a')
readtime = 0
commit_time = 0
execute_time = 0
fCsv = csv.writer(open('record.csv', 'a'))
fCsv2 = csv.writer(open('record_select.csv', 'a'), lineterminator='\n')
# fCsv2.writerow(("record", ""))
# fCsv2.writerow(("第多少条数据", "花费时间"))


# fCsv2.writerow(("record_select", ""))
# fCsv2.writerow(("第多少条数据", "花费时间"))


def select_t3(i):
    IsInExecute = False
    begin = int(time.time())
    mysql_t3 = "SELECT * from group_message WHERE ID=" + str(random.randint(10000, 99999)) + ";"
    while True:
        if not IsInExecute:
            before = datetime.datetime.now()
            cur.execute(mysql_t3)
            now = datetime.datetime.now()
            WriteRow = (str((i + 1)), str(now - before))
            fCsv2.writerow(WriteRow)
            IsInExecute = True
        if int(time.time()) - begin >= 1:
            break


def run_t2():
    for i in range(5010):
        try:
            select_t3(i)
        except Exception:
            continue


# 连接数据库，
conn = pymysql.connect(
    host='180.76.232.1',
    user='root',
    password='max101312',
    db='wechat',
    charset='utf8',
    # autocommit=True,  # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
# ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
# 创建游标对象，
cur = conn.cursor()
pro_begin = datetime.datetime.now()
# 创建线程
# th1 = threading.Thread(run_t1()).start()
th2 = threading.Thread(run_t2()).start()
# 循环
# cur.execute(mysql_t2)
conn.commit()
# 关闭游标
cur.close()
# 关闭连接
conn.close()
# 关闭文件
f.close()
# fw.close()
pro_end = datetime.datetime.now()
print("运行总时间", pro_end - pro_begin)
