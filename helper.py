import mysql.connector


class DB:
	#as soon as we create an object of this class, construtor will be called
	#& so dbs will be connected 
	
	def __init__(self):
		#connect to dbs
		try:
			self.conn = mysql.connector.connect(
			host = '127.0.0.1',
			user = 'root',
			password = '',
			database = 'indigo'
			)

			self.mycursor = self.conn.cursor()
			print('connection established')


		except: 
			print("Connection Error")


	def fetch_city_names(self):
		
		city = []

		self.mycursor.execute(""" 
			SELECT distinct(Source) FROM indigo.flights_data
			union
			SELECT distinct(Destination) FROM indigo.flights_data
			""")

		data = self.mycursor.fetchall()
		
		for item in data:
			city.append(item[0])

		return city



	def fetch_all_flights(self,source,destination):

		self.mycursor.execute(f"SELECT * FROM indigo.flights_data WHERE Source = '{source}' AND Destination = '{destination}'")
		data = self.mycursor.fetchall()
		return data


	
	def fetch_als_freq(self):
		
		als = []
		freq = []

		self.mycursor.execute(f"select Airline,count(*) from indigo.flights_data group by Airline")
		data = self.mycursor.fetchall()
		for i in data:
			als.append(i[0])
			freq.append(i[1])

		return als,freq


	def fetch_busy_apt(self):

		city = []
		freq = []

		self.mycursor.execute("""
							    SELECT Source, COUNT(*) AS Count
							    FROM (
							        SELECT Source FROM indigo.flights_data
							        UNION ALL
							        SELECT Destination FROM indigo.flights_data
							    ) t
							    GROUP BY t.Source
							    ORDER BY Count DESC
								""")
		data = self.mycursor.fetchall()

		for i in data:
			city.append(i[0])
			freq.append(i[1])

		return city,freq



	def daily_running_flights(self):
		date = []
		count = []

		self.mycursor.execute("""

			SELECT Date_of_Journey, count(*) FROM indigo.flights_data
			group by Date_of_Journey

			""")
		data = self.mycursor.fetchall()
		for i in data:
			date.append(i[0])
			count.append(i[1])

		return date,count


	