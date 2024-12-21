
class Tokenizer:
    def __init__(self,content):
        self.content = content
        self.preXMLTokens = []

        self.keywordList = ['class', 'constructor','function','method','field','static','var', 'int', 'char', 'boolean',
                            'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
        self.postKeywordList = []

        pass

    def preXMLTokenization(self):
        temp = []
        for i in self.content:
            temp.append(i.split(" "))

        for i in temp:
            for j in i:
                self.preXMLTokens.append(j)

        return self.preXMLTokens

    def keywordTokenization(self):
        for i in range(len(self.preXMLTokens)):
            if self.preXMLTokens[i] in self.keywordList:
                self.postKeywordList.append(f"<keyword>{self.preXMLTokens[i]}</keyword>")
            else:
                self.postKeywordList.append(self.preXMLTokens[i])

        return self.postKeywordList







