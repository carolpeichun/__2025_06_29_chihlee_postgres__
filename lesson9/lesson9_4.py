import psycopg2

def create_connection():
    conn = psycopg2.connect(
        host="host.docker.internal",
        database="postgres",
        user="postgres",
        password="raspberry",
        port="5432"
    )
    return conn

#建立一個Function, 功能是取得所有台鐵車站資訊的站點名稱
def get_all_stations():
    """
    取得所有台鐵車站的名稱。

    此函式會連接至資料庫，查詢「台鐵車站資訊」資料表中的所有車站名稱，並以列表形式回傳查詢結果。

    回傳值:
        list: 包含所有車站名稱的查詢結果，每一項為一個字串。
    """
    conn = create_connection()  # Conn實體
    cursor = conn.cursor()      # Cursor實體
    # SQL語法
    query = """
    SELECT "stationName"
    FROM "台鐵車站資訊";
    """
    cursor.execute(query)
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()  # 關閉Cursor
    conn.close()    # 關閉Conn
    return result

def main():
    all_stations = get_all_stations()
    print("台鐵車站資訊的站點名稱:")
    for station in all_stations:
        print(station)

if __name__ == "__main__":
    main()