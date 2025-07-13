## 問題2. 查詢全世界2020年的總確診數

```sql
SELECT  
  SUM(新增確診數) AS 總確診數
FROM world
WHERE 洲名 = '全球' AND 日期 BETWEEN '2020-01-01' AND '2020-12-31';
```

### **🚩 RESULT**

|總確診數|
|----|
|83044990|


/*建立Student資料*/
CREATE TABLE student(
student_id serial,
name varchar(20),
major varchar(20),
PRIMARY KEY(student_id)
);

/*新增資料*/
INSERT INTO student VALUES(1, '小白', '歷史')
INSERT INTO student VALUES(2, '小黑', '生物')
INSERT INTO student VALUES(3, '小綠', NULL)

INSERT INTO student(name,major) VALUES('小綠',NULL);

