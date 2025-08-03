SELECT count(*) AS 筆數
FROM "台鐵車站資訊"

SELECT count(name) AS 台北站數
FROM "台鐵車站資訊"
WHERE "stationAddrTw" LIKE '臺北%'

SELECT *
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON 車站代碼 = "stationCode"
WHERE "stationName" = '基隆'

/*
 * 全省各站點2022年進站總人數
 */

SELECT name AS 站名, count("name") AS 筆數, SUM(進站人數) AS "2022進站總人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON 車站代碼 = "stationCode"
WHERE 日期 BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY 站名;

SELECT name AS 站名, date_part('year', 日期) AS 年份, count("name") AS 筆數, SUM(進站人數) AS 進站總人數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON 車站代碼 = "stationCode"
GROUP BY 站名, 年份;

SELECT name AS 站名, date_part('year', 日期) AS 年份, count("name") AS 筆數, SUM(進站人數) AS 進站總人數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON 車站代碼 = "stationCode"
WHERE name = '基隆'
GROUP BY 站名, 年份
HAVING SUM(進站人數) > 1000000
ORDER BY 進站總人數 DESC;

/*
 * 全省各站點2022年進站總人數大於5佰萬人的站點
 */

SELECT
    t."stationName" AS "車站名稱",
    SUM(p."進站人數") AS "2022年進站總人數"
FROM "每日各站進出站人數" p
LEFT JOIN "台鐵車站資訊" t ON p."車站代碼" = t."stationCode"
WHERE DATE_PART('year', p."日期") = 2022
GROUP BY t."stationCode", t."stationName"
HAVING SUM(p."進站人數") > 5000000
ORDER BY SUM(p."進站人數") DESC;

/*
*基隆火車站2020,2021,2022,每年進站人數
*若AI一直給錯誤的(資料表沒有的欄位), 確認AI讀到的資料表欄位是否正確!
*問：請幫我取出基隆火車站2020,2021,2022每年進站人數, 並請使用postgreSQL語法
*/

SELECT 
	s."stationName" AS 站名,
	EXTRACT(YEAR FROM d.日期) AS 年份,
  	SUM(d.進站人數) AS 年進站人數
FROM "每日各站進出站人數" d
JOIN "台鐵車站資訊" s
  ON d.車站代碼 = s."stationCode"
WHERE s."stationName" = '基隆'
  AND EXTRACT(YEAR FROM d.日期) IN (2020, 2021, 2022)
GROUP BY 站名, 年份
ORDER BY 年份;

/*
*基隆火車站,臺北火車站2020,2021,2022,每年進站人數
*問：請幫我取出基隆火車站,臺北火車站2020,2021,2022每年進站人數, 並請使用postgreSQL語法
*/

SELECT 
  s."stationName" AS 站名,
  EXTRACT(YEAR FROM d.日期) AS 年份,
  SUM(d.進站人數) AS 年進站人數
FROM "每日各站進出站人數" d
JOIN "台鐵車站資訊" s
  ON d.車站代碼 = s."stationCode"
WHERE s."stationName" IN ('基隆', '臺北')
  AND EXTRACT(YEAR FROM d.日期) IN (2020, 2021, 2022)
GROUP BY 站名, 年份
ORDER BY 站名, 年份;

/*
*查詢 2022 年平均每日進站人數超過 2 萬人的站點
*問：請幫我取出2022年平均每日進站人數超過 2 萬人的站點, 並請使用postgreSQL語法
*/

SELECT 
  s."stationName" AS "站名",
  ROUND(AVG(d."進站人數")) AS "2022平均每日進站人數"
FROM "每日各站進出站人數" d
JOIN "台鐵車站資訊" s
  ON d."車站代碼" = s."stationCode"
WHERE EXTRACT(YEAR FROM d."日期") = 2022
GROUP BY "站名"
HAVING AVG(d."進站人數") > 20000
ORDER BY "2022平均每日進站人數" DESC;

