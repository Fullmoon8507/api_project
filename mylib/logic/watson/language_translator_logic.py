from watson_developer_cloud import LanguageTranslatorV2
from mylib.dao.common.account_dao import AccountDao as AccountDao


db_name = "db.sqlite3"


def translate(sentence, before_lang, after_lang):

    # usernameとpasswordを取得
    id, pw = __get_id_pw()

    # ログイン認証
    language_translator = LanguageTranslatorV2(
        username=id,
        password=pw
    )

    # 翻訳
    translation = language_translator.translate(
        text=sentence,
        source=before_lang,
        target=after_lang
    )

    return translation


def __get_id_pw():

    dao = AccountDao(db_name)

    dao.open()

    id_pw_tuple = dao.get_id_pw("language_translator")

    dao.close()

    return id_pw_tuple
