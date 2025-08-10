import datasource

def main():   
    # 呼叫get_all_stations函式
    results = datasource.get_all_stations()
    if results:
        print("台鐵車站資訊的站點名稱:") 
        for station in results:
            print(station) 
    else:
        print("無法取得車站資料")

if __name__ == "__main__":
    main()