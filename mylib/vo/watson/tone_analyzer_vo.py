class ToneAnalyzerVo():

    def __init__(self):
        self.category_id = ""
        self.tone_id = ""
        self.tone_name = ""
        self.score = 0.0
        self.category_ja = ""
        self.tone_ja = ""

    def display(self):
        s = self.category_id + "," + \
            self.tone_id + "," + \
            self.tone_name + "," + \
            str(self.score) + "," + \
            self.category_ja + "," + \
            self.tone_ja

        return s
