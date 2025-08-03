import psycopg2
#請幫我建立一個function
#傳入connection參數
#建立一個Cursor物件
#執行一個簡單的SQL查詢
#並返回查詢結果

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result

def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="postgres",
        user="postgres",
        password="raspberry",
        port="5432"
    )
    return conn


def main():
    conn = create_connection()
    if conn:
        print("成功連接到資料庫！")
        query = """        
        SELECT count(*) AS "筆數"
        FROM "台鐵車站資訊";
        """
        result = execute_query(conn, query)
        print("查詢結果:", result)
        conn.close()
    else:
        print("無法連接到資料庫，請檢查連接參數。")
        return

if __name__ == "__main__":
    main()