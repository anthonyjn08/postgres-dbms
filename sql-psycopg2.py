import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Marvin Gaye" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Marvin Gaye"])

# Query 4 - select only by the "ArtistId" #104 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [104])

# Query 5 - select on the albums with "ArtistId" #104 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [104])

# Query 6 - select all tracks where the composer is "Marvin Gaye" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Marvin Gaye"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)