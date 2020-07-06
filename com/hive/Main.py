# -*- coding:UTF-8 -*-
import datetime
import com.hive.buildHQL as bq
from com.utils.HiveUtil import HiveUtil

if __name__ == '__main__':
    #today = datetime.date.today() + datetime.timedelta(-1)
   # dt = today.strftime('%Y-%m-%d')
    dt='2017-06-27'
    hqls = bq.resolve_conf("analysis", dt)
    hqls += bq.resolve_conf("etl_data_dedup", dt)

    # print hqls[3]
    # HiveUtil.execute_shell(hqls[3])

    for hql in hqls:
        print(hql)

        HiveUtil.execute_shell(hql)
