import pyodbc 

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=cs_coredb_mlau1_hq;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT MonitorDataID, TripNumber, SerialNumber, ResetCount FROM MonitorDataTable')

for row in cursor:
    print('row = %r' % (row,))