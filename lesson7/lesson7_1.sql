SELECT
  "stationCode",
  "stationName",
  "name"
FROM
  "台鐵車站資訊"
WHERE
  "stationAddrTw" LIKE '基隆市%';

SELECT 
    COUNT(*) AS station_count,
    STRING_AGG("stationName", ', ') AS station_names
FROM 
    "台鐵車站資訊"
WHERE 
    "stationAddrTw" LIKE '%基隆%';

SELECT * 
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON 車站代碼 = "stationCode"