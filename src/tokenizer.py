class Tokenizer:

    def __init__(self,content):
        self.content = content
        pass

    def preXMLTokenization(self):
        temp = []
        preXMLTokens = []
        for i in self.content:
            temp.append(i.split(" "))

        for i in temp:
            for j in i:
                preXMLTokens.append(j)

        return preXMLTokens




