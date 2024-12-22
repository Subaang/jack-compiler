import tokenizer
import compiler

with open('D:/PythonProjects/jack-compiler/data/test.jack', 'r') as file:
    content = file.readlines()

content = [x.strip(" \n\t") for x in content]
content = [x for x in content if x != '']
content = [x for x in content if (x[0] != "/" and x[0] != "\n")]

tokenizer1 = tokenizer.Tokenizer()
tokenizedXML = tokenizer1.tokenize(content)

with open('D:/PythonProjects/jack-compiler/data/tokens.xml', 'w') as file:
    file.write('<tokens>\n')
    for i in tokenizedXML:
        file.write(i)
        file.write('\n')
    file.write('</tokens>')




