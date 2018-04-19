# spider_entry 词条蜘蛛

### 百度百科词条爬虫

## 说明
* 基于python3 开发
* 基于requests抓取HTTPS
* 将数据保存到mysql

## 需要的包

* requests
* pymysql
* beatufulsoup4
* urllib3

## 运行

* Run 'spider_main.py'

## 文件说明

* **html_downloader.py**: 数据抓取
* **html_outputer.py**: 数据输出
* **html_parser.py**: 数据解析
* **mysql.py**: 数据库操作
* **output.html**: 最终输出的HTML
* **spider.sql**: 数据库文件
* **spider_main.py**: 爬虫调度器
* **style.css**: HTML样式表
* **url_manager.py**: URL管理器
