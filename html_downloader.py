# coding:utf8
# 数据抓取类

import requests


class HtmlDownloader(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def download(self, url):
        if url is None:
            return None
        response = requests.get(url,headers=self.headers)
        if response.status_code != 200:
            return None
        response.encoding = 'utf-8'
        return response.content
