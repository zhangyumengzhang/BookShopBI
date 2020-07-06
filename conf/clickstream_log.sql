CREATE TABLE clickstream_log(
  ipAddress STRING,
  uniqueId STRING,
  url STRING,
  sessionId STRING,
  sessionTimes INT,
  areaAddress STRING,
  localAddress STRING,
  browserType STRING,
  operationSys STRING,
  referUrl STRING,
  receiveTime STRING,
  userId STRING,
  csvp INT
)
PARTITIONED BY (dt STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';