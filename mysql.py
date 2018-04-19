# coding:utf8
# 数据库操作类

import pymysql


class Mysql:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "root"
        self.dataBase = "spider"
        self.charset = "utf8"
        self.cursorclass = pymysql.cursors.DictCursor
        self.cursor = None

        self.lastSql = None
        try:
            self.db = pymysql.connect(self.host, self.user, self.password, self.dataBase, charset=self.charset,
                                      cursorclass=self.cursorclass)
            self.cursor = self.db.cursor()
        except pymysql.Error as err:
            print('mysql connect error: ' + err)

    def insert(self, table, **data):
        fields = ','.join('`' + k + '`' for k in data.keys())
        values = ','.join(("%s",) * len(data))
        sql = 'INSERT INTO `%s` (%s) VALUES (%s)' % (table, fields, values)
        self.cursor.execute(sql, tuple(data.values()))
        insert_id = self.cursor.lastrowid
        self.db.commit()
        return insert_id

    def update(self, sql, *keys):
        change_rows = self.cursor.execute(sql, tuple(keys))
        self.db.commit()
        return change_rows

    def select_row(self, sql, *keys):
        self.cursor.execute(sql, tuple(keys))
        row = self.cursor.fetchone()
        return row

    def select_rows(self, sql, *keys):
        self.cursor.execute(sql, tuple(keys))
        rows = self.cursor.fetchall()
        return rows

    def delete(self):
        pass

    def get_last_sql(self):
        return self.lastSql
