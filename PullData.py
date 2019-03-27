import psycopg2
try:
   connection = psycopg2.connect(user="",
                                 password="",
                                 host="",
                                 port="",
                                 database="")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT result FROM dev_raw limit 10"
   cursor.execute(postgreSQL_select_Query)
   spot_table = cursor.fetchall()

   print("Print each row and it's columns values")
   for row in spot_table:
       print('Spot Occupancy Result = ', row[0])
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
