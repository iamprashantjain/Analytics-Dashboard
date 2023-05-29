import streamlit as st
from helper import DB
import matplotlib.pyplot as plt


db = DB()


st.sidebar.title('Flights Analystics')
option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])


if option == 'Check Flights':
	st.title('Check Flights')

	city = db.fetch_city_names()

	col1,col2 = st.columns(2)
	with col1:		
		source = st.selectbox('Source',sorted(city))


	with col2:		
		destination = st.selectbox('Destination',sorted(city))


	if st.button('Search'):
		results = db.fetch_all_flights(source,destination)
		st.dataframe(results)



elif option == 'Select One':
	st.title("Live SQL Dashboard")




else:
	st.title('Analytics')
	
	#als freq
	als,freq = db.fetch_als_freq()

	fig, ax = plt.subplots()
	ax.pie(freq, labels=als, autopct='%1.1f%%')
	ax.axis('equal')

	ax.set_title('Daily Airline Frequency')

	st.pyplot(fig)


	#busy apt
	labels, values = db.fetch_busy_apt()
	fig, ax = plt.subplots()
	ax.bar(labels, values)

	ax.set_title('Busiest Airports')
	ax.set_xlabel('City')
	ax.set_ylabel('Frequency')

	plt.xticks(rotation=90)

	st.pyplot(fig)


	#daily_flight_running
	dates, counts = db.daily_running_flights()

	fig, ax = plt.subplots()

	# Create the line chart using the dates and counts
	ax.plot(dates, counts)

	# Set chart title and axis labels
	ax.set_title('Daily Running Flights')
	ax.set_xlabel('Date')
	ax.set_ylabel('Count')

	# Rotate x-axis labels if needed
	plt.xticks(rotation=90)

	# Display the chart
	st.pyplot(fig)



