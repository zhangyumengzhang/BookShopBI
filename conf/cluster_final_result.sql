create table final_result(
  userId STRING,
  clusterId INT,
  subTotal DOUBLE,
  ordersCount DOUBLE,
  sessionCount DOUBLE
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';