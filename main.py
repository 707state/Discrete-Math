import re
print("请保证输入的语句中，原子命题，括号，联结符之间存在空格")
print("为保证程序的正确运行，请将'→‘用LaTex语句 \\rightarrow替代，双条件用\\leftrightarrow替代")
print("命题请使用大写字母，暂且不支持希伯来字母，后续学会后将完全使用正则表达式")
print("合取请使用\\bigvee，析取请使用\\bigwedge，暂时不支持异或、同或")
print("样例：")
print("( P \leftarrow Q ) \\bigvee R \\bigwedge P")
def searchBracket(text:str):
    first="("
    second=")"
    list_i=list(text.split(" "))
    f=list_i.count(first)
    s=list_i.count(second)
    if f!=s:
        return "括号没有封闭"
    else:
        return True
def get_string():
    input_line=input()
    return input_line
def find_condi(text:str):
    exceptions=[
        "\\bigvee )",
        "( \\bigvee",
        "\\bigwedge )",
        "( \\bigwedge",
    ]
    for i in exceptions:
        if(text.find(i)!=-1):
            return "语法错误，检查一下是否合取或析取符号的位置"
    return True
def find_fault(text:str):
    exceptions=[
        "\\rightarrow )",
        "( \\rightarrow",
        "\\leftarrow )",
        "( \\leftarrow",
        "( \\leftrightarrow",
        "\\leftrightarrow )"
    ]
    for i in exceptions:
        if(text.find(i)!=-1):
            return "语法错误，检查一下是否条件符号的位置"
    return True
def search_con_alpha(test:str):
    reg=re.compile("[A-Z] [A-Z]")
    t=re.search(reg,test,flags=0)
    if t==None:
        return True
    else:
        return "命题之间必须有联结词"
def search_co_conj(text:str):
    pattern=re.compile(r"\\.\w+\s{1}\\")
    t=re.search(pattern,text)
    if t!=None:
        return "存在联接符连续的错误"
    else:
        return True
def find_blank_bracket(text:str):
    pat=re.compile(r"\( \)")
    t=re.search(pat,text)
    if t!=None:
        return "括号里面没有东西"
    return True
def bracket_first_second(text:str):
    text_copy=text.split(" ")
    first_br=0
    second_br=0
    for i in text_copy:
        if i =="(":
            first_br+=1
        elif i ==")":
            second_br+=1
        if(second_br>first_br):
            return "存在不正确的括号"
    return True
def find_gap(text):
    pat=re.compile(r"\) \(")
    t=re.search(pat,text)
    if t!=None:
        return "两个括号之间缺少联结词"
    else:
        return True
if __name__=="__main__":
    while True:
        test=get_string()
        wor2=find_fault(test)
        wor1=search_con_alpha(test)
        wor3=searchBracket(test)
        wor4=find_condi(test)
        wor5=search_co_conj(test)
        wor6=find_blank_bracket(test)
        wor7=bracket_first_second(test)
        wor8=find_gap(test)
        if wor1==True and wor2 ==True and wor3==True and wor4==True and wor5==True and wor6==True and wor7==True and wor8==True:
            print("这是一个合式公式")
        else:
            list_wor=[str(wor1),str(wor2),str(wor3),str(wor4),str(wor5),str(wor6),str(wor7),str(wor8)]
            print("这不是一个合式公式")
            print("\n".join(list_wor))