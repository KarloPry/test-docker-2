import pymysql

# Connect to the database
connection = pymysql.connect(host='sql-py',
                             port=3306,
                             user='root',
                             password='my-secret-pw',
                             db='testdb')
# CLI to enter the query and never closes until the user enters 'exit'
print("Connected to the database")
while True:
    try:
        query = input("$ ")
        if query == 'exit':
            break
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    except:
        continue
connection.close()
