import streamlit as st
import datasource2 as ds

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年每日各站進出站人數")
st.subheader("進出站人數顯示區")

@st.cache_data      # 使用快取資源以提高效能(第一次連線已cache暫存,不需要再一直連線)
def get_stations():
    """取得所有車站資料"""
    return ds.get_all_stations()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料")
    st.stop()

#sidebar要先選示常用的車站名稱
#使用者可以很快的選擇
#如果不常用的車站名稱,再使用selectbox選擇
st.sidebar.subheader("常用車站")
# 從已快取的 stations 直接取出前幾筆作為常用車站，避免再次呼叫資料庫
common_stations = stations[:5] if stations else None
if common_stations is None:
    st.sidebar.error("無法取得常用車站資料")
else:
    common_station_names = [station['name'] for station in common_stations]
    common_station_names.insert(0, "請選擇常用車站")
    common_station = st.sidebar.selectbox(
        "請選擇常用車站",
        common_station_names,
    )

    if common_station != "請選擇常用車站":
        station = next((s for s in stations if s['name'] == common_station), None)
        if station:
            st.write("您選擇的常用車站:", station['name'])
        else:
            st.error("無法找到所選的常用車站")
    else:
        st.write("請選擇常用車站以顯示相關資訊")
        
station_names = [s['name'] for s in stations]
station = st.sidebar.selectbox(
    "請選擇車站",
    station_names,
)

st.write("您選擇的車站:", station )
