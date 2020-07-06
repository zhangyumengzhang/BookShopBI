# -*- coding:UTF-8 -*-

import com.sqoop.buildExport as exp
import com.sqoop.buildImport as imp
from com.utils.SqoopUtil import SqoopUtil
import datetime

if __name__ == '__main__':
    #today = datetime.date.today() + datetime.timedelta(-1)
    #dt = today.strftime('%Y-%m-%d')
    dt='2017-06-27'
    cmds = imp.resolve_conf(dt)

    for cmd in cmds:
        print(cmd)
       # 执行导入过程
        SqoopUtil.execute_shell(cmd)
