# -*- coding:UTF-8 -*-
from xml.etree import ElementTree
import com.utils.py_env as env


#
# 数据导出：生成“将数据从Hive导出到MySql”的命令。
#
# 1.全部导出
# Sqoop export --connect  jdbc:mysql://127.0.0.1:3306/dbname
#   --username mysql(mysql用户名) --password 123456(密码)
#   --table  student(mysql上的表) --hcatalog-database sopdm(hive上的schema)
#   --hcatalog-table student(hive上的表)
#
# 2.部分导出
# Sqoop export --connect  jdbc:mysql://127.0.0.1:3306/dbname
#   --username mysql(mysql用户名) --password 123456(密码)
#   --table  student(mysql上的表) --columns "id,name,age"  --hcatalog-database sopdm(hive上的schema)
#   --hcatalog-table student(hive上的表)

def resolve_conf(dt):
    # 导出配置文件路径
    conf_file = env.PROJECT_CONF_DIR + "export.xml"

    # 解析配置文件
    xml_tree = ElementTree.parse(conf_file)

    # 获取sqoop-shell元素
    shells = xml_tree.findall('./sqoop-shell')

    # 用来保存待执行的Sqoop命令的集合
    cmds = []
    for shell in shells:
        # sqoop命令类型
        sqoop_cmd_type = shell.attrib["type"]
        # 首先组装成sqoop命令头
        command = "sqoop " + sqoop_cmd_type
        # 获取
        params = shell.findall('./param')
        for param in params:
            # 获取key属性值
            key = param.attrib["key"]
            # 获取param标签的中间值
            value = param.text
            # 如果不是键值对形式的命令选项
            if (value == None or value == "" or value == " "):
                value = ""
            # 继续组装命令
            command += " --" + key + " " + value
        cmds.append(command)
    return cmds
