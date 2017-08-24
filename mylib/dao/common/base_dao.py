import sqlite3


class BaseDao():

    def __init__(self, db):
        self.db = db


    def open(self):
        # �ڑ����
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()

        # �ϐ���ێ�
        self.conn = conn
        self.cur = cur


    def close(self):
        # �N���[�Y����
        self.cur.close()
        self.conn.close()


    def commit(self):
        # �R�~�b�g
        self.conn.commit()
