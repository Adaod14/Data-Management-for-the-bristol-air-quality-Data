import pandas as pd

# First, a dataframe is created from the given project data file using pandas and stored in a variable called 'data'.
data = pd.read_csv("bristol-air-quality-data.csv", sep=';')
# Next, the data is sorted by the 'Date Time' column and arranged in ascending order
asc = data.sort_values("Date Time", ascending=True)
# The data is cropped to delete any records before 00:00 1 Jan 2010
cropped_data = asc[asc["Date Time"] >= "2010-01-01T00:00:00+00:00"]
# Finally, we saved the cropped data to a .csv file for further cleaning
crop = cropped_data.to_csv("crop.csv", index = False)
