import pymysql

def execute_query(connection, query, args=None):  # 변수 여러개 받을 수 있게

    with connection.cursor() as cursor:    # cursor의 context 유지
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()

def main():
    connection = pymysql.connect(host='localhost',
                                 user='username',
                                 password='password',
                                 db='database_name',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        # SELECT 연산
        result = execute_query(connection, "SELECT * FROM table_name")
        print("SELECT 연산 결과:")
        for row in result:
            print(row)

        # INSERT 연산
        execute_query(connection, "INSERT INTO table_name (column1, column2) VALUES (%s, %s)", ('data1', 'data2'))
        print("INSERT 연산 수행됨.")

        # UPDATE 연산
        execute_query(connection, "UPDATE table_name SET column1=%s WHERE column2=%s", ('new_data', 'criteria'))
        print("UPDATE 연산 수행됨.")

        # DELETE 연산
        execute_query(connection, "DELETE FROM table_name WHERE column_name=%s", ('criteria',))
        print("DELETE 연산 수행됨.")

    finally:
        connection.close()

if __name__ == "__main__":
    main()



results = execute_query(connection, "SELECT * FROM table_name")

# 함수로 만들고 원하는 결과를 한꺼번에 불러올 수 있음

for i in results:
    print(i)