import sqlite3
connection= sqlite3.connect("mytable5.db")
crsr=connection.cursor()
connection.execute("PRAGMA foreign_keys = ON")
sql_command="""CREATE TABLE IF NOT EXISTS jobs(
    Job_id VARCHAR(255) PRIMARY KEY
    );"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO jobs VALUES ('job00001');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO jobs VALUES('job00002');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO jobs VALUES('job00003');"""
crsr.execute(sql_command)
sql_command="""CREATE TABLE IF NOT EXISTS job_history(employeeid INTEGER PRIMARY KEY NOT NULL,startdate DATE NOT NULL,enddate DATE NOT NULL,job_id VARCHAR(255) NOT NULL,departmentid INTEGER NOT NULL,FOREIGN KEY (job_id) REFERENCES jobs(Job_id));"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO job_history VALUES('121','2020-18-04','2022-18-04','job00001','101');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO job_history VALUES('121','1995-15-09','1996-15-09','job00002','102');"""
crsr.execute(sql_command)
sql_command="""INSERT INTO job_history VALUES('125','1994-15-09','1998-05-09','job00002','100');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO job_history VALUES('123','1990-13-09','1996-15-09','job00003','105');"""
crsr.execute(sql_command)
crsr.execute("SELECT * FROM job_history")
ans = crsr.fetchall()
for i in ans:
    print(i)
connection.close()
