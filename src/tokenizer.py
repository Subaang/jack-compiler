from itertools import filterfalse


class Tokenizer:
    def __init__(self):
        self.keywordList = ['class', 'constructor','function','method','field','static','var', 'int', 'char', 'boolean',
                            'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
        self.symbolList = ['{','}','(',')','[',']','.',',','+','-','*','/','&','|','<','>','=',"~",';']

    def preXMLTokenization(self,content):
        pre_res = []
        for i in content:
            pre_res += i.split(" ")

        for i in range(len(pre_res)):
            temp = []
            word = ""
            for j in pre_res[i]:
                if j in self.symbolList:
                    if word != "":
                        temp.append(word)
                        word = ""

                    temp.append(j)
                else:
                    word += j
            if word != "":
                temp.append(word)

            pre_res[i] = temp

        pre_res = [j for sub in pre_res for j in sub]

        res = []
        i = 0
        while i < len(pre_res):
            if pre_res[i][0] == '"':
                temp = ""
                temp += pre_res[i]
                temp += " "
                i += 1
                while pre_res[i][0] != '"':
                    temp += pre_res[i]
                    temp += " "
                    i += 1

                if temp == "":
                    res.append(temp)
                else:
                    res.append(temp)

            else:
                res.append(pre_res[i])

            i += 1
        return res

    def symbolAndKeywordTokenization(self,content):
        res = []
        for i in range(len(content)):
            if content[i] in self.keywordList:
                res.append(f"<keyword>{content[i]}</keyword>")

            elif content[i] in self.symbolList:
                if content[i] == '<':
                    res.append(f"<symbol>&lt;</symbol>")
                elif content[i] == '>':
                    res.append(f"<symbol>&gt;</symbol>")
                elif content[i] == '"':
                    res.append(f"<symbol>&quot;</symbol>")
                    print("CHECK THIS. HOW DID THIS HAPPEN -----------------------------------------")
                elif content[i] == '&':
                    res.append(f"<symbol>&amp;</symbol>")
                else:
                    res.append(f"<symbol>{content[i]}</symbol>")

            else:
                res.append(content[i])

        return res

    def intConstTokenization(self,content):
        res = []
        for i in range(len(content)):
            try:
                int(content[i])
                res.append("<intConst>" + content[i] + "</intConst>")
            except ValueError:
                res.append(content[i])

        return res

    def stringConstTokenization(self,content):
        res = []
        for i in range(len(content)):
            if content[i][0] == '"':
                res.append("<stringConst>" + content[i][1:] + "</stringConst>")
            else:
                res.append(content[i])

        return res

    def identifierTokenization(self,content):
        res = []
        for i in range(len(content)):
            if content[i][0].isalpha() or content[i][0].isalpha():
                res.append("<identifier>" + content[i] + "</identifier>")
            else:
                res.append(content[i])

        return res

    def verifyXML(self,content):
        for i in content:
            if i[0] != "<":
                return False

        return True


