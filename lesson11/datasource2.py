from dotenv import load_dotenv  # 用於讀取環境變數(自動去讀取 .env 檔案)
import os   # 用於讀取環境變數(如HOST, DATABASE等)

load_dotenv()

#建立一個Function, 功能是取得所有台鐵車站資訊的站點名稱
#try except finally 用於處理例外情況和確保資源釋放
def get_all_stations():
    """取得所有台鐵車站資訊的站點名稱
    Returns:
    list: 包含所有站點的列表，元素為 dict e.g. {'name': '台北'}；連線失敗時回傳 None
    """
    try:
        try:
            import psycopg2
        except ImportError:
            print("psycopg2 not installed; 無法連接資料庫")
            return None

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
        # 轉換成 list[dict] 以符合前端使用預期
        result = [{'name': row[0]} for row in cursor.fetchall()]
        return result
    except Exception as e:
        print(f"資料庫連線或查詢失敗或發生錯誤：{e}")
        return None
    finally:
        # 確保資源正確釋放
        if 'cursor' in locals():
            try:
                cursor.close()
            except Exception:
                pass
        if 'conn' in locals():
            try:
                conn.close()
            except Exception:
                pass


def get_common_stations(limit=5):
    """取得常用車站（從所有車站取前幾筆並以 dict{name: ...} 回傳）
    Returns:
        list: 若成功回傳像 [{'name': '台北'}, ...] 的列表；失敗回傳 None
    """
    try:
        all_stations = get_all_stations()
        if all_stations is None:
            return None
        # all_stations 已經是 list[dict]，直接取前面幾筆
        common = all_stations[:limit]
        return common
    except Exception as e:
        print(f"取得常用車站時發生錯誤：{e}")
        return None
