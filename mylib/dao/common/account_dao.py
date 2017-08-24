from mylib.dao.common.base_dao import BaseDao as BaseDao


class AccountDao(BaseDao):

    def __init__(self, db):
        super().__init__(db)

    def get_id_pw(self, site):

        # SQL文の作成
        sql = "select * from common_account"
        sql += " where site=\'" + site + "\'"

        # SQL実行
        self.cur.execute(sql)

        row_list = self.cur.fetchall()

        return (row_list[0][1], row_list[0][2])
