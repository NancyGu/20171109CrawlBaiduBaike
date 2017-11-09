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