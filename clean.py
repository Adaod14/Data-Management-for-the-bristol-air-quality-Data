import pandas as pd



# First, a data frame is created from the 'crop.csv' file using pandas and saved in a variable called 'cropped_data'
cropped_data = pd.read_csv('crop.csv')
# The 'dropna()' function is used to delete dud records with an empty siteID value

empty_siteID = cropped_data.dropna(subset=['SiteID'])

# from the code above, no records were deleted, this indicates that there are no rows with a missing record for site ID.


# For further cleaning, records with a mismatch between siteID and Location are also deleted.
# To do this, we create lists of the stations and their accurate IDs embedded in a bigger list called 'site_info'.
# A Data frame called 'site_data' is created out of the site_info list.
# This Data frame contains the sites and their correct site IDs.
# The idea is to compare the values of the locations and their IDs in the new and accurate data frame with that
# of the cropped data frame to find and delete records with a mismatch.
# The cleaned data frame is then saved as a csv file called "clean.csv"


site_info = [['location', 'siteID'],
             ['AURN Bristol Centre', '188'],
             ['Brislington Depot', '203'],
             ['Rupert Street', '206'],
             ['IKEA M32', '209'],
             ['Old Market', '213'],
             ['Parson Street School', '215'],
             ['Temple Meads Station', '228'],
             ['Wells Road', '270'],
             ['Trailer Portway P&R', '271'],
             ['Newfoundland Road Police Station', '375'],
             ["Shiner's Garage", '395'],
             ['AURN St Pauls', '452'],
             ['Bath Road', '447'],
             ['Cheltenham Road \ Station Road', '459'],
             ['Fishponds Road', '463'],
             ['CREATE Centre Roof', '481'],
             ['Temple Way', '500'],
             ['Colston Avenue', '501']]

columns = site_info.pop(0)
site_data = pd.DataFrame(site_info, columns=columns)

cropped_data['SiteID'] = cropped_data['SiteID'].astype(str)

mismatched_rows = cropped_data[~cropped_data['SiteID'].isin(site_data['siteID'].values)]

cleaned_data = cropped_data[cropped_data['SiteID'].isin(site_data['siteID'].values)]
print(mismatched_rows)
clean = cleaned_data.to_csv('clean.csv', index = False)
