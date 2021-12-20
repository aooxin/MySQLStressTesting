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
fCsv = csv.writer(open('record2.csv', 'a'), lineterminator='\n')
# fCsv.writerow(("record", ""))
# fCsv.writerow(("第多少条数据", "花费时间"))
fCsv2 = csv.writer(open('record_select.csv', 'a'))


# fCsv2.writerow(("record_select", ""))
# fCsv2.writerow(("第多少条数据", "花费时间"))


def run_t1():
    count = 0
    global commit_time
    start_time = int(time.time())
    for i in range(5010):
        before = datetime.datetime.now()
        beforeTt = int(time.time())
        isInFor = False
        while True:
            if not isInFor:
                for j in range(100):
                    ran = random.randint(10000, 99999)
                    try:
                        insert(ran, 1000)
                    except Exception:
                        # conn.rollback()
                        continue
                    count = count + 1
            isInFor = True
            if int(time.time()) - beforeTt >= 1:
                # print(int(time.time()) - beforeTt)
                break
        now = datetime.datetime.now()
        write_in_str = "The " + str(i * count) + " t1 at:" + str(before) + " to " + str(
            now) + " used " + str(now - before) + "\n"
        # print("insert time: ", int(time.time()) - start_time)
        # 文本操作
        # fw.write(write_in_str)
        if not (i + 1) % 10:
            WriteRow = (str((i + 1) * 100), str(now - before))
            fCsv.writerow(WriteRow)
        end_time = int(time.time())
        # print(end_time - start_time)
        conn.commit()
        # time.sleep(1)


def insert(user_id, group_id):
    global execute_time
    read_start = int(time.time())
    content = f.readline()
    global readtime
    while len(content) == 1:
        content = f.readline()
        break
    read_end = int(time.time())
    readtime = readtime + read_end - read_start
    if len(content) == 0:
        content = f.readline()[1:]
    mysql_t1 = "INSERT INTO group_message(ID,G_ID,message_content,mess_time)VALUES(" + str(user_id) + "," + str(
        group_id) + "," + "'" + content + "'" + ",CURRENT_TIMESTAMP);"
    execute_start = int(time.time())
    cur.execute(mysql_t1)
    execute_time = execute_time + int(time.time()) - execute_start


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
th1 = threading.Thread(run_t1()).start()
# th2 = threading.Thread(run_t2()).start()
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
print(pro_end - pro_begin)
print("read time :", readtime)
print("commit time: ", commit_time)
print("execute time: ", execute_time)
