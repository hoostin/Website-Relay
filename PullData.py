import psycopg2
try:
   connection = psycopg2.connect(user="",
                                  password="",
                                  host="",
                                  port="",
                                  database="")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT * FROM pg_catalog.pg_tables"
   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   spot_table = cursor.fetchall()

   print("Print each row and it's columns values")
   for row in spot_table:
       print("parkingSpot = ", row[0])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
