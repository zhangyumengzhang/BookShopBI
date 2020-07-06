from com.utils.HiveUtil import HiveUtil


def prepare_normaliz(start_time, end_time):
    # 提取数据维度
    hql_1 = "insert overwrite table user_dimension select t1.userId,t1.avg,t2.ordercount,t3.sessioncount from " \
            "(select userId,avg(subTotal) avg from bx_orders where dt<=" + start_time + " and dt>=" + end_time + " group by userId) t1 " \
            "join (select userId,count(orderId) ordercount from bx_orders where dt<="+start_time+" and dt>="+end_time+" group by userId) t2 on t1.userId=t2.userId " \
            "join (select userId,count(sessionId) sessioncount from clickstream_log where dt<="+start_time+" and dt>="+end_time+" group by userId) t3 on t1.userId=t3.userId";
    HiveUtil.execute_shell(hql_1)

    # 将user_dimension数据导入到cluster_input中，去掉CustomerId
    hql_2 = "insert overwrite table cluster_input select subTotal,orderCount,sessionCount from user_dimension";
    HiveUtil.execute_shell(hql_2)

    # 数据归一化处理
    hql_3 = "insert overwrite table cluster_input " \
            "select (subTotal-avg_subTotal)/std_subTotal,(ordersCount-avg_ordersCount)/std_ordersCount,(sessionCount-avg_sessionCount)/std_sessionCount from cluster_input " \
            "join (select std(subTotal) std_subTotal,std(ordersCount) std_ordersCount,std(sessionCount) std_sessionCount from cluster_input) t1 on 1=1 " \
            "join (select avg(subTotal) avg_subTotal,avg(ordersCount) avg_ordersCount,avg(sessionCount) avg_sessionCount from cluster_input) t2 on 1=1";
    HiveUtil.execute_shell(hql_3)

    #计算相关系数矩阵
    hql_4="select (avg(subTotal*subTotal)-avg(subTotal)*avg(subTotal))/(std(subTotal)*std(subTotal))," \
          "(avg(subTotal*ordersCount)-avg(subTotal)*avg(ordersCount))/(std(subTotal)*std(ordersCount))," \
          "(avg(subTotal*sessionCount)-avg(subTotal)*avg(sessionCount))/(std(subTotal)*std(sessionCount))," \
          "(avg(ordersCount*subTotal)-avg(ordersCount)*avg(subTotal))/(std(ordersCount)*std(subTotal))," \
          "(avg(ordersCount*ordersCount)-avg(ordersCount)*avg(ordersCount))/(std(ordersCount)*std(ordersCount))," \
          "(avg(ordersCount*sessionCount)-avg(ordersCount)*avg(sessionCount))/(std(ordersCount)*std(sessionCount))," \
          "(avg(sessionCount*subTotal)-avg(sessionCount)*avg(subTotal))/(std(sessionCount)*std(subTotal))," \
          "(avg(sessionCount*ordersCount)-avg(sessionCount)*avg(ordersCount))/(std(sessionCount)*std(ordersCount))," \
          "(avg(sessionCount*sessionCount)-avg(sessionCount)*avg(sessionCount))/(std(sessionCount)*std(sessionCount)) " \
          "from cluster_input";
    HiveUtil.execute_shell(hql_4)