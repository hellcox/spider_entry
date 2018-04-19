# coding:utf8
# 爬虫调度器
# 需安装包：requests pymysql beatufulsoup4 urllib3
# Date : 2018-04-19

import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parper = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 将起始URL加入URL管理器
        self.urls.add_new_url(root_url)
        # 当有待抓取的URL时执行逻辑
        while self.urls.has_new_url():
            # 抓取次数超过则退出抓取
            if count > 5:
                break

            try:
                # 获取带抓取URL总数
                size = self.urls.get_urls_count()
                print("【url size】:", size)
                # 获取带抓取URL
                new_url = self.urls.get_new_url()
                print("【url down】:", count, new_url)
                html_cont = self.downloader.download(new_url)
                # 解析抓取的内容
                new_urls, new_data = self.parper.parse(new_url, html_cont)
                print("【entry title】:", new_data['title'])
                # 添加待抓取的URLS
                self.urls.add_new_urls(new_urls)
                # 添加解析的数据
                self.outputer.collect_data(new_data)
                # 数据入库 若无数据库环境请注释
                self.outputer.add_data(new_data)
                # 抓取次数加一
                count = count + 1
            except:
                # 抓取次数加一
                count = count + 1
                print('\033[1;31m' + '【FAILED】Craw Failed' + '\033[0m')

        # 数据输出 HTML
        self.outputer.output_html()

if __name__ == "__main__":
    print('========== 蜘蛛开始活动 ==========')
    root_url = "https://baike.baidu.com/item/Python/407313"
    spider = SpiderMain()
    spider.craw(root_url)
    print('========== 蜘蛛结束活动 ==========')
