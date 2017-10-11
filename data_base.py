import sqlite3

class Group_two_DB:
    def __init__(self):
        self.conn = sqlite3.connect('sensor.db')
        self.curs = self.conn.cursor()
        self.make_table('Jog')
        self.make_table('LED')
        self.make_table('CLCD')
        self.make_table('FND')
        self.make_table('Motor')

        self.make_table('PIR')
        self.make_table('Light')
        self.make_table('Temp')
        self.make_table('Piezo')
        self.make_table('Sonic')
        return

    def make_table(self,name):
        self.curs.execute('drop table if exists {}'.format(name))
        self.curs.execute('create table {}(time integer primary key,state varchar(10),commend varchar(10))'.format(name))
        return

    def add_values(self,table_name,values):
        self.curs.execute('insert into {} values {}'.format(table_name,values))
        return

    def save(self):
        self.conn.commit()
        return

    def finish(self):
        self.conn.close()
        return


two_db = Group_two_DB()

two_db.save()
two_db.finish()
