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
