import sqlite3

class Group_two_DB:
    def __init__(self):
        self.conn = sqlite3.connect('sensor.db')
        self.curs = self.conn.cursor()
        return

    def make_table(self,name,field):
        self.curs.execute('drop table if exists {}'.format(name))
        self.curs.execute('create table {}({})'.format(name,field))
        return

    def add_values(self,table_name,form,values):
        self.curs.executemany('insert into {} values {}'.format(table_name,form),values)
        return

    def save(self):
        self.conn.commit()
        return

    def finish(self):
        self.conn.close()
        return

"""test code"""
two_db = Group_two_DB()
two_db.make_table('store','try,number')
test = [(1,100),(2,200),(3,300),(4,400),(5,500)]
two_db.add_values('store','(?,?)',test)
two_db.save()
two_db.finish()
