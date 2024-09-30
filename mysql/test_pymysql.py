# pip install mysql

import pymysql

# 데이터베이스 연결 설정 (DB Connection)
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='class-password',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)      # 값을 딕셔너리 형태로 저장해달라 (안그러면 키값 없어서 조회할 때 불편함)


## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    connection.close()


# 데이터를 딕셔너리 형태로 저장 (전체 데이터 가져오기 fetchall)
customers = cursor.fetchall()
print("customers: ", customers)

# 하나의 데이터만 가져와서 보기 fetchone
customers2 = cursor.fetchone()
print("customers2: ", customers2)

'''
- **`charset='utf8mb4'`**
    - 이 설정은 데이터베이스 연결에 사용되는 문자 집합을 지정합니다.
    - **`utf8mb4`**는 MySQL에서 유니코드를 완벽하게 지원하기 위한 문자 집합으로, 이모지를 포함한 모든 유니코드 문자를 지원합니다.
    - 데이터베이스에 다양한 언어의 문자 데이터를 저장하거나, 이모지 등의 4바이트 유니코드 문자를 사용할 경우 이 설정이 필요합니다.


- **`cursorclass`**
    1. **Default Cursor (`pymysql.cursors.Cursor`)**: 기본 커서 클래스로, 결과를 튜플 형식으로 반환합니다. 각 행은 값들의 튜플로 나타나며, 열 이름 정보는 포함하지 않습니다.
    2. **DictCursor (`pymysql.cursors.DictCursor`)**: 이 커서 클래스는 결과를 딕셔너리 형식으로 반환합니다. 각 행은 열 이름을 키로 하고 해당 데이터를 값으로 하는 딕셔너리로 나타납니다. 이는 결과를 처리할 때 열 이름으로 데이터에 접근할 수 있게 해줘 편리합니다.
    3. **SSCursor (`pymysql.cursors.SSCursor`)**: 서버 사이드 커서로, 큰 결과 집합을 처리할 때 유용합니다. 이 커서는 모든 결과를 한 번에 메모리에 로드하지 않고, 필요할 때마다 서버에서 행을 가져옵니다.
    4. **SSDictCursor (`pymysql.cursors.SSDictCursor`)**: 서버 사이드 딕셔너리 커서로, **`SSCursor`**의 기능에 딕셔너리 형식의 결과 반환을 추가합니다. 큰 데이터 집합에서 열 이름으로 데이터에 접근해야 할 때 유용합니다.
    5. **NamedTupleCursor (`pymysql.cursors.NamedTupleCursor`)**: 이 커서는 결과를 명명된 튜플(namedtuple) 형식으로 반환합니다. 각 행은 필드 이름으로 접근 가능한 튜플로 나타납니다. 이는 열 이름으로 데이터에 접근할 수 있으면서도 튜플의 간결함을 유지합니다.

- **`cursorclass=pymysql.cursors.DictCursor`**
    - 이 설정은 데이터베이스 쿼리의 결과를 어떻게 반환할지 결정합니다.
    - 기본적으로 PyMySQL은 쿼리 결과를 튜플(tuple) 형태로 반환합니다.
    - **`DictCursor`**를 사용하면 쿼리 결과를 딕셔너리(dictionary) 형태로 받을 수 있어, 각 열의 이름으로 결과에 접근할 수 있습니다. 이는 결과 데이터를 처리할 때 더 직관적이고 편리할 수 있습니다.

- **`DictCursor`**와 **`SSDictCursor`**
    
    **`DictCursor`**와 **`SSDictCursor`**는 PyMySQL에서 사용되는 두 종류의 커서입니다. 두 커서 모두 쿼리 결과를 딕셔너리 형식으로 반환하는 것은 같지만, 데이터를 처리하는 방식에서 차이가 있습니다.
    
    - **`DictCursor`**: 이 커서는 쿼리 결과를 딕셔너리 형식으로 반환합니다. 이 경우, 쿼리의 전체 결과가 클라이언트의 메모리에 한 번에 로드됩니다. 이 방식은 결과 집합이 상대적으로 작을 때 효과적입니다.
    - **`SSDictCursor` (Server-Side DictCursor)**: 이 커서도 결과를 딕셔너리 형식으로 반환하지만, 서버 사이드 커서의 특징을 가집니다. 즉, 쿼리의 전체 결과를 한 번에 메모리에 로드하지 않고, 필요할 때마다 서버에서 데이터를 가져옵니다. 이는 큰 결과 집합을 처리할 때 메모리 사용량을 줄이고 효율을 높이는 데 유용합니다.
    
    결론적으로, 작은 데이터 세트를 다룰 때는 **`DictCursor`**를 사용하는 것이 좋고, 큰 데이터 세트를 다룰 때는 **`SSDictCursor`**를 사용하는 것이 더 효율적입니다. 그러나 **`SSDictCursor`**는 데이터를 서버에서 점진적으로 가져오기 때문에, 작은 데이터 세트에 대해서도 사용할 수 있지만, 이 경우에는 **`DictCursor`**에 비해 약간의 오버헤드가 발생할 수 있습니다. 따라서 적절한 커서 선택은 사용 사례와 데이터 세트의 크기에 따라 달라질 수 있습니다.

'''


## 2. INSERT INTO

def add_customer():
    cursor = connection.cursor()
    name = 'emma'
    family_name = 'wang'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES ({10000}, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()
    connection.close() # 데이터베이스 연결 종료

add_customer()



## 3. UPDATE INTO
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_emma'
    contactLastName = 'update_wang'

    sql = f"UPDATE customers SET customerName='{update_name}', contactLastname='{contactLastName}' WHERE customerNumber=1000"

    cursor.execute(sql)
    connection.commit()
    cursor.close()

update_customer()



## 4. DELETE FROM
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()


