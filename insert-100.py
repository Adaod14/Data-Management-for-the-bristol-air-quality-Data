import pandas as pd

clean_df = pd.read_csv("clean.csv", nrows = 100, low_memory= False)
table = "data_main_table"
with open('insert-100.py', 'w'):
    for index, row in clean_df.iterrows():
        print(
            'INSERT INTO' + table + '(\'Date Time\', \'NOx\', \'NO2\', \'NO\', \'SiteID\', \'PM10\', \'NVPM10\', \'VPM10\', \'NVPM2.5\', \'VPM2.5\', \'CO\', \'O3\', \'SO2\', \'Temperature\', \'RH\', \'Air Pressure\', \'Location\', \'geo_point_2d\', \'DateStart\', \'DateEnd\', \'Current\',\`Instrument Type\') VALUES (',
            row['Date Time'], ',', row['NO2'], ',', row['NO2'], ',', row['NO'], ',', row['SiteID'], ',', row['PM10'], ',',
            row['NVPM10'], ',', row['VPM10'], ',', row['NVPM2.5'], ',', row['VPM2.5'], ',', row['CO'], ',', row['O3'], ',',
            row['SO2'], ',', row['Temperature'], ',', row['RH'], ',', row['Air Pressure'], ',', row['Location'], ',',
            row['geo_point_2d'], ',', row['DateStart'], ',', row['DateEnd'], ',', row['Current'],
            ',\'' + row['Instrument Type'] + '\');', file=open("insert_100.sql", "a"))
        print(
            'INSERT INTO' + table + '(\'Date Time\', \'NOx\', \'NO2\', \'NO\', \'SiteID\', \'PM10\', \'NVPM10\', \'VPM10\', \'NVPM2.5\', \'VPM2.5\', \'CO\', \'O3\', \'SO2\', \'Temperature\', \'RH\', \'Air Pressure\', \'Location\', \'geo_point_2d\', \'DateStart\', \'DateEnd\', \'Current\',\`Instrument Type\') VALUES (',
            row['Date Time'], ',', row['NO2'], ',', row['NO2'], ',', row['NO'], ',', row['SiteID'], ',', row['PM10'], ',',
            row['NVPM10'], ',', row['VPM10'], ',', row['NVPM2.5'], ',', row['VPM2.5'], ',', row['CO'], ',', row['O3'], ',',
            row['SO2'], ',', row['Temperature'], ',', row['RH'], ',', row['Air Pressure'], ',', row['Location'], ',',
            row['geo_point_2d'], ',', row['DateStart'], ',', row['DateEnd'], ',', row['Current'],
            ',\'' + row['Instrument Type'] + '\');', )

