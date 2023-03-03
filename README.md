# sqlalchemy-challenge
Part 1: Analyze and Explore the Climate Data

Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame, and set the index to the "date" column.
5. Sort the DataFrame values by "date".
6.Plot the results by using the DataFrame plot method, as the following image shows:
7:Use Pandas to print the summary statistics for the precipitation data.

Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows).
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data.
5. Close your session.

Part 2: Design Your Climate App
Use Flask to create your routes
