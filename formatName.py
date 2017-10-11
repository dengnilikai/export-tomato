'''
假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，
请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：

输入：['adam', 'LISA', 'barT']
输出：['Adam', 'Lisa', 'Bart']
'''

def formatName(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1;
NameList=["adam","LISA","barT"]
print(formatName("adam"))
#在python3中，要取得map生成的list，需在map前加list()
print(list(map(formatName,['abc','defF','AAAA'])))
