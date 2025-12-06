import requests
import re
import time
#b变量为排名序列初始值
b=0
#打开创建文件
f=open(f"C:/Users/scx and hqy/Desktop/豆瓣top250.txt",mode="w",encoding='utf-8')
#循环页码
for i in range(0,250,25):
    url=f"https://movie.douban.com/top250?start={i}"
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWeb'
                            'Kit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
    response = requests.get(url,headers=headers).text
    #让程序暂停小段时间用以读取网页源代码
    time.sleep(1)
    #编写正则表达式，导演用的与主演栏目之间的空格为索引，但其中一个电影它没有主演导致它无法被识别，所以选择了用空格或者斜杠来匹配
    obj=re.compile((r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<div clas'
                    r's="bd">.*?导演: '
                    r'(?P<daoyan>.*?)(&nbsp;| / ).*?<br>(?P<nianfen>.*?)&nbsp;.*?'
                    r'<span class="rating_num" property="v:average">(?P<pingfen>.*?)</span>'),re.S)
    #获取的html里按照正则表达式进行匹配
    shuju=obj.finditer(response)
    #循环每一次的匹配结果并提取其中元素写入文件
    for item in shuju:
        b += 1
        name = item.group('name')
        daoyan = item.group('daoyan').strip()
        nianfen = item.group('nianfen').strip()
        pingfen = item.group('pingfen').strip()
        f.write(f"{b}.《{name}》\n导演:{daoyan}\n上映时间:{nianfen}\n评分：{pingfen}\n\n")
#循环结束关闭文件并给出提示
f.close()
print('豆瓣top250信息提取完毕')






