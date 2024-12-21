import tokenizer

with open('D:/PythonProjects/jack-compiler/data/test.jack', 'r') as file:
    content = file.readlines()

content = [x.strip(" \n\t") for x in content]
content = [x for x in content if x != '']
content = [x for x in content if (x[0] != "/" and x[0] != "\n")]

tokenizer1 = tokenizer.Tokenizer()
preXMLTokens = tokenizer1.preXMLTokenization(content)
symbolAndKeywordTokens = tokenizer1.symbolAndKeywordTokenization(preXMLTokens)
intTokens = tokenizer1.intConstTokenization(symbolAndKeywordTokens)
stringTokens = tokenizer1.stringConstTokenization(intTokens)
identifierTokens = tokenizer1.identifierTokenization(stringTokens)

tokenizedXML = identifierTokens.copy()

with open('D:/PythonProjects/jack-compiler/data/tokens.xml', 'w') as file:
    file.write('<tokens>\n')
    for i in tokenizedXML:
        file.write(i)
        file.write('\n')
    file.write('</tokens>')


if not tokenizer1.verifyXML(identifierTokens):
    print("PROBLEM ---------------------------")






