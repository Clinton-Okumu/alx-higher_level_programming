USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS temperature (
    city VARCHAR(50),
    temperature FLOAT(6,2)
);

LOAD DATA INFILE 'temperatures.sql'
INTO TABLE temperature
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(city, temperature);

SELECT city, AVG(temperature) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
