import mysql.connector


#connect to the dbs server
#connecting to mysql_workbench

# try:
# 	conn = mysql.connector.connect(
# 		host = '127.0.0.1',
# 		user = 'root',
# 		password = '',
# 		database = 'indigo'
# 		)

# 	mycursor = conn.cursor()
# 	print('connection established')


# except: 
# 	print("Connection Error")



#to create a db on db server (mysql workbench)
# mycursor.execute('create database indigo')
# conn.commit()



#create a table
#airport -> apt_id(int), code(varchar), name(varchar)


# mycursor.execute("""

# create table airport (
# 	apt_id integer primary key,
# 	code varchar(10) not null,
# 	city varchar(255) not null,
# 	name varchar(255) not null
# )

# """)

# conn.commit()



#insert data to table
# mycursor.execute(''' 
# 	insert into airport values 
# 	(1,'del','delhi', 'igi'),
# 	(2,'ccu','kolkata', 'nsp'),
# 	(3,'knu','kanpur', 'knc')


# 	''')
# conn.commit()



#search/retrieve ops
#all complex queries can be written like below

# mycursor.execute(""" select * from airport where apt_id > 1""")
# data = mycursor.fetchall()				#rows are called tuple in sql, thats output is in tuple
# # print(data)

# for i in data:
# 	print(i[3])



#update values
# mycursor.execute(""" update airport
# 	set name = 'cst'
# 	where apt_id = 3
# 	""")

# conn.commit()



#retrieve again to see if changes being done or not

# mycursor.execute(""" select * from airport where apt_id > 0""")
# data = mycursor.fetchall()				#rows are called tuple in sql, thats output is in tuple
# # print(data)

# for i in data:
# 	print(i[3])



#delete 
# mycursor.execute(""" delete from airport where apt_id = 3""")
# conn.commit()


#retrieve again to see if changes done or not
# mycursor.execute(""" select * from airport where apt_id > 0""")
# data = mycursor.fetchall()				#rows are called tuple in sql, thats output is in tuple
# # print(data)

# for i in data:
# 	print(i[3])


