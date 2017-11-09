from bs4 import BeautifulSoup
import re
import urllib
import urllib.parse

class HtmlParser():

    def parse(self,url,html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(
            html_cont,  # html文档字符
            'html.parser',
            from_encoding='utf-8'
        )


        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return new_urls,new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href = re.compile(r"/item/+"))


        for link in links:
            new_url = link['href']
            # 按照url的去匹配，生出拼接url
            # urlpaser == urllib.parse in python 3.x
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(new_full_url)
            #new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_data = {}
        #url
        res_data['url'] = url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data