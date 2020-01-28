from collections import defaultdict

# pip install nltk
import nltk
from nltk.stem import WordNetLemmatizer

class Statistics(object):

    # https://www.ibm.com/support/knowledgecenter/zh/SS5RWK_3.5.0/com.ibm.discovery.es.ta.doc/iiysspostagset.htm
    skipTags = [
        'DT', # 限定词
        'QT', # 量词
        'CD', # 基数
        'PRP', # 人称代词 (PP)
        'PRP$', # 物主代词 (PP$)
        'CC', # 并列连词
        'IN', # 介词或从属连词
        'JJ', # 形容词
        'WDT', # Wh 限定词
        'WRB', # Wh 副词
        'RB', # 副词
        'RBS', # 副词（最高级）
        'RBR', # 副词（比较级）
        'JJS', # 形容词（最高级）
        'JJR', # 形容词（比较级）
        'JJ', # 形容词
        'VB', # 动词（基本形式）
        'VBP', # 动词（现在时态，非第三人称单数）
        'VBZ', # 动词（现在时态，第三人称单数）
        'VBD', # 动词（过去时态）
        'VBN', # 动词（过去分词）
        'VBG', # 动词（动名词或现在分词）
        'MD',  # 情态动词
    ]

    nounTags = [
        'NN', # 名词（单数）
        'NNS', # 名词（复数）
        'NNP', # 专有名词（单数）
        'NNPS', # 专有名词（复数）
    ]

    skipWords = [
        'allows',
        'attacker',
        'aka',
        'buffer',
        'cause',
        'code',
        'cve',
        'data',
        'doe',
        'execute',
        'function',
        'packet',
        'server',
        'service',
        'remote',
        'vulnerability',
    ]

    def __init__(self):
        super(Statistics, self).__init__()
        self.statistics = defaultdict(int)
        self.lemmatizer = WordNetLemmatizer()
    
    def update(self, desc):
        tokens = nltk.word_tokenize(self.unification(desc))
        # 一个描述之内 一个关键词只应该被计算一次
        tokens = set(map(self.lemmatizer.lemmatize, set(tokens)))
        for t in tokens:
            self.statistics[t] += 1

    def sortByCount(self):
        statistics = sorted(self.statistics.items(), key=lambda d: d[1])
        for s in statistics:
            if s[1] < 3:
                continue
            if s[0] in self.skipWords:
                continue
            if len(s[0]) < 3:
                continue
            tag = nltk.pos_tag([s[0]])[0][1]
            if tag in self.skipTags:
                continue
            yield s[1], s[0], tag

    def getCounts(self, keys):
        for k in keys:
            print(k, s.statistics.get(k))

    @classmethod
    def unification(cls, sen):
        sen = sen.lower()
        # sen = sen.replace(',', '')
        return sen
