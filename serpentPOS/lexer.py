import re

class LexerNode(object):
    def __init__(self, string, pattern, regexs, case_sensitive):
        self.string = string
        self.children = []
        if string:
            self.matches = re.findall(pattern, string, case_sensitive)
            childElements = re.split(pattern, string, case_sensitive)
        if not hasattr(self, 'matches'):
            self.matches = []
            childElements = [string]

        if len(regexs) > 0:
            nextRegex = regexs[0]
            nextRegexes = regexs[1:]
            numElements = len(childElements)
            for  i in range(0,numElements):
                self.children.append(LexerNode(childElements[i], nextRegex[0], nextRegexes, nextRegex[1]))
        else:
            self.children = childElements;


    def fillArray(self, arr):
        numChildren = len(self.children)
        for i in range(numChildren):
            child = self.children[i]
            if hasattr(child, 'fillArray'):
                child.fillArray(arr)
            elif re.search(r'[^ \t\n\r]+', child, re.IGNORECASE):
                arr.append(child)
            if i < len(self.matches):
                match = self.matches[i]
                if re.search(r'[^ \t\n\r]+', match, re.IGNORECASE):
                    arr.append(match)


    def __str__(self):
        arr = []
        self.fillArray(arr)
        return str(arr)


class Lexer(object):
    def __init__(self):
        self.regexs = [(r'[0-9]*\.[0-9]+|[0-9]+',re.IGNORECASE), (r'[ \t\n\r]+', 0), (r'[\.\,\?\!]', re.IGNORECASE)]

    def lex(self, string):
        arr = []
        node = LexerNode(string, self.regexs[0][0], self.regexs[1:], self.regexs[0][1])
        node.fillArray(arr)
        return arr
