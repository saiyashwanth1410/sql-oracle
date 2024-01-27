import csv
import cx_Oracle
conn=cx_Oracle.Connection('system/manager@mother')
cur = conn.cursor()

def createtable():
    query = '''create table saiyashwanth1410MCA (id number(2) primary key,name varchar(50))'''
    cur.execute(query) 
def insertrecord(sid,name):
    record={'id':str(sid),'name':name}
    cur.execute("insert into saiyashwanth1410MCA(id,name) values(:id,:name)",record)
    conn.commit()

def read_records():
    query = 'select * from saiyashwanth1410MCA'
    cur.execute(query)
    records = cur.fetchall()
    with open ('records.csv','w',newline='') as csvfile:
        data=csv.writer(csvfile)
        data.writerow(['id','name'])
        for row in records:
            data.writerow(row)
read_records()

def fetch_records(sid):
    query='select * from saiyashwanth1410MCA'
    cur.execute(query)
    records=cur.fetchall()
    
#fetch_records(2)

def update_name(sid,name):
    fetch_records(sid)
    name=input('enter new name to update:-')
    record={'id':str(sid),'name':name}
    query='update saiyashwanth1410MCA set name=:name where i =:id'
    cur.execute(query,record)
    conn.commit()
#fetch_records('sid')


def delete_record(sid):
    record={'id':str(sid)}
    query='delete from saiyashwanth1410MCA where id =:id'
    cur.execute(query,record)
    cur.commit()

def truncate():
    query ='truncate table saiyashwanth1410MCA'
    cur.execute(query)

def insert_from_csv():
    with open ('record.csv','r') as csvfile:
        data=csv.reader(csvfile)
        data=list(data)
        for row in range (1,len(data)):
            insertrecord(*data[row])