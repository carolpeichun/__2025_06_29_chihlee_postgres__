#請幫我自訂一個function
#連線至postgres DB
#建立連線環境參數的樣版
#請使用繁體中文註解

import psycopg2

def create_connection_params():
    """
    建立連線至PostgreSQL資料庫的環境參數樣板。
    
    回傳一個包含連線參數的字典。
    """
    params = {
        'dbname': 'postgres',  # 資料庫名稱
        'user': 'postgres',          # 使用者名稱
        'password': 'raspberry',      # 密碼
        'host': 'host.docker.internal',   # 主機名稱
        'port': '5432'                    # 連接埠
    }
    return params

def connect_to_db(params):
    """
    連線至PostgreSQL資料庫。

    :param params: 包含連線參數的字典
    :return: 資料庫連線物件或None
    """
    try:
        connection = psycopg2.connect(**params)
        print("成功連線至資料庫。")
        return connection
    except Exception as e:
        print(f"連線至資料庫時發生錯誤: {e}")
        return None

def close_connection(connection):
    """
    關閉資料庫連線。

    :param connection: 資料庫連線物件
    """
    if connection:
        connection.close()
        print("資料庫連線已關閉。")

def main():
    # 建立連線參數
    params = create_connection_params()

    # 連線至資料庫
    connection = connect_to_db(params)

    # 在這裡執行資料庫操作

    # 關閉資料庫連線
    close_connection(connection)

if __name__ == "__main__":
    main()