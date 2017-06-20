# encoding=utf-8
import jieba

# seg_list = jieba.cut("轩辕之时，神农氏世衰。诸侯相侵伐，暴虐百姓，而神农氏弗能征。	", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# # seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

# # seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# # print(", ".join(seg_list))

# # seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# # print(", ".join(seg_list))

import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags_with_weight.py [file name] -k [top k] -w [with weight=1 or 0]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
parser.add_option("-w", dest="withWeight")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

if opt.withWeight is None:
    withWeight = False
else:
    if int(opt.withWeight) is 1:
        withWeight = True
    else:
        withWeight = False

content = open(file_name, 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=withWeight)

if withWeight is True:
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
else:
    print(",".join(tags))