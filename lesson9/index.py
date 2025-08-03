import db

def main():
    all_stations = get_all_stations()
    print("台鐵車站資訊的站點名稱:")
    for station in all_stations:
        print(station)

if __name__ == "__main__":
    main()