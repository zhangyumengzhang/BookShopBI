# -*- coding:UTF-8 -*-
from com.utils.py_env import PROJECT_CONF_DIR

import xml.etree.ElementTree as ET


def resolve_conf(type, dt):
    # 配置文件的路径
    confFile = PROJECT_CONF_DIR + "conversion.xml"

    # 解析配置文件
    xmlTree = ET.parse(confFile)
    eles = xmlTree.findall('./urls')
    rootEle = eles[0]

    # 用来保存漏斗的URL的集合
    urls = []

    for ele in rootEle.getChildren():
        if ele.tag == 'url':
            url = ele.text.strip()
            if url != None or url != '':
                print(url)
                urls.append(url)

    if len(urls) == 0:
        raise Exception('缺少参数，程序终止')

    return urls
