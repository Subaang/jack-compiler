import tokenizer
import compiler
import os

os.chdir("D:/PythonProjects/jack-compiler/data/jack_programs")
for filePath in os.listdir():
    with open(filePath, 'r') as file:
        content = file.readlines()

    for i in range(len(content)):  # Removes inline comments
        if '//' in content[i]:
            content[i] = content[i][:content[i].index('//')]

    content = [x.strip(" \n\t") for x in content]
    content = [x for x in content if x != '']
    content = [x for x in content if (x[0] != "/" and x[0] != "\n")]

    print(content)

    tokenizer1 = tokenizer.Tokenizer(content)
    tokenizedXML = tokenizer1.tokenize()
    compiler1 = compiler.CompilationEngine(tokenizedXML)

    output_files = [x[:-5]+".xml" for x in os.listdir()]

    for i in output_files:
        with open(f'D:/PythonProjects/jack-compiler/data/xml_outputs/{i}', 'w') as file:
            for i in compiler1.compiled:
                file.write(i)
                file.write('\n')


