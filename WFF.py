import re
__all__= "WFF"
class WFF:
    def __int__(self,setString:str):
        self.target=setString
        self.errors=[]
    def printRule(self)->str:
        rules="请保证输入的语句中，原子命题，括号，联结符之间存在空格\
        为保证程序的正确运行，请将'→‘用LaTex语句 \\rightarrow替代，双条件用\\leftrightarrow替代\
        命题请使用大写字母，暂且不支持希伯来字母，后续学会后将完全使用正则表达式\
        合取请使用\\vee，析取请使用\\wedge，暂时不支持异或、同或, 表示“非”请使用/nor\
        样例：\
        ( P \leftarrow Q )  \\vee R \\wedge P"
        return rules
    def searchBracket(self):
        first="("
        second=")"
        targetList=list(self.target.split(" "))
        countF=targetList.count(first)
        countS=targetList.count(second)
        if countS!=countF:
            self.errors.append('wrong')
            return "括号没有封闭"
        else:
            self.errors.append(True)
            return True
    def findWrongChar(self):
        exceptions=[
            "\\vee )",
            "( \\vee",
            "\\wedge )",
            "( \\bigwedge",
            "/nor )",#这里可能还需要改动
        ]
        for i in exceptions:
            if self.target.find(i)!=-1:
                self.errors.append('wrong')
                return "语法错误，请检查一下符号位置"
        self.errors.append(True)
        return True
    def findWrongArrow(self):
        exceptions=[
            "\\rightarrow )",
            "( \\rightarrow",
            "\\leftarrow )",
            "( \\leftarrow",
            "( \\leftrightarrow",
            "\\leftrightarrow )"
        ]
        for i in exceptions:
            if self.target.find(i)!=-1:
                self.errors.append("Wrong")
                return "检查一下箭头语法是否有错"
        self.errors.append(True)
        return True
    def searchConnectAlpha(self):
        pureAlpha=r"[A-Z] [A-Z]"
        norAlpha=r"[A-Z] /nor [A-Z]"
        connectAl=re.compile(pureAlpha)
        resultAlpha=re.search(connectAl,self.target,flags=0)
        norAlpha=re.search(norAlpha,self.target,flags=0)
        if resultAlpha is None and norAlpha is None:
            self.errors.append(True)
            return True
        else:
            self.errors.append("wrong")
            return "命题之间确失联结词"
    def searchConnectConjuction(self):
        patterns=[
            r"\\.\w+\s{1}\\",#两个或者多个连续的联结词
            r"/nor.\\",#非的符号和联结词写在一起，这是一种情况
            r"\\.\w+./nor\s{1}\\",#多个符号之间出现/nor的情况
        ]
        for item1 in patterns:
            eachResult=re.search(re.compile(item1), self.target, flags=0)
            if eachResult is not None:
                self.errors.append("wrong")
                return "存在联结词连续性错误"
        self.errors.append(True)
        return True
    def findBlankBracket(self):
        blankBracket=re.compile(r"\( \)")
        result=re.search(blankBracket,self.target)
        if result is not None:
            self.errors.append("wrong")
            return "括号中缺少表达"
        self.errors.append(True)
        return True
    def findBracketFirSec(self):
        targetList=self.target.split(" ")
        firstBrack=0
        secondBrack=0
        bracket={
            "(":firstBrack,
            ")":secondBrack
        }
        for item in targetList:
            if item== "(" or item == ")":
                bracket[item]+=1
            if firstBrack<secondBrack:
                self.errors.append('wrong')
                return "存在不正确的括号"
        self.errors.append(True)
        return True
    #上面这个方法用于判断括号的个数和方向
    def findGap(self):
        gapBrack=r"\) \("#中途出现无效括号
        norGap=r"\) /nor \("
        result=re.search(gapBrack,self.target,flags=0)
        norGAp=re.search(norGap,self.target,flags=0)
        if result is not None or norGAp is not None:
            self.errors.append('wrong')
            return "括号之间缺少联结词"
        else:
            self.errors.append(True)
            return True
    def norText(self):
        searchNor=r"[A-Z] /nor"
        result=re.search(searchNor,self.target,flags=0)
        if result is not None:
            self.errors.append('wrong')
            return "命题变元后面不能出现‘非’"
        else:
            self.errors.append(True)
            return True
    def outcome(self)->list:
        answerList=[]
        if self.findGap() is not True:
            answerList.append(self.findGap())
        if self.findBracketFirSec() is not True:
            answerList.append(self.findBracketFirSec())
        if self.findBlankBracket() is not True:
            answerList.append(self.findBlankBracket())
        if self.searchBracket() is not True:
            answerList.append(self.searchBracket())
        if self.findWrongArrow() is not True:
            answerList.append(self.findWrongArrow())
        if self.findWrongChar() is not True:
            answerList.append(self.findWrongChar())
        if self.searchConnectAlpha() is not True:
            answerList.append(self.searchConnectAlpha())
        if self.searchConnectConjuction() is not True:
            answerList.append(self.searchConnectConjuction())
        if self.norText() is not True:
            answerList.append(self.norText())
        elif 'wrong' not in self.errors:
            endLine="这是一个合式公式"
            answerList.append(endLine)
        if "这是一个合式公式" not in answerList:
            answerList.append("这不是一个合式公式")
        return answerList
