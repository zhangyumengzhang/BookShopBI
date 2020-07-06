create table cluster_result(
  clusterId INT,
  subTotal DOUBLE,
  ordersCount DOUBLE,
  sessionCount DOUBLE
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';