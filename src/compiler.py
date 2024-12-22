import tokenizer



def error():
    print("ERROR")
    exit()


class CompilationEngine:
    def __init__(self,tokens):
        self.typeList = ["int", "char", "boolean","className"]
        self.tokens = tokens
        self.compiled = []
        self.i = 0

        self.compileClass()

    def eat(self,terminal_list):
        token = self.tokens[self.i]
        tokenType = tokenizer.tokenType(token)

        if tokenType == "KEYWORD":
            if tokenizer.keyword(token) not in terminal_list:
               error()

        elif tokenType == "SYMBOL":
            if tokenizer.symbol(token) not in terminal_list:
                error()

        elif tokenType == "INT_CONST":
            if terminal_list[0] != "INT_CONST":
                error()

        elif tokenType == "STRING_CONST":
            if tokenizer.stringVal(token)[0] != terminal_list:
                error()

        elif tokenType == "IDENTIFIER":
            if terminal_list[0] != "IDENTIFIER":
                error()

        self.compiled.append(token)
        self.i += 1

    def compileClass(self):
        self.compiled.append("<class>")
        self.eat(["class"])
        self.eat(["IDENTIFIER"])
        self.eat(["{"])
        self.compileClassVarDec()
        #self.compileSubroutineDec()
        self.eat(["}"])
        self.compiled.append("</class>")

    def compileClassVarDec(self):
        while tokenizer.tokenType(self.tokens[self.i]) == "KEYWORD" and tokenizer.keyword(self.tokens[self.i]) in ["field", "static"]:
            self.compiled.append("<classVarDec>")
            self.eat(["field","static"])
            self.eat(self.typeList)
            self.eat(["IDENTIFIER"])

            while (tokenizer.tokenType(self.tokens[self.i]) == "SYMBOL" and tokenizer.symbol(self.tokens[self.i]) == ";") is False:
                self.eat([","])
                self.eat(["IDENTIFIER"])

            self.eat([";"])
            self.compiled.append("</classVarDec>")

    def compileSubroutineDec(self):
        self.eat(["constructor","function","method"])





