import os

from com.utils.py_env import HADOOP_PATH, PROJECT_LIB_DIR


def count_urls(start, end, urls):
    # MapReduce作业的输入路径，即conversion_input表的HDFS地址
    inputPath = "/user/warehouse/conversion_input/dt=" + start + "-" + end
    # MapReduce作业的输出路径
    outputPath = "/user/warehouse/conversion_out"
    # 删除上一次作业输出目录
    os.system(HADOOP_PATH + "hadoop dfs -rmr " + outputPath)
    # 将表示漏斗的正则表达式拼装成一个字符串，作为参数传给MapReduce作业
    urlstr = ""
    for i in range(len(urls)):
        if (i == len(urls) - 1):
            urlstr += urls[i]
        else:
            urlstr += urls[i] + " "

    # 拼接成shell命令
    shell = HADOOP_PATH + "hadoop jar " + PROJECT_LIB_DIR + "conversion.jar com.conversion.mr.Driver " + inputPath + " " + outputPath + " " + urlstr
    # 执行命令
    os.system(shell)
