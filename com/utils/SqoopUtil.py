# -*- coding:UTF-8 -*-
from com.utils.py_env import SQOOP_PATH
import subprocess


class SqoopUtil(object):
    '''
    sqoop operation
    '''

    def __init__(self):
        pass

    @staticmethod
    def execute_shell(shell, sqoop_path=SQOOP_PATH):
        # 执行传入的shell命令
        status, output = subprocess.getstatusoutput(sqoop_path + shell)
        if status != 0:
            print("failed:the number is " + str(status))
            print(output)
            return None
        else:
            print("success")
            output = str(output).split("\n")
        return output
