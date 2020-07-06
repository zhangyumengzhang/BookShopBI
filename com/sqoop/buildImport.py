# -*- coding:UTF-8 -*-

from xml.etree import ElementTree
import com.utils.py_env as env


# 其中dt为昨天的日期，将由调度模块传入
def resolve_conf(dt):
    # 获取配置文件路径
    conf_file = env.PROJECT_CONF_DIR + "import.xml"
    # 解析配置文件
    xml_tree = ElementTree.parse(conf_file)

    # 获取所有的sqoop-shell元素
    shells = xml_tree.findall('./sqoop-shell')

    # 用来保存待执行的Sqoop命令的集合
    cmds = []

    for shell in shells:
        # 获取sqoop命令类型，如：import或export
        sqoop_cmd_type = shell.attrib["type"]
        # 获取导入类型，如：增量导入或全量导入
        import_type = shell.attrib["import_type"]
        # 获取
        params = shell.findall("./param")
        # 首先组装sqoop命令头
        command = "sqoop " + sqoop_cmd_type
        for param in params:
            if (import_type == "all"):
                import_condition = "< '" + dt + "'"
            elif (import_type == "add"):
                import_condition = "= '" + dt + "'"
            else:
                raise Exception

            key = param.attrib["key"]
            value = param.text
            if (value == None or value == "" or value == " "):
                value = ""

            if (key == "query"):
                value = value.replace("\$dt", import_condition)

            if (key == "hive-partition-value"):
                value = value.replace("$dt", dt)
            if(key== "Dorg.apache.sqoop.splitter.allow_text_splitter"):
                command += " \"-" + key + "=" + value + "\""
            else:
                command += " --" + key + " " + value
        cmds.append(command)

    return cmds
