CREATE TABLE user_dimension(
  customerId STRING,
  subTotal DOUBLE,
  ordersCount DOUBLE,
  sessionCount DOUBLE
) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';