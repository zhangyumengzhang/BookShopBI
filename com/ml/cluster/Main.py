import sys

from com.ml.cluster.dimension_and_normalization import prepare_normaliz
from com.ml.cluster.user_cluster import cluster_output, get_finalresult

if __name__ == '__main__':
    start = sys.argv[1]
    end = sys.argv[2]

    # 准备数据并做数据归一化
    prepare_normaliz(start, end)

    # 聚类并输出
    cluster_output()

    # 得到聚类结果
    get_finalresult()
