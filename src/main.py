import tokenizer

with open('D:/PythonProjects/jack-compiler/data/program.jack', 'r') as file:
    content = file.readlines()

content = [x.strip(" \n \t") for x in content]
content = [x for x in content if x != '']
content = [x for x in content if (x[0] != "/" and x[0] != "\n")]

tokenizer = tokenizer.Tokenizer(content)
preXMLTokens = tokenizer.preXMLTokenization()

print(preXMLTokens)

