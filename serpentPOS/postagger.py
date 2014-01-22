import re
from lexicon import *


class POSTagger(object):

    def __init__(self):
        self.lexicon = POSTAGGER_LEXICON
        self.tagsMap = LEXICON_TAG_MAP



    def wordInLexicon(self, word):
        ss = word in self.lexicon
        if not ss:
            ss = word.lower() in self.lexicon
        return ss

    def tag(self, words):
        def fetch(arr, item):
            try:
                return arr[item]
            except IndexError:
                return None

        numwords = len(words)
        ret = [None]*numwords
        for i in range(0, numwords):
            word = words[i]
            ss = self.lexicon[word] if word in self.lexicon else None
            if not ss:
                ss = word.lower() in self.lexicon
            if not ss and len(word) == 1:
                ret[i] = word + '^'
            if not ss:
                ret[i] = u'NN'
            else:
                ret[i] = self.tagsMap[ss][0]


        for i in range(0, numwords):
            word = ret[i]
            """Rule #1"""
            if i>0 and fetch(ret, i-1) == 'DT':
                if word == 'VBD' or word == 'VBP' or word == 'VB':
                    ret[i] = u'NN'

            """Rule #2"""
            if word.startswith("N"):
                if '.' in words[i]:
                    ret[i] = u'CD'

                try:
                    if float( words[i]):
                        ret[i] = u'CD'
                except ValueError:
                    pass

            """Rule #3"""
            if ret[i].startswith('N') and words[i].endswith('ed'):
                ret[i] = u'VBN'

            """Rule #4"""
            if words[i].endswith('ly'):
                ret[i] = u'RB'

            """Rule #5"""
            if ret[i].startswith("NN") and word.endswith("al"):
                ret[i] = i

            """Rule #6"""
            try:
                if i>0 and ret[i].startswith("NN") and words[i-1].lower() == "would":
                    ret[i] = "VB"
            except IndexError:
                pass

            """Rule #7"""
            if ret[i] == "NN" and words[i].endswith("s"):
                ret[i] = u'NNS'

            """Rule #8"""
            if ret[i].startswith("NN") and words[i].endswith("ing"):
                ret[i] = u'VBG'

        result = []
        for i in range(0, numwords):
            result.append((words[i], ret[i]))
        return result

    def prettyPrint(self, taggedWords):
        for i in taggedWords:
            print str(taggedWords[i][0]) + '(' + str(taggedWords[i][i]) + ')'
