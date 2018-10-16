import pandas as pd
import calendar
import time

# Input the selected year and month
year = 2018
month = 9
nbDays = calendar.monthrange(year,month)[1]

# For each day in the selected month
for x in range(1, nbDays+1):

	# Build the date string
	if x<10:
		day_str = "0" + str(x)
	else:
		day_str = str(x)
	if month<10:
		month_str = "0" + str(month)
	else:
		month_str = str(month)
	year_str = str(year)
	date = year_str + "-" + month_str + "-" + day_str
	
	# While the received data is incorrect (max. 3 trials)
	nbEl = 0
	trials = 1
	while(nbEl<1 and trials<=3):
		print("Extracting day-ahead data for " + date + " - Trial " + str(trials))
		
		# Read data from the webpage
		table = pd.read_html("https://www.epexspot.com/en/market-data/dayaheadauction/auction-table/" + date + "/FR", attrs={'class': 'list hours responsive'})[0]

		# Extract the last column (i.e., the selected day)
		last_column = table.iloc[:,8]
		nbEl = last_column.shape[0]
		#print("Number of read elements: " + str(nbEl))
		
		# Extract volumes
		volumes = last_column.iloc[::2]
		volumes.drop(volumes.index[0], inplace=True)
		volumes = volumes.reset_index(drop=True)

		# Extract prices
		prices = last_column.iloc[1::2]
		prices = prices.reset_index(drop=True)

		# Save as CSV file
		export = pd.concat([volumes, prices], axis=1)
		export.to_csv('' + date + '.csv', index=False, header=False)

		# Wait 1 second
		time.sleep(1)
		
		# Increase trials counter
		trials = trials+1

