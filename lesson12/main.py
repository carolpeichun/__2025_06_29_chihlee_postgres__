import streamlit as st
import datasource1 as ds

st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年每日各站進出站人數")
st.subheader("進出站人數顯示區")

@st.cache_data      # 使用快取資源以提高效能(第一次連線已cache暫存,不需要再一直連線)
def get_stations():
    """取得所有車站資料"""
    return ds.get_all_stations()

@st.cache_data
def get_date_range():
    """取得日期範圍"""
    return ds.get_min_and_max_date()

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

date_range = get_date_range()
if date_range is None:
    st.error("無法取得日期範圍，請稍後再試。")
    st.stop()   

import datetime

def _to_date(d):
    if isinstance(d, datetime.date):
        return d
    if isinstance(d, datetime.datetime):
        return d.date()
    if isinstance(d, str):
        # 支援常見格式: ISO (YYYY-MM-DD) 或 YYYY/MM/DD
        try:
            return datetime.date.fromisoformat(d)
        except Exception:
            try:
                return datetime.datetime.strptime(d, "%Y-%m-%d").date()
            except Exception:
                try:
                    return datetime.datetime.strptime(d, "%Y/%m/%d").date()
                except Exception:
                    raise ValueError(f"無法解析日期: {d}")
    raise ValueError(f"不支援的日期格式: {type(d)}")

min_date = _to_date(date_range[0])
max_date = _to_date(date_range[1])

# 在 sidebar 顯示可選日期範圍（只允許選擇 min_date ~ max_date 之間的日期）
selected_range = st.sidebar.date_input(
    "請選擇日期範圍",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(selected_range, tuple) and len(selected_range) == 2:
    selected_start, selected_end = selected_range
else:
    selected_start = selected_end = selected_range


# 請使用datasource1.get_station_data_by_date() 取得車站資料,並顯示資料
st.write("您選擇的車站:", station )
#st.write("日期範圍:", min_date, "至", max_date)
st.write("選取的日期:", selected_start, "至", selected_end)

station_data = ds.get_station_data_by_date(station, selected_start, selected_end)

if station_data is None:
    st.error("無法取得車站資料，請稍後再試。")
    st.stop()

# 將資料轉為 pandas DataFrame（如果尚未是 DataFrame）
import pandas as pd
if not isinstance(station_data, pd.DataFrame):
    try:
        station_df = pd.DataFrame(station_data)
    except Exception:
        st.error("取得的車站資料格式不正確。")
        st.stop()
else:
    station_df = station_data.copy()

# 調整欄位顯示名稱（將常見欄位轉為中文名稱，其他欄位做格式化顯示）
_mapping = {
    'date': '日期',
    'station': '車站',
    'entry': '進站',
    'entries': '進站',
    'in': '進站',
    'boardings': '進站',
    'exit': '出站',
    'exits': '出站',
    'out': '出站',
    'alightings': '出站',
    'total': '合計',
    'count': '數量'
}
new_cols = {}
for col in station_df.columns:
    key = str(col).lower().strip()
    mapped = None
    for k, v in _mapping.items():
        if k == key or k in key:
            mapped = v
            break
    if mapped is None:
        mapped = str(col).replace('_', ' ').strip().title()
    new_cols[col] = mapped

station_df = station_df.rename(columns=new_cols)

# 顯示資料並提供下載 CSV 的功能
st.dataframe(station_df)

try:
    csv_bytes = station_df.to_csv(index=False).encode('utf-8-sig')
    fname = f"{station}_{selected_start}_{selected_end}.csv"
    st.download_button("下載 CSV", data=csv_bytes, file_name=fname, mime="text/csv")
except Exception:
    # 若無法轉為 CSV，仍顯示資料但不提供下載
    pass