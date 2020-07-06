from com.utils import HiveUtil


def extract_data(start, end):
    hql = "insert into table conversion_input partition (dt='" + start + "-" + end + "') " \
           "select url,uuid,sessionid,csvp from clickstream_log where where dt>= " + start + " and dt<= " + end

    HiveUtil.execute_shell(hql)
