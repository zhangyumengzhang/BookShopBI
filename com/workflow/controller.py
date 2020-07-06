import importlib
import sys
import datetime
from xml.etree import ElementTree as ET
from com.utils.py_env import PROJECT_CONF_DIR
import os

if __name__ == '__main__':
    importlib.reload(sys)
    today = datetime.date.today()
    yestoday = today + datetime.timedelta(-1)

    # 获取昨天的日期
    dt = yestoday.strftime('%Y-%m-%d')

    # 加载主配置文件
    xmlTree = ET.parse(PROJECT_CONF_DIR + "workflow.xml")

    # 获得所有task节点
    workflow = xmlTree.findall('./task')

    for task in workflow:
        # 获得模块名称
        moduleName = task.text

        if (moduleName == "exe_hive"):
            shell = "python " + moduleName + ".py " + task.attrib.get('type') + " " + dt
            os.system(shell)
        else:
            shell = "python " + moduleName + ".py " + dt
            os.system(shell)
