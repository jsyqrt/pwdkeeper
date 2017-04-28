# coding: utf-8
# pwdkeeper.py # password keeper with SQLite3 database and AES entryption.

import sqlite3
import os
import DES

DATABASE = 'PASSWD.sqlite'
CREATE_DB = '''create table records (
				sitename text not null, 
				username text not null,
				passwd text not null,
				notes text default "hack you!",
				primary key (sitename, username))
			'''
class pwdkeeper:

	def __init__(self, database = DATABASE):
		if not os.path.exists(database):
			open(database, 'w').close()
			self.database = database
			self.db = sqlite3.connect(self.database)
			self.db.execute(CREATE_DB)
			self.key = raw_input('input your des key:')

		else:
			self.database = self.decrypt(database)
			self.db = sqlite3.connect(self.database)

	def decrypt(self, database, ty = 'd'):
		if ty == 'd':
			self.key = raw_input('input your des key:')
		with open(database, 'rb') as f:
			w = DES.DES(f.read(), self.key, ty)
		with open(database, 'wb') as f:
			f.write(w)
		return database

	def create_record(self, sitename, username, passwd, notes):
		sql = 'insert into records values ("%s", "%s", "%s", "%s");' %(sitename, username, passwd, notes)
		self.db.execute(sql)
		self.db.commit()
		return True

	def find_record(self, sitename, username):
		sql = 'select * from records where sitename="%s" and username="%s"' %(sitename, username)
		return ','.join(list(list(self.db.execute(sql))[0]))
	
	def update_record(self, sitename, username, val, var):
		sql = 'update records set "%s"="%s" where sitename="%s" and username="%s"' %(val, var, sitename, username)
		self.db.execute(sql)
		self.db.commit()
		return True

	def delete_record(self, sitename, username):
		sql = 'delete from records whese sitename="%s" and username="%s"' %(sitename, username)
		self.db.execute(sql)
		self.db.commit()
		return True
	
	def execute_sql(self, sql):
		return self.db.execute(sql)
	
	def loop(self):
		while True:
			try:
				help_info = '''
password keeper
input your option:
0. exit
1. create new record
2. find record
3. update record
4. delete record
5. execute your sql
'''
				
				option = int(raw_input(help_info))
				if option == 0:
					self.db.close()
					self.decrypt(self.database, 'e')
					print 'exit...bye...'
					break
				elif option == 1:
					x = self.create_record(*raw_input('input your new record wiht order: \nsitename, username, passwd, notes. split them with ",":\n').split(','))
					print 'create record: ', x
				elif option == 2:
					print self.find_record(*raw_input('input your sitename and username to find your record with order: \nsitename, username. split them with ",":\n').split(','))
				elif option == 3:
					x = self.update_record(*raw_input('input your sitename, username, val(passwd/notes), var, split them with ",":\n').split(','))
					print 'update record: ', x
				elif option == 4:
					x = self.delete_record(*raw_input('input the sitename and username to delete your record, split them with ",":\n').split(','))
					print 'delete record: ', x
				elif option == 5:
					print self.execute_sql(raw_input('input your sql string:\n'))
				else:
					print 'wrong input! please input again!'
			except:
				print 'there may be some trouble...'

pwd = pwdkeeper()
pwd.loop()