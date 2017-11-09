# 20171109CrawlBaiduBaike
[easy] a demo to crawl a static website.

###【爬虫初级】爬取百度百科静态页面数据案例

**目的：**
-1- 学习爬虫架构
-2- 学习常用爬虫模块
-3- 学习爬取静态页面

**准备：**
[课程资料][1]
收拾了一下pycharm,eclipse用着不顺手。工欲善其事必先利其器嘛。

**开动：**
**-1-** 项目架构

调度端 -> `管理器` `下载器` `解析器` -> 有效数据 url
					
				
**-2-** 管理器
**功能：**添加url；取出url；区分已爬和未爬；
**实现：**
`第一种方式:`内存，如python中的set()
	优点：可以自动去重
	缺点：内存空间有限，不适合大数据
`第二种方式:`MySQL，用table两列url和is_crawl即可
	优点：节省了内存
	缺点：需要写去重的语句
`第三种方式:`缓存数据库，如redis
	优点：高性能
	缺点：我不会-有待学 redis是C编写的



**-3-** 下载器**[核心]** 三种方式下载html页面
`第一种方式:`urlopen()直接打开
`第二种方式:`用Request类对象打开.Request类和http的Request、Response模型应该是对应的，可以对照着学。
`第三种方式:`创建openner，使用cookie、代理、加密、重定向等功能，打开url
以上三种方法最终都要用urlopen()；实践中，有必要了解HTTP头部，cookie和代理等基本知识，以便于深入学习。

python3.x中，urllib2和request合并形成了urllib，所以python3调用urlopen()要用urllib.request.urlopen()。第二种方式中用Request的时候要用urllib.request.Request

在cookiejar上python3.x也有变化，调用的时候要用http.cookiejar.CookieJar()

代码如下：
``` python
#coding: utf-8
import urllib.request
import http.cookiejar

url = "http://www.baidu.com"

print("Method 1")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("Method 2")
request = urllib.request.Request(url)
# 模拟浏览器请求
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("Method 3")
cj = http.cookiejar.CookieJar()
openner = urllib.request.build_opener( urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(openner)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(len(response3.read()))
print(cj)
```
附加：
[HTTP状态码][2]

**-4-** 解析器
`第一种方式:`正则表达式，模糊匹配解析
`第二种方式:`BeautifulSoup第三方库，用DOM树的方式获取标签内容。[官方使用文档][3]

示例代码：
``` python
from bs4 import BeautifulSoup
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""
soup = BeautifulSoup(
    html_doc,  #html文档字符
    'html.parser',
    from_encoding='utf-8'
)

# 获取全部
link1 = soup.find_all( 'a')
for node in link1:
    print( node.name, node['href'],node.get_text())

# 获取lacie
link2 = soup.find('a',href ="http://example.com/lacie" )
print(link2.get_text())

# 正则表达式
link3 = soup.find('a',href = re.compile(r"ll"))
print(link3.get_text())

# 获取段落名称
link4 = soup.find('p', class_ = "title")
print(link4.get_text())
```

**-5-** 真实静态爬虫的实现步骤：
`第一步:`确定进口url，审查页面元素，确定页面编码
`第二步:`完成每一部分代码，调试，运行


[1]:
http://www.imooc.com/learn/563
[2]:
https://baike.baidu.com/item/HTTP%E7%8A%B6%E6%80%81%E7%A0%81/5053660?fr=aladdin
[3]:
https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id15
