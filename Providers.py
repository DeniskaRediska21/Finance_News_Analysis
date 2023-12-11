
class Provider():
    def __init__(self, url_main,what_main='a', what_sub='a', class_main='',class_sub='', bad_words_main=[], bad_words_sub=[]):
        self.url_main = url_main
        self.what_main = what_main
        self.what_sub = what_sub
        self.class_main = class_main
        self.class_sub = class_sub
        self.bad_words_main = bad_words_main
        self.bad_words_sub = bad_words_sub
    def list(self):
        print('russia-briefing')


Providers = {'russia-briefing': Provider(url_main ='https://www.russia-briefing.com/news/category/business/',
                                         what_main='a',
                                         what_sub='div',
                                         class_main='pull-left',
                                         class_sub='entry-content',
                                         bad_words_main=['asiabriefing'],
                                         bad_words_sub=['asiabriefing'])}
