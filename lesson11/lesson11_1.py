import streamlit as st
import datasource1 as ds

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年每日各站進出站人數")
st.subheader("進出站人數顯示區")

@st.cache_data      # 使用快取資源以提高效能(第一次連線已cache暫存,不需要再一直連線)
def get_stations():
    """取得所有車站資料"""
    return ds.get_all_stations()

stations = get_stations()
if stations is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()

#sidebar要先選示常用的車站名稱
#使用者可以很快的選擇
#如果不常用的車站名稱,再使用selectbox選擇
common_stations = ['臺北','桃園','新竹','台中','臺南','高雄','其它']

choice = st.sidebar.radio("快速選擇常用車站", common_stations)

if choice == "其它":
    station = st.sidebar.selectbox(
        "請選擇車站",
        stations,
    )
else:
    station = choice

st.write("您選擇的車站:", station )