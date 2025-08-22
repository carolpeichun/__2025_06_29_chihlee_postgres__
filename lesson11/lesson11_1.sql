SELECT
  d."日期"          AS date,
  s."stationName"   AS station,
  d."進站人數"      AS in_count,
  d."出站人數"      AS out_count
FROM "每日各站進出站人數" AS d
JOIN "台鐵車站資訊"      AS s
  ON d."車站代碼" = s."stationCode"
WHERE s."stationName" = '基隆'
  AND d."日期" = '2023-01-01';

SELECT MIN("日期") AS min_date, MAX("日期") AS max_date
        FROM public."每日各站進出站人數";

SELECT
  d."日期"        AS date,
  s."stationName" AS station,
  d."進站人數"    AS in_count,
  d."出站人數"    AS out_count
FROM "每日各站進出站人數" AS d
JOIN "台鐵車站資訊" AS s
  ON d."車站代碼" = s."stationCode"
WHERE s."stationName" = '基隆'
  AND d."日期" BETWEEN '2023-01-01' AND '2023-01-31'
ORDER BY d."日期";