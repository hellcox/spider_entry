# coding:utf8
# 数据输出类

import time
from mysql import Mysql


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        else:
            self.datas.append(data)

    def output_html(self):
        fout = open('./output.html', 'w', encoding="utf-8")
        fout.write('<html>')
        fout.write(
            '<head><meta charset="utf-8"><link rel="stylesheet" type="text/css" href="./style.css"></head>')
        fout.write('<body>')
        fout.write('<table id ="table-1">')
        fout.write('<thead><tr><th>序号</th><th>标题</th><th>简介</th></tr></thead>')
        for index, data in enumerate(self.datas):
            num = index + 1
            fout.write('<tr>')
            fout.write('<td>%s</td>' % num)
            fout.write('<td>')
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('</td>')
            fout.write('<td>%s</td>' % data['content'])
            fout.write('</tr>')
        fout.write('</table>')

        fout.write('</body>')

        fout.write('</html>')

        fout.close()

    def add_data(self, data):
        now = int(time.time())
        nowDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        mysql = Mysql()

        row = mysql.select_row("select * from entry where entry_url=%s", *[data['url']])

        # 记录是否存在
        if row is None:
            # 不存在则插入
            data = {"entry_title": data['title'],
                    "entry_url": data['url'],
                    "entry_content": data['content'],
                    "add_time": now,
                    "update_time": now,
                    "add_date": nowDate,
                    "update_date": nowDate,
                    }
            insert_id = mysql.insert("entry", **data)
            print('\033[1;33m' + '【INSERT】' + '\033[0m')
            return insert_id
        else:
            # 存在则更新
            keys = [data['title'], data['content'], now, nowDate, data['url']]
            row_count = mysql.update(
                "update entry set entry_title=%s,entry_content=%s,update_time=%s,update_date=%s,entry_times=entry_times+1 where entry_url=%s",
                *keys)
            print('\033[1;34m' + '【UPDATE】' + '\033[0m')
            return row_count
