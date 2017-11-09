import urlManager
import htmlDownload
import htmlParser
import htmlPrinter


class Controller(object):
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.downloader = htmlDownload.HtmlDownload()
        self.parser = htmlParser.HtmlParser()
        self.printer = htmlPrinter.HtmlPrinter()

    def crawl(self,root_url):
        count = 1

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s'% (count,new_url))
                html_cont = self.downloader.download(new_url)
                new_url,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_url)
                self.printer.collect_data(new_data)

                if count == 10:
                    break
                count = count + 1
            except:
                print('craw failed')

        self.printer.output_html()

if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = Controller()
    obj_spider.crawl(root_url)