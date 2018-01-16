from random import randint
import random
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','+','*','-','?','_','=','$']
charset=characters+numbers+symbols
PasswordRange=25
aplength=5
duplicateRange=5
amount=10
amount_rules=1000
def LowercaseLetters():
    return 'l'
def UppercaseLetters():
    return 'u'
def CapitalizeLetters():
    return 'c'
def InvertCapitilizeLetters():
    return 'C'
def ToggleChars():
    return 't'
def ToggleCharAtIndex():
    return 'T'+str(randint(0,PasswordRange))
def Reverse():
    return 'f'
def RotateLeft():
    return '{'
def RotateRight():
    return '}'
def AppendChar():
    iterations=randint(1,aplength)
    rule="$"
    for i in range(0,iterations):
        rule=rule+charset[randint(0,len(charset)-1)]
    return rule
def PrependChar():
    iterations=randint(1,aplength)
    rule="^"
    for i in range(0,iterations):
        rule=rule+charset[randint(0,len(charset)-1)]
    return rule
def DeleteFirstChar():
    return '['
def DeleteLastChar():
    return ']'
def DeleteCharAtIndex():
    return 'D'+str(randint(0,PasswordRange))
def ExtractChars():
    start=randint(0,PasswordRange-1)
    stop=randint(start,PasswordRange)
    return 'x'+str(start)+str(stop)
def DeleteChars():
    start=randint(0,PasswordRange-1)
    stop=randint(start,PasswordRange)
    return 'O'+str(start)+str(stop)
def InsertChar():
    rule="i"+str(randint(0,PasswordRange))+charset[randint(0,len(charset)-1)]
    return rule
def OverwriteChar():
    rule="o"+str(randint(0,PasswordRange))+charset[randint(0,len(charset)-1)]
    return rule
def TruncateWord():
    return "'"+str(randint(0,PasswordRange))
def ReplaceCharWithChar():
    rule="s"+charset[randint(0,len(charset)-1)]+charset[randint(0,len(charset)-1)]
    return rule
def PurgeChar():
    rule='@'+charset[randint(0,len(charset)-1)]
    return rule
def DuplicateFirstChar():
    return "z"+str(randint(0,duplicateRange))
def DuplicateLastChar():
    return "Z"+str(randint(0,duplicateRange))
def DuplicateAll():
    return 'q'
methods=[LowercaseLetters,UppercaseLetters,CapitalizeLetters,InvertCapitilizeLetters,ToggleChars,ToggleCharAtIndex,Reverse,RotateLeft,RotateRight,AppendChar,PrependChar,DeleteFirstChar,DeleteLastChar,DeleteCharAtIndex,ExtractChars,DeleteChars,InsertChar,OverwriteChar,TruncateWord,ReplaceCharWithChar,PurgeChar,DuplicateFirstChar,DuplicateLastChar,DuplicateAll]
def GenerateRandomRules():
    print("Getting started");
    for m in range(0,amount_rules):
        rules=[];
        rules.append(":")
        for i in range(0,amount):
            rule=ReturnRandomRule()
            if(rules.count(rule)==0):
                rules.append(rule)
        SaveRulesToFile(str(m),rules)


def SaveRulesToFile(name,thelist):
    thefile=open('rr/'+name+'.rule','w')
    for item in thelist:
        thefile.write("%s\n" % item)
def ReturnRandomRule():
    rule=random.choice(methods)()
    return rule
def ReturnRandomRule2():
    rand=randint(0,len(methods)-1)
    print(str(rand))
    rule=methods[rand]()
    print(rule)
