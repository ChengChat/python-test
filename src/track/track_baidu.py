import urllib.request
from bs4 import BeautifulSoup

url_page = 'http://www.baidu.com'
print(url_page)
# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(url_page)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# 查找网页中的某个元素，例如查找所有的<title>标签
title = soup.find('title')
print(f"网页标题：{title.string}")

# 查找网页中的某个元素，例如查找所有的<div>标签
div_head = soup.find('div', {'id': 'head'})
div_top = div_head.find('div', {'id': "s-top-left"})
print(f"找到的<div>标签：{div_top}")
a = div_top.find_all('a')
for e in a:
    print(f"找到的<a>标签：{e.get_text()}")
