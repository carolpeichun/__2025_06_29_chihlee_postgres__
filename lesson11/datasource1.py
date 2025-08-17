import psycopg2
from dotenv import load_dotenv  # 用於讀取環境變數(自動去讀取 .env 檔案)
import os   # 用於讀取環境變數(如HOST, DATABASE等)

load_dotenv()

#建立一個Function, 功能是取得所有台鐵車站資訊的站點名稱
#try except finally 用於處理例外情況和確保資源釋放
def get_all_stations():
    """取得所有台鐵車站資訊的站點名稱
    Returns:
        list: 包含所有站點名稱的列表，連線失敗時回傳 None
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432"
        )
        print("資料庫連線成功")
        cursor = conn.cursor()
        query = """
        SELECT "stationName"
        FROM "台鐵車站資訊";
        """
        cursor.execute(query)
        result = [row[0] for row in cursor.fetchall()]        
        return result
    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        # 確保資源正確釋放
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


def get_min_and_max_date():
    """取得每日各站進出站人數的最小和最大日期
    Returns:
        list: 包含最小和最大日期的列表，連線失敗時回傳 None
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            port="5432"
        )
        print("資料庫連線成功")
        cursor = conn.cursor()
        query = """
        SELECT MIN("日期") AS min_date, MAX("日期") AS max_date
        FROM public."每日各站進出站人數";
        """
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except psycopg2.Error as e:
        print(f"資料庫連線或查詢失敗：{e}")
        return None
    except Exception as e:
        print(f"發生未預期的錯誤：{e}")
        return None
    finally:
        # 確保資源正確釋放
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

