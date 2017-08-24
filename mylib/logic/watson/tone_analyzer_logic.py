from watson_developer_cloud import ToneAnalyzerV3
from mylib.dao.common.account_dao import AccountDao as AccountDao
from mylib.vo.watson.tone_analyzer_vo import ToneAnalyzerVo as ToneAnalyzerVo


db_name = "db.sqlite3"


def tone_analyze(sentence):

    # usernameとpasswordを取得
    id, pw = __get_id_pw()

    # ログイン認証
    tone_analyzer = ToneAnalyzerV3(
        username=id,
        password=pw,
        version="2016-05-19"
    )

    # 分析
    json_data_dict = tone_analyzer.tone(text=sentence)

    tone_categories = json_data_dict['document_tone']['tone_categories']

    # import pdb; pdb.set_trace()
    ret_list = []
    for tones in tone_categories:
        for key1, value1 in tones.items():
            if key1 == 'tones':

                for vdict in value1:
                    vo = ToneAnalyzerVo()
                    vo.category_id = tones['category_id']
                    vo.tone_id = vdict['tone_id']
                    vo.tone_name = vdict['tone_name']
                    vo.score = vdict['score']
                    __set_japanese_name(vo)

                    ret_list.append(vo)

    return ret_list


def __set_japanese_name(vo):

    id = vo.category_id
    if id == 'emotion_tone':
        vo.category_ja = '感情'
    elif id == 'language_tone':
        vo.category_ja = '言語'
    elif id == 'social_tone':
        vo.category_ja = '社会'

    id = vo.tone_id
    if id == 'anger':
        vo.tone_ja = '怒り'
    elif id == 'disgust':
        vo.tone_ja = '嫌悪感'
    elif id == 'fear':
        vo.tone_ja = '恐怖'
    elif id == 'joy':
        vo.tone_ja = '喜び'
    elif id == 'sadness':
        vo.tone_ja = '悲しみ'
    elif id == 'analytical':
        vo.tone_ja = '分析的'
    elif id == 'confident':
        vo.tone_ja = '自信'
    elif id == 'tentative':
        vo.tone_ja = '自信なさげな'
    elif id == 'openness_big5':
        vo.tone_ja = '開放性'
    elif id == 'conscientiousness_big5':
        vo.tone_ja = '誠実さ'
    elif id == 'extraversion_big5':
        vo.tone_ja = '外交性'
    elif id == 'agreeableness_big5':
        vo.tone_ja = '妥当性'
    elif id == 'emotional_range_big5':
        vo.tone_ja = '感情的な範囲'


def __get_id_pw():

    dao = AccountDao(db_name)

    dao.open()

    id_pw_tuple = dao.get_id_pw("tone_analyzer")

    dao.close()

    return id_pw_tuple
