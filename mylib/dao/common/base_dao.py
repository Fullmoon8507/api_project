import sqlite3


class BaseDao():

    def __init__(self, db):
        self.db = db


    def open(self):
        # 接続情報
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        # 変数を保持
        self.conn = conn
        self.cur = cur


    def close(self):
        # クローズ処理
        self.cur.close()
        self.conn.close()


    def commit(self):
        # コミット
        self.conn.commit()
