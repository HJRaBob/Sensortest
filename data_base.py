import sqlite3
import time

class Group_two_DB:
    def __init__(self):
        self.conn = sqlite3.connect('sensor.db')
        self.curs = self.conn.cursor()
        self.make_table('JOY')
        self.make_table('LED1')
        self.make_table('LED2')
        self.make_table('MOTOR')

        self.make_table('PIR')
        self.make_table('ILLU')
        self.make_table('TEMP')
        self.make_table('HUMI')
        self.make_table('PIEZO')
        self.make_table('SONIC')
        return

    def make_table(self,name):
        self.curs.execute('drop table if exists {}'.format(name))
        self.curs.execute('create table {}(time varchar(15),state varchar(10))'.format(name))
        return

    def add_values(self,table_name,values):
        self.curs.execute('insert into {} values {}'.format(table_name,values))
        return

    def find_value(self,table_name,field_name,values):
        self.curs.execute('select time,state,control from {} where {}={}'.format(table_name,field_name,values))
        return

    def save(self):
        self.conn.commit()
        return

    def finish(self):
        self.conn.close()
        return

class DB_Control:
    def __init__():
        two_db = Group_two_DB()
        return

    def save_data(statelist):
        now_time = time.time()
        two_db.add_values(JOY,(now_time,statelist[0]))
        two_db.add_values(PIR,(now_time,statelist[1]))
        two_db.add_values(ILLU,(now_time,statelist[2]))
        two_db.add_values(LED1,(now_time,statelist[3]))
        two_db.add_values(LED2,(now_time,statelist[4]))
        two_db.add_values(ULTRA,(now_time,statelist[5]))
        two_db.add_values(TEMP,(now_time,statelist[6]))
        two_db.add_values(HUMI,(now_time,statelist[7]))
        two_db.add_values(PIEZO,(now_time,statelist[8]))
        two_db.add_values(MOTOR,(now_time,statelist[9]))
        two_db.save()
        two_db.finish()
        return
