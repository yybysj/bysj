# -*- coding: utf-8 -*-
from scrapy import cmdline
from pyecharts import Bar,Pie
import string,json
import chardet

cmdline.execute("scrapy crawl douban -o movie.json".split())

bar1 = Bar('豆瓣Top250分类','柱状图',height=720, width=1200)
pie1 = Pie('豆瓣Top250分类',height=720, width=1200)
v1   = [  0   ,  0  ,  0   ,  0  ,  0   ,  0  ,  0   ,  0  ,  0  ,  0   ,  0  ,   0  ,  0  ,  0  ,  0   ,  0  ,   0  ,  0  ,   0  ,  0  ,   0  ,  0  ]
str1 = ['剧情','喜剧','动作','爱情','科幻','动画','悬疑','惊悚','恐怖','犯罪','同性','音乐','歌舞','传记','历史','战争','西部','奇幻','冒险','灾难','武侠','情色']

bar2 = Bar('豆瓣Top250国家','柱状图',height=720, width=1200)
pie2 = Pie('豆瓣Top250国家',height=720, width=1200)
v2   = [    0    ,  0  ,  0   ,  0  ,  0   ,  0  ,  0   ,  0  ,  0  ,    0   ,   0   ,   0  ,  0  ,   0   ,  0   ,   0   ,    0    ,   0   ,   0  ,  0  ,   0  ]
str2 = ['中国大陆','美国','香港','台湾','日本','韩国','英国','法国','德国','意大利','西班牙','印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦']

fs = file("movie.json")
result = json.load(fs)

for j in range(len(result)):
    # print j
    # print result[j]['movieInfo']
    # print chardet.detect(str1[1])
    movieinfo = result[j]['movieInfo'].encode('utf-8')
    for i in range(len(str1)):
        if movieinfo.find(str1[i]) != -1:
            v1[i] += 1

    for i in range(len(str2)):
        if movieinfo.find(str2[i]) != -1:
            v2[i] += 1

bar1.add('类型',str1,v1,is_more_utils = True,is_convert = False,bar_category_gap=0,is_datazoom_show=True)
bar2.add('国家',str2,v2,is_more_utils = True,is_convert = False,bar_category_gap=0,is_datazoom_show=True)
pie1.add('类型',str1,v1)
pie2.add('国家',str2,v2)
bar1.render("type_bar.html")
bar2.render("contry_bar.html")
pie1.render("type_pie.html")
pie2.render("contry_pie.html")