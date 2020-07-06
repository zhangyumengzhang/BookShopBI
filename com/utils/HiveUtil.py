# -*- coding:UTF-8 -*-
from com.utils.py_env import HIVE_PATH
import subprocess


class HiveUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def execute_shell(hql, hive_path=HIVE_PATH):
        # 将hql语句进行字符串转义
        # hql = hql.replace("\"", "'")
        # 执行查询，并取得执行的状态和输出
        status, output = subprocess.getstatusoutput(cmd=hive_path + "hive -S -e " + hql)

        if status != 0:
            print("failed:the number is " + str(status))
            print(output)
            return None
        else:
            print("success")
        output = str(output).split("\n")

        return output
