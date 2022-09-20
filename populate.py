import pandas as pd
import mariadb as mysql
from mysql.connector import Error

cleaned_data = pd.read_csv('clean.csv', low_memory=False)
renamed_data = cleaned_data.rename(columns={'Date Time': 'date_time', 'PM2.5': 'pm25', 'NVPM2.5': 'nvpm25', 'VPM2.5': 'vpm25',
                             'Air Pressure': 'air_pressure', 'Instrument Type':'Instrument'}, inplace=True)
dbsite = cleaned_data.loc[0:805302,["SiteID", "Location", "geo_point_2d"]]
dbsitedata = dbsite.drop_duplicates()

try:
    connection = mysql.connect(host="localhost", user="root", password="")
    cursor = connection.cursor()
    print("MySQL Database connection successful")

except Error as err:
        print(f"Error: '{err}'")

pw = '123456'


try:
    cursor.execute("select database();")
    cursor.execute("DROP DATABASE IF EXISTS pollution_db2")
    cursor.execute("CREATE DATABASE pollution_db2")
    print("Database created successfully")
except Error as err:
        print(f"Error: '{err}'")


try:
    connection = mysql.connect(host='localhost', database='pollution_db2', user='root', password= "")
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)
except Error as e:
            print("Error while connecting to MySQL", e)

try:
    cursor.execute('DROP TABLE IF EXISTS sites;')
    cursor.execute('DROP TABLE IF EXISTS readings;')
    cursor.execute('DROP TABLE IF EXISTS schema_table;')

    cursor.execute("CREATE TABLE `sites` (`Location` text NOT NULL,`Site_id` int NOT NULL,`geo_point` float NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")

    cursor.execute('''
CREATE TABLE `readings` (
  `reading_id` int NOT NULL AUTO_INCREMENT,
  `Site_id` int NOT NULL,
  `Date_time` varchar(90) NOT NULL,
  `NO` float NOT NULL,
  `NOx` float NOT NULL,
  `NO2` float NOT NULL,
  `PM10` float NOT NULL,
  `NVPM10` float NOT NULL,
  `VPM10` float NOT NULL,
  `PM2.5` float NOT NULL,
  `NVPM2.5` float NOT NULL,
  `VPM2.5` float NOT NULL,
  `CO` float NOT NULL,
  `O3` float NOT NULL,
  `SO2` float NOT NULL,
  `Temperature` float NOT NULL,
  `RH` float NOT NULL,
  `Air_pressure` float NOT NULL,
  `date_start` varchar(90) NOT NULL,
  `date_end` varchar(90) NOT NULL,
  `current` float NOT NULL,
  `instrument` text NOT NULL,
  PRIMARY KEY(`reading_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
''')
    cursor.execute("CREATE TABLE `schema_table` (`schema_id` int NOT NULL AUTO_INCREMENT,`Measure` varchar(90) NOT NULL,`unit` varchar(90) NOT NULL,`Description` text NOT NULL, PRIMARY KEY(`schema_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")

except Error as e:
    print("Error while creating tables", e)


try:
    for row in dbsitedata.itertuples():

        cursor.execute("INSERT INTO sites (Location, Site_id, geo_point) VALUES (?,?,?)",
                         (row.Location, row.SiteID, row.geo_point_2d))

    connection.commit()
except Error as e:
    print("Error while creating tables", e)


try:
    for row in cleaned_data.itertuples():
                clean_row = [None if str(i) == "nan" else i for i in row]
                cursor.execute("INSERT INTO readings (`Site_id`, `Date_time`, `NO`, `NOx`, `NO2`, `PM10`, `NVPM10`, `VPM10`, `PM2.5`, `NVPM2.5`, `VPM2.5`, `CO`, `O3`, `SO2`, `Temperature`, `RH`, `Air_pressure`, `date_start`, `date_end`, `current`, `instrument`) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                row.SiteID, row.date_time, row.NO, row.NOx, row.NO2, row.PM10, row.NVPM10, row.VPM10, row.pm25, row.nvpm25,
                row.vpm25, row.CO, row.O3, row.SO2, row.Temperature, row.RH, row.air_pressure, row.DateStart, row.DateEnd,
                row.Current, row.Instrument))
    connection.commit()
except Error as e:
            print("Error while executing sql", e)


schema = [['Date Time','Date and time of measurement', 'datetime'], ['NOx','Concentration of oxides of nitrogen', '㎍/m3'],
            ['NO2','Concentration of nitrogen dioxide', '㎍/m3'], ['NO','Concentration of nitric oxide', '㎍/m3'],
           ['SiteID','Site ID for the station', 'integer'], ['PM10','Concentration of particulate matter <10 micron diameter', '㎍/m3'],
            ['NVPM10',' Concentration of non - volatile particulate matter <10 micron diameter', '㎍/m3'], ['VPM10','Concentration of volatile particulate matter <10 micron diameter', '㎍/m3'],
             ['NVPM2.5', 'Concentration of non volatile particulate matter <2.5 micron diameter', '㎍/m3'], ['PM2.5', 'Concentration of particulate matter <2.5 micron diameter', '㎍/m3'],
             ['VPM2.5', 'Concentration of volatile particulate matter <2.5 micron diameter', '㎍/m3'], ['CO', 'Concentration of carbon monoxide', 'mg/m3'],
             ['O3', 'Concentration of ozone', '㎍/m3'], ['SO2', 'Concentration of sulphur dioxide', '㎍/m3'], ['Temperature', 'Air temperature', '°C'],
             ['RH', 'Relative Humidity', '%'], ['Air Pressure', 'Air Pressure', 'mbar'], ['Location', 'Text description of location', 'text'],
             ['geo_point_2d', 'Latitude and longitude', 'geo point'], ['DateStart', 'The date monitoring started', 'datetime'],
             ['DateEnd', 'The date monitoring ended', 'datetime'], ['Current', 'Is the monitor currently operating', 'text'],
             ['Instrument Type', 'Classification of the instrument', 'text']]
schema_data = pd.DataFrame(schema, columns = ['measure', 'desc', 'units'])


try:

    sql = '''INSERT INTO schema_table(`Measure`,`unit`,`Description`) VALUES ('Date Time','Date and time of measurement', 'datetime'), ('NOx','Concentration of oxides of nitrogen', '㎍/m3'),
        ('NO2','Concentration of nitrogen dioxide', '㎍/m3'), ('NO','Concentration of nitric oxide', '㎍/m3'),
       ('SiteID','Site ID for the station', 'integer'), ('PM10','Concentration of particulate matter <10 micron diameter', '㎍/m3'),
        ('NVPM10',' Concentration of non - volatile particulate matter <10 micron diameter', '㎍/m3'), ('VPM10','Concentration of volatile particulate matter <10 micron diameter', '㎍/m3'),
         ('NVPM2.5', 'Concentration of non volatile particulate matter <2.5 micron diameter', '㎍/m3'), ('PM2.5', 'Concentration of particulate matter <2.5 micron diameter', '㎍/m3'),
         ('VPM2.5', 'Concentration of volatile particulate matter <2.5 micron diameter', '㎍/m3'), ('CO', 'Concentration of carbon monoxide', 'mg/m3'),
         ('O3', 'Concentration of ozone', '㎍/m3'), ('SO2', 'Concentration of sulphur dioxide', '㎍/m3'), ('Temperature', 'Air temperature', '°C'),
         ('RH', 'Relative Humidity', '%'), ('Air Pressure', 'Air Pressure', 'mbar'), ('Location', 'Text description of location', 'text'),
         ('geo_point_2d', 'Latitude and longitude', 'geo point'), ('DateStart', 'The date monitoring started', 'datetime'),
         ('DateEnd', 'The date monitoring ended', 'datetime'), ('Current', 'Is the monitor currently operating', 'text'),
         ('Instrument Type', 'Classification of the instrument', 'text');'''
    cursor.execute(sql)
    connection.commit()
except Error as e:
            print("Error while executing sql", e)
print('Im working perfectly')